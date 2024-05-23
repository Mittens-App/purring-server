from grpc import ServicerContext
from src.v1.protofiles.user_pb2 import LoginRequest, LoginResponse, PingRequest, PingResponse
from src.v1.protofiles.user_pb2_grpc import UserServicer
from src.v1.services.user_service import UserService
from src.v1.protofiles.testcase_pb2 import GetRequest as TestcaseGetReq, CreateRequest as TestcaseCreateReq, RunRequest as TestcaseRunReq, UpdateRequest as TestcaseUpdateReq, DeleteRequest as TestcaseDeleteReq, ViewRequest as TestcaseViewReq
from src.v1.protofiles.testcase_pb2_grpc import TestcaseServicer
from src.v1.services.testcase_service import TestcaseService
from src.v1.protofiles.tag_pb2_grpc import TagServicer
from src.v1.protofiles.tag_pb2 import GetRequest as TagGetReq, CreateRequest as TagCreateReq, UpdateRequest as TagUpdateReq, DeleteRequest as TagDeleteReq
from src.v1.services.tag_service import TagService

class User(UserServicer):
    """implement user.proto
    """

    userService: UserService

    def __init__(self):
        super().__init__()
        self.userService = UserService()


    def Login(self, request: LoginRequest, context: ServicerContext):
        result = self.userService.login(
            username=request.username,
            password=request.password
        )
        context.set_code(result.status)
        return LoginResponse(
            username=result.body['username'],
            status=str(result.status),
            token=result.body['token']
        )
    
    def Ping(self, request: PingRequest, context: ServicerContext):
        return PingResponse(
            status="OK"
        )

class Testcase(TestcaseServicer):
    """implement testcase.proto
    """
    
    testcaseService: TestcaseService

    def __init__(self):
        super().__init__()
        self.testcaseService = TestcaseService()

    def Create(self, request: TestcaseCreateReq, context: ServicerContext):
        result = self.testcaseService.create(
            payload = request, creator = context.myToken["username"]
        )
        
        context.set_code(result.status)
        return result.body

    def Get(self, request: TestcaseGetReq, context: ServicerContext):
        result = self.testcaseService.get(
            filter = request.filter,
            keyword = request.keyword,
            limit = request.limit,
            page = request.page
        )

        context.set_code(result.status)

        return result.body
    
    def Run(self, request: TestcaseRunReq, context: ServicerContext):
        result = self.testcaseService.runAsync(
            id=request.id, executor=context.myToken["username"]
        )
        context.set_code(result.status)
        return result.body

    def Update(self, request: TestcaseUpdateReq, context: ServicerContext):
        result = self.testcaseService.update(request)
        context.set_code(result.status)
        return result.body

    def Delete(self, request: TestcaseDeleteReq, context: ServicerContext):
        result = self.testcaseService.delete(request.id)
        context.set_code(result.status)
        return result.body
    
    def View(self, request: TestcaseViewReq, context: ServicerContext):
        result = self.testcaseService.view(request.path)
        context.set_code(result.status)
        return result.body

class Tag(TagServicer):
    """implement tag.proto
    """

    tagService: TagService

    def __init__(self):
        super().__init__()
        self.tagService = TagService()
    
    def Create(self, request: TagCreateReq, context: ServicerContext):
        result = self.tagService.create(request)
        context.set_code(result.status)
        return result.body
    
    def Get(self, request: TagGetReq, context: ServicerContext):
        result = self.tagService.get(request.keyword)
        context.set_code(result.status)
        return result.body
    
    def Update(self, request: TagUpdateReq, context: ServicerContext):
        result = self.tagService.update(request)
        context.set_code(result.status)
        return result.body
    
    def Delete(self, request: TagDeleteReq, context: ServicerContext):
        result = self.tagService.delete(request.id)
        context.set_code(result.status)
        return result.body