
class ResultSuite(object):

    def __init__(self, count=0, success=False, fail_count=0, resultcase=[], duration=0):
        self.__count = count
        self.__success = success
        self.__fail_count = fail_count
        self.__resultcase = resultcase
        self.__duration = duration

    def test_count(self):
        return self.__count
    
    def fail_count(self):
        return self.__fail_count

    def is_success(self):
        return self.__success
    
    def effectiveness(self):
        # https://www.browserstack.com/guide/top-test-automation-metrics
        # Automation Pass Rate = (no. of cases that passed / no. of test cases executed) * 100

        return (self.test_count() - self.__fail_count) / self.test_count() * 100
    
    def resultcase(self):
        return self.__resultcase
    
    def duration(self):
        return self.__duration

class _Fails:
    def __init__(self, type=None, method=None, msg=None):
        self.type = type
        self.method = method
        self.msg = msg

class ResultCase(object):
    def __init__(self, classname=None, duration=0, file_path=None, test_count=0, success=False, failures=[], errors=[], skipped=[]):
        self.classname = classname
        self.duration = duration
        self.file_path = file_path
        self.test_count = test_count
        self.success = success
        self.__failures = failures
        self.__errors = errors
        self.__skipped = skipped
        self.__type_error = "ERROR"
        self.__type_failed = "FAILED"
        self.__type_skip = "SKIPPED"
    
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