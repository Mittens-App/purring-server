import ast
import unittest
import os
from .result import ResultSuite

class AutomationManager :
    __file_paths = None

    def __init__(self) -> None:
        self.flush()
        self.__verbosity = 1

    def flush(self):
        self.__file_paths = []

        return self
    
    def add_file(self, file_path, argv=None):
        self.__file_paths.append(_FilePaths(
            path=file_path,
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
        with open(file_path, 'r') as file:
            source = file.read()

        comments = self.__get_comments(source=source)

        filename = os.path.basename(file.path)
        path = os.path.dirname(file.path)
        discover = unittest.defaultTestLoader.discover(path, pattern=filename, top_level_dir=path)

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
        is_success = True
        errors = []
        failures = []
        skipped = []

        for file in self.__file_paths:
            test_result = None
            if file.argv is None:
                
                filename = os.path.basename(file.path)
                path = os.path.dirname(file.path)
                discover = unittest.defaultTestLoader.discover(path, pattern=filename, top_level_dir=path) # rewrite top_level_dir tiap load file
                test_result = unittest.TextTestRunner(verbosity=self.__verbosity).run(discover)
            else:
                test_result = self.__with_argv(file_path=file.path, argv=file.argv)

            test_count += test_result.testsRun
            if test_result.wasSuccessful() is False:
                is_success = False
            errors += test_result.errors
            failures += test_result.failures
            skipped += test_result.skipped

        return ResultSuite(
            count=test_count,
            success=is_success,
            errors=errors,
            failures=failures,
            skipped=skipped
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