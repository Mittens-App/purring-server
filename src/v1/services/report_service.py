from grpc import StatusCode as rpc_status
from src.v1.protofiles.report_pb2 import ReportResponse
from src.v1.gateways.response import Response
from src.v1.repositories.tag_repository import TagRepository
from src.v1.repositories.testcase_repository import TestcaseRepository

class ReportService():

    tagRepository: TagRepository
    testcaseRepository: TestcaseRepository

    def __init__(self):
        self.tagRepository = TagRepository()
        self.testcaseRepository = TestcaseRepository()

    def get(self):
        status = rpc_status.OK

        count_total_tags = str(self.tagRepository.total_tag())
        count_total_testcase = str(self.testcaseRepository.total_testcase())
        
        return Response(
            status=status,
            body=ReportResponse(
                total_tags= count_total_tags,
                total_testcases= count_total_testcase
            )
        )