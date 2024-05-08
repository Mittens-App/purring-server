from grpc_interceptor import ServerInterceptor
from grpc_interceptor.exceptions import GrpcException, Unauthenticated
from grpc import ServicerContext, StatusCode as rpc_status
from src.v1.services.auth import JwtGenerator
from datetime import datetime

class AuthInterceptor(ServerInterceptor):
    __LOGIN_METHOD: str
    __AUTH_KEY: str

    def __init__(self) -> None:
        super().__init__()
        self.__LOGIN_METHOD = "/src.v1.user.User/Login"
        self.__AUTH_KEY = "authorization"

    def intercept(
        self,
        method,
        request_or_iterator,
        context: ServicerContext,
        method_name: str,
    ):
        metadata = context.invocation_metadata()

        # login whitelist
        if (method_name == self.__LOGIN_METHOD):
            return method(request_or_iterator, context)
        
        getToken = self.__get_token(metadata=metadata, context=context)

        if getToken["status"] is False:
            context.set_code(rpc_status.UNAUTHENTICATED)
            context.set_details("Bye.")
            raise Unauthenticated("UNAUTHENTICATED", rpc_status.UNAUTHENTICATED)
        
        context.myToken = getToken["data"]

        return method(request_or_iterator, context)

    def __get_token(self, metadata, context: ServicerContext):
        result = {
            "status": False,
            "data": None
        }
        found = False
        value = ""
        for data in metadata:
            if data.key == self.__AUTH_KEY:
                found = True
                value = data.value
                break
        
        if found is False:
            return result
        
        generator = JwtGenerator()
        token = generator.decode(value)
        
        if token['expr'] < datetime.now().timestamp():
            return result
        
        result["status"] = found
        result["data"] = token

        return result