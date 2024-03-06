import ast
import unittest
import os
from .result import ResultSuite

class AutomationManager :
    __files = None
    __argvs = None
    __filename = None
    __path = None
    __abs_filepath = None

    def __init__(self) -> None:
        self.flush()
        self.__verbosity = 1

    def flush(self):
        self.__abs_filepath = None
        self.__filename = None
        self.__path = None
        self.__files = []
        self.__argvs = []

        return self
    
    def add_file(self, file_path, argv=None):
        self.__abs_filepath = file_path
        self.__filename = os.path.basename(file_path)
        self.__path = os.path.dirname(file_path)
        self.__files.append({
            "path": self.__path,
            "filename":  self.__filename,
            "filepath": self.__abs_filepath
        })
        self.__argvs.append(argv)

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
    
    def list_test_functions(self):
        with open(self.__abs_filepath, 'r') as file:
            source = file.read()

        comments = self.__get_comments(source=source)

        discover = unittest.defaultTestLoader.discover(self.__path, pattern=self.__filename)

        test_suites = unittest.TestSuite(discover)

        # check test_suites length. throws not found exception
        test_cases = test_suites._tests[0]

        test_functions = []
        for tase_case in test_cases:
            for case in tase_case: 
                defName = case._testMethodName
                test_functions.append((defName,comments[defName]))

        return test_functions

    def run(self):
        
        test_count = 0

        for i, file in enumerate(self.__files):
            print(i) 





        result_suite = ResultSuite(
            count=test_count,
            success=test_result.wasSuccessful(),
            errors=test_result.errors,
            failures=test_result.failures,
            skipped=test_result.skipped
        )

        return result_suite



        test_result = None
        if len(argv) != 0: 
            test_result = self.__with_argv(argv)
        else:
            discover = unittest.defaultTestLoader.discover(self.__path, pattern=self.__filename)
            test_result = unittest.TextTestRunner(verbosity=self.__verbosity).run(discover)
        
        self.flush()

        result_suite = ResultSuite(
            count=test_result.testsRun,
            success=test_result.wasSuccessful(),
            errors=test_result.errors,
            failures=test_result.failures,
            skipped=test_result.skipped
        )

        return result_suite

    def __with_argv(self, argv):
        import sys
        import importlib.util
        from pathlib import Path

        sys.path.append(self.__path)

        test_module_name = Path(self.__abs_filepath).stem
        test_module = importlib.import_module(test_module_name)
        test_runner = unittest.TextTestRunner(verbosity=self.__verbosity)

        test_result = unittest.TestProgram(module=test_module, exit=False, testRunner=test_runner, argv=argv).result

        # Remove the reference to the module from the namespace
        del sys.modules[test_module_name]

        return test_result


# run testsuite