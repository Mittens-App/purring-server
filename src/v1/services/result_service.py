from grpc import StatusCode as rpc_status
from src.v1.gateways.response import Response
from src.v1.protofiles.result_pb2 import GetResponse, DataResponse, MetaDataResponse
from src.v1.repositories.result_repository import ResultRepository
import math

class ResultService():

    resultRepository: ResultRepository

    def __init__(self):
        self.resultRepository = ResultRepository()

    def get(self, filter = None, keyword = None, limit = 10, page = 1):
        
        offset = page - 1        
        if page <= 1:
            page=1
            offset = 0

        data = self.resultRepository.get(
            filter=filter,
            keyword=keyword,
            limit=limit,
            offset=offset
        )

        total_count = data["total_count"]
        results = data["data"]
        last_page = 1
        if total_count > 0:
            last_page = math.ceil(total_count / limit)

        rpc_response = GetResponse(
            metadata=MetaDataResponse(
                total=total_count,
                current_page=page,
                last_page=last_page,
                per_page=limit
            )
        )

        for result in results:
            tags_data = []
            for tag in result.tags:
                tags_data.append({
                    'name': tag.tag_name,
                    'color': tag.tag_color
                })

            rpc_response.data.append(
                DataResponse(
                    id=result.id,
                    name=result.name,
                    execute_date=str(result.execute_date),
                    duration= round(float(result.duration), 2),
                    test_status=str(result.test_status).split('.')[-1],
                    efectiveness=round(float(result.effectiveness), 2),
                    executor=result.executor,
                    DataTag=tags_data
                )
            )

        rpc_response.status = str(rpc_status.OK)
        
        return Response(
            body=rpc_response,
            status=rpc_status.OK
        )