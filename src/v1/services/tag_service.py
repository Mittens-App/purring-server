from grpc import StatusCode as rpc_status
from sqlalchemy.exc import SQLAlchemyError
from src.v1.repositories.tag_repository import TagRepository
from src.v1.models.tag import Tag
from src.v1.protofiles.tag_pb2 import CreateResponse, GetResponse, DataResponse, UpdateResponse, DeleteAllResponse
from src.v1.gateways.response import Response
from src.v1.repositories.testcase_repository import TestcaseRepository

class TagService:
    tagRepo: TagRepository
    testcaseRepo: TestcaseRepository
    
    def __init__(self):
        self.tagRepo = TagRepository()
        self.testcaseRepo = TestcaseRepository()
    
    def create(self, payload):
        tag = Tag()
        tag.name = payload.name
        tag.description = payload.desc
        tag.color = payload.color

        status = rpc_status.OK
        rpc_response = CreateResponse(
            message="success",
        )

        try:
            self.tagRepo.create(tag)
            self.tagRepo.commit()
        except SQLAlchemyError as e:
            error = str(e.__dict__)
            self.tagRepo.rollback()
            rpc_response.message = error
            status = rpc_status.INTERNAL

        rpc_response.status= str(status)

        return Response(
            body=rpc_response,
            status=status
        )

    def get(self, keyword):
        status = rpc_status.OK
        rpc_response = GetResponse(
            status=str(status),
        )
        
        tags = self.tagRepo.get(keyword)

        for tag in tags:
            rpc_response.data.append(
                DataResponse(
                    id=tag.id,
                    name=tag.name,
                    desc=tag.description,
                    color=tag.color
                )
            )

        return Response(
            body=rpc_response,
            status=status
        )

    def update(self, payload):
        tag: Tag = self.tagRepo.get_by_id(payload.id)

        if tag is None:
            return Response(
                body=UpdateResponse(
                    message="failed",
                    status=str(rpc_status.NOT_FOUND)
                ),
                status=rpc_status.NOT_FOUND
            )
        
        status = rpc_status.OK
        rpc_response = UpdateResponse(
            message="success",
        )
        tag.name = payload.name
        tag.description = payload.desc
        tag.color = payload.color

        try:
            self.tagRepo.commit()
        except SQLAlchemyError as e:
            error = str(e.__dict__)
            self.tagRepo.rollback()
            rpc_response.message = error
            status = rpc_status.INTERNAL
        
        rpc_response.status= str(status)

        return Response(
            body=rpc_response,
            status=status
        )

    def delete(self, id):
        tag: Tag = self.tagRepo.get_by_id(id)

        if tag is None:
            return Response(
                body=UpdateResponse(
                    message="failed",
                    status=str(rpc_status.NOT_FOUND)
                ),
                status=rpc_status.NOT_FOUND
            )
        
        status = rpc_status.OK
        rpc_response = UpdateResponse(
            message="success",
        )
        try:
            self.tagRepo.delete_by_id(id)
            self.tagRepo.commit()
        except SQLAlchemyError as e:
            error = str(e.__dict__)
            self.tagRepo.rollback()
            rpc_response.message = error
            status = rpc_status.INTERNAL

        rpc_response.status= str(status)

        return Response(
            body=rpc_response,
            status=status
        )
    
    def delete_all(self):
        status = rpc_status.OK
        response = DeleteAllResponse(
            message="Success",
            status=str(status)
        )

        try:
            self.tagRepo.delete_all()
        except SQLAlchemyError as err:
            self.tagRepo.rollback()
            message = str(err.__dict__)
            status = rpc_status.INTERNAL

        return Response(
            body= response,
            status= status
        )