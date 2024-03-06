
class ResultSuite(object):

    def __init__(self, count=0, success=False, failures=[], errors=[], skipped=[]):
        self.__count = count
        self.__success = success
        self.__failures = failures
        self.__errors = errors
        self.__skipped = skipped
        self.__type_error = "ERROR"
        self.__type_failed = "FAILED"
        self.__type_skip = "SKIPPED"

    def test_count(self):
        return self.__count
    
    def is_success(self):
        return self.__success
    
    def effectiveness(self):
        # https://www.browserstack.com/guide/top-test-automation-metrics
        # Automation Pass Rate = (no. of cases that passed / no. of test cases executed) * 100

        return (self.test_count() - len(self.fails())) / self.test_count() * 100

    def fails(self):

        list_fails = []

        for fail, err in self.__failures:
            list_fails.append(_Fails(
                type= self.__type_failed,
                method=fail._testMethodName,
                msg=err
            ))

        for error, err in self.__errors:
            list_fails.append(_Fails(
                type= self.__type_error,
                method=error._testMethodName,
                msg=err
            ))

        for skip, err in self.__skipped:
            list_fails.append(_Fails(
                type= self.__type_skip,
                method=skip._testMethodName,
                msg=err
            ))

        return list_fails

class _Fails:
    def __init__(self, type=None, method=None, msg=None):
        self.type = type
        self.method = method
        self.msg = msg