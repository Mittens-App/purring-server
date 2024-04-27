from fastapi import Depends, status as http_status
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from src.v1.repositories.testcase_repository import TestcaseRepository
from src.v1.repositories.result_repository import ResultRepository
from src.v1.models.testcase import ResultEnum
from src.v1.models.result import StatusEnum, Result, ResultTags, ResultMessage
from src.v1.models.result_suite import ResultCase
from src.v1.gateways.http_auth import Result as HttpResult
from src.v1.services.manager import AutomationManager

class TestcaseService:
    testcaseRepo: TestcaseRepository
    resultRepo: ResultRepository
    manager: AutomationManager
    
    def __init__(self, testcaseRepo: TestcaseRepository = Depends(), resultRepo: ResultRepository = Depends(), manager: AutomationManager = Depends()):
        self.testcaseRepo = testcaseRepo
        self.resultRepo = resultRepo
        self.manager = manager
    
    def get(self, id: int):
        return self.testcaseRepo.get(id)
    
    def run(self, id: int, executor: str):
        testcase = self.testcaseRepo.getWithTags(id)

        body = HttpResult(
            body=StatusEnum.success,
            status=http_status.HTTP_200_OK
        )

        if testcase is None or len(testcase) == 0:
            body.body = StatusEnum.failed
            body.status = http_status.HTTP_404_NOT_FOUND
            return body
        
        date = datetime.now()
        result = Result()
        result.description = testcase[0].TestCase.description
        result.duration = 0
        result.execute_date = date
        result.effectiveness = 0
        result.executor = executor
        result.name = testcase[0].TestCase.name
        result.success_count= 0
        result.test_count = 0
        result.test_status= StatusEnum.running
        testcase[0].TestCase.last_execute_date = date

        isError = False
        try:
            result = self.resultRepo.create(result)
            tags = []

            for case in testcase:
                if case.TestCaseTags is None:
                    break
                tag = ResultTags()
                tag.tag_id = case.Tag.id
                tag.result_id = result.id
                tag.tag_color = case.Tag.color
                tag.tag_name = case.Tag.name
                tags.append(tag)

            if len(tags) > 0:
                self.resultRepo.createTags(tags)
        except Exception as e:
            error = str(e.__dict__)
            print(error)
            isError = True
        
        if isError is True:
            self.resultRepo.rollback()
            body.body = StatusEnum.failed
            body.status = http_status.HTTP_500_INTERNAL_SERVER_ERROR
            return body

        self.resultRepo.commit()

        file = testcase[0].TestCase.file
        self.manager.set_file(file)
        result_suite = self.manager.run(use_worker=False)

        result_detail: ResultCase = result_suite.resultcase()[0]

        result.duration = result_suite.duration()
        result.effectiveness = result_suite.effectiveness()
        result.success_count= result_detail.test_count - len(result_detail.fails())
        result.test_count = result_suite.test_count()
        result.test_status= StatusEnum.success
        testcase[0].TestCase.last_result = ResultEnum.success

        if result_suite.is_success() is False:
            result.test_status= StatusEnum.failed
            body.body = StatusEnum.failed
            testcase[0].TestCase.last_result = ResultEnum.failed

        msgs = []
        separator = 'Stacktrace:'
        for fail in result_detail.fails():
            msg = ResultMessage()
            trimmed = fail.msg.split(separator, 1)[0]
            msg.message = trimmed
            msg.result_id = result.id
            msg.result_method = fail.method
            msg.result_type = fail.type
            msgs.append(msg)
        
        if len(msgs) > 0:
            self.resultRepo.createMessage(msgs)

        self.resultRepo.commit()
        
        return body
