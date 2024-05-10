import ast
import unittest
import os
from datetime import datetime
import concurrent.futures
from src.v1.models.result_suite import ResultSuite, ResultCase
from config.loader import ConfigLoad as cfg

class AutomationManager :
    __file_paths = None

    def __init__(self) -> None:
        self.flush()
        self.__verbosity = 1
        self.__source_dir = cfg["source"]

    def flush(self):
        self.__file_paths = []

        return self
    
    def add_file(self, file_path, argv=None):
        path = file_path
        if self.__source_dir is not False:
            path = "/".join([self.__source_dir, file_path])

        self.__file_paths.append(_FilePaths(
            path= path,
            argv=argv
        ))

        return self

    def set_file(self, file_path, argv=None):
        self.flush()

        self.add_file(file_path=file_path, argv=argv)        

        return self
    
    def set_files(self, file_paths):
        self.flush()

        for file in file_paths:
            self.add_file(file_path=file)

        return self

    def __get_comments(self, source):
        comments = {}
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                docs = ast.get_docstring(node) or ''
                comments [node.name] = docs

        return comments
    
    def get_functions(self, file_path):
        if self.__source_dir is not False:
            file_path = "/".join([self.__source_dir, file_path])
        
        with open(file_path, 'r') as file:
            source = file.read()

        comments = self.__get_comments(source=source)

        filename = os.path.basename(file_path)
        path = os.path.dirname(file_path)
        discover = unittest.defaultTestLoader.discover(path, pattern=filename, top_level_dir=path)

        test_suites = unittest.TestSuite(discover)

        # check test_suites length. throws not found exception
        test_cases = test_suites._tests[0]

        functions = []
        classname = None
        for test_case in test_cases:
            for case in test_case: 
                classname = case.__class__.__name__
                defName = case._testMethodName
                functions.append(_Function(name=defName, comment=comments[defName]))

        return _TestClass(
            classname=classname,
            path=file_path,
            functions=functions
        )

    def run(self, use_worker=True, worker_pool=5):

        if len(self.__file_paths) <= 1 or use_worker is False:
            result = self.__run_suite(list=self.__file_paths)
            self.flush()
            return result
        else:
            print("use worker") # need logger gaes

            total_test = 0
            total_fail = 0
            total_duration = 0
            is_success = True
            all_resultcase = []
            list_result=[]
            starttime = datetime.now()

            # Create a ThreadPoolExecutor
            with concurrent.futures.ThreadPoolExecutor(max_workers=worker_pool) as executor:
                future_results = [executor.submit(self.__run_suite, [s]) for s in self.__file_paths]

                for future in concurrent.futures.as_completed(future_results):
                    list_result.append(future.result())

            # thread joined
            for result in list_result:
                total_test += result.test_count()
                total_fail += result.fail_count()
                total_duration += result.duration()
                all_resultcase += result.resultcase()
                if result.is_success() is False:
                    is_success = False
    
            endtime = datetime.now()
            diff = endtime - starttime
            total_duration = diff.total_seconds()

            self.flush()
            return ResultSuite(
                success=is_success,
                count=total_test,
                fail_count=total_fail,
                duration=total_duration,
                resultcase=all_resultcase
            )

    def __run_suite(self, list=[]):
        total_test = 0
        total_fail = 0
        total_duration = 0
        is_success = True
        all_resultcase = []
    
        for file in list:
            test_result = None
            starttime = datetime.now()

            # if file.argv is None:
            #     filename = os.path.basename(file.path)
            #     path = os.path.dirname(file.path)
            #     # bug multi thread
            #     discover = unittest.defaultTestLoader.discover(path, pattern=filename, top_level_dir=path) # rewrite top_level_dir tiap load file
            #     test_result = unittest.TextTestRunner(verbosity=self.__verbosity).run(discover)
                
            # else:
            test_result = self.__with_argv(file_path=file.path, argv=file.argv)

            case_classname = test_result._previousTestClass.__name__
            case_test_count = test_result.testsRun
            endtime = datetime.now()
            diff = endtime - starttime
            case_duration = diff.total_seconds()
            case_status = test_result.wasSuccessful()

            result_case = ResultCase(
                classname=case_classname,
                duration=case_duration,
                file_path=file.path,
                test_count=case_test_count,
                success=case_status,
                errors=test_result.errors,
                failures=test_result.failures,
                skipped=test_result.skipped,
            )

            total_duration += case_duration
            total_test += case_test_count
            total_fail += len(result_case.fails())
            if case_status is False:
                is_success = False
            all_resultcase.append(result_case)

        return ResultSuite(
            success=is_success,
            count=total_test,
            fail_count=total_fail,
            duration=total_duration,
            resultcase=all_resultcase
        )

    def __with_argv(self, file_path, argv):
        import sys
        import importlib.util
        from pathlib import Path

        path = os.path.dirname(file_path)
        sys.path.append(path)
        test_module_name = Path(file_path).stem
        test_module = importlib.import_module(test_module_name)
        test_runner = unittest.TextTestRunner(verbosity=self.__verbosity)

        test_result = unittest.TestProgram(module=test_module, exit=False, testRunner=test_runner, argv=argv).result

        # Remove the reference to the module from the namespace
        del sys.modules[test_module_name]

        return test_result

class _FilePaths:
    def __init__(self, path=None, argv=None):
        self.path = path
        self.argv = argv

class _Function:
    def __init__(self, name=None, comment=None):
        self.name = name
        self.comment = comment

class _TestClass:
    def __init__(self, classname=None, path=None, functions=[]):
        self.classname = classname
        self.path = path
        self.functions = functions