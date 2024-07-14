from grpc import StatusCode as rpc_status
from src.v1.gateways.response import Response
from src.v1.protofiles.result_pb2 import GetResponse, DataResponse, MetaDataResponse, DetailResponse, ResultDetail, DeleteAllResponse
from src.v1.repositories.result_repository import ResultRepository
import math
from sqlalchemy.exc import SQLAlchemyError

class ResultService():

    resultRepository: ResultRepository

    def __init__(self):
        self.resultRepository = ResultRepository()

    def get(self, filter = None, keyword = None, limit = 10, page = 1):
        
        offset = page - 1        
        if page <= 1:
            page=1
            offset = 0

        filter = filter.casefold()

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
    
    def detail(self, id):
        status = rpc_status.OK
        response = DetailResponse(
            status=str(status),
        )

        data_query = self.resultRepository.get_detail(id)

        tag_data = []
        for tag in data_query.tags:
            tag_data.append({
                'name': tag.tag_name,
                'color': tag.tag_color
            })

        data_message = []
        for failed in data_query.messages:
            data_message.append({
                'type': failed.result_type,
                'method': failed.result_method,
                'message': failed.message
            })

        response.DataById.append(
            ResultDetail(
                id=data_query.id,
                name=data_query.name,
                test_count=data_query.test_count,
                duration=round(float(data_query.duration), 2),
                test_status=str(data_query.test_status).split('.')[-1],
                efectiveness=round(float(data_query.effectiveness), 2),
                executor=data_query.executor,
                DataTag=tag_data,
                fail_message=data_message
            )
        )

        return Response(
            body=response,
            status=rpc_status.OK
        )
    
    def delete_all(self):
        status = rpc_status.OK
        rpc_response = DeleteAllResponse(
            message="Success",
            status=str(rpc_status.OK)
        )

        try:
            self.resultRepository.delete_all()
            self.resultRepository.commit()
        except SQLAlchemyError as err:
            self.resultRepository.rollback()
            rpc_response.message = str(err.__dict__)
            status = rpc_status.INTERNAL

        return Response(
            body= rpc_response,
            status= status
        )
