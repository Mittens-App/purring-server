from grpc import StatusCode as rpc_status
from src.v1.protofiles.report_pb2 import ReportResponse
from src.v1.gateways.response import Response
from src.v1.repositories.tag_repository import TagRepository
from src.v1.repositories.testcase_repository import TestcaseRepository
from src.v1.repositories.result_repository import ResultRepository
from datetime import datetime

class ReportService():

    tagRepository: TagRepository
    testcaseRepository: TestcaseRepository
    resultRepository: ResultRepository
    now = datetime.now()

    def __init__(self):
        self.tagRepository = TagRepository()
        self.testcaseRepository = TestcaseRepository()
        self.resultRepository = ResultRepository()

    def get(self):
        status = rpc_status.OK

        current_date = self.now.strftime('%Y-%m-%d %H:%M:%S')
        first_day_month = datetime(self.now.year, self.now.month, 1, 0, 0, 0)

        count_total_tags = self.tagRepository.total_tag()
        count_total_testcase = self.testcaseRepository.total_testcase()
        total_efectiveness = float(self.resultRepository.totalEfectiveness())
        lists = self.resultRepository.reportGetlist(first_day_month, current_date)
        tag_list = self.resultRepository.tag_report_list(first_day_month, current_date)

        mapped_list = []
        for item in tag_list:
            mapped_list.append({
                'id': item[0],
                'name': item[1],
                'total': item[2],
                'failed': item[3]
            })

        for item in mapped_list:
            total = item['total']
            failed = item['failed']
            efectiveness = ((total - failed)/total)*100
            item['efectiveness'] = efectiveness
            item.pop('failed')

        data_report = []
        for list_item in lists:
            report_data = {
                'id': list_item.id,
                'date': str(list_item.execute_date),
                'name': list_item.name,
                'status': str(list_item.test_status).split('.')[-1],
                'executor': list_item.executor
            }
            data_report.append(report_data)

        response = ReportResponse(
            current_month=self.now.month,
            current_month_string=self.now.strftime("%B"),
            current_year=self.now.year,
            total_tags= count_total_tags,
            total_testcases= count_total_testcase,
            total_efectiveness= total_efectiveness,
            ResultData= data_report,
            TagData= mapped_list,
            status=str(status)
        )

        return Response(
            status=status,
            body=response
        )