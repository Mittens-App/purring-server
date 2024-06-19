import grpc
from concurrent import futures
from fastapi import FastAPI
from src.v1.gateways.http import AppRoute
from config.database import init_db
from config.loader import ConfigLoad as cfg

app = FastAPI(
    docs_url=None,
    redoc_url=None,
)
# register http route
app.include_router(AppRoute)

# register grpc
from src.v1.gateways.rpc_auth import AuthInterceptor
server = grpc.server(
    futures.ThreadPoolExecutor(max_workers=cfg['grpc']['worker']),
    interceptors=(AuthInterceptor(),)
)
# start server
def serve():
    # start grpc server
    server.add_insecure_port(":".join(["[::]", str(cfg['grpc']['port'])]))
    server.start()
    server.wait_for_termination(True)
    print("".join(["Server started. Listening on port ", str(cfg['grpc']['port'])]))

    # start http server
    import uvicorn
    if cfg['env'] == 'PRODUCTION':
        uvicorn.run(app='main:app', host=cfg['http']['host'], port=cfg['http']['port'], workers=cfg['http']['worker'])
    else:
        uvicorn.run(app='main:app', host=cfg['http']['host'], port=cfg['http']['port'], reload=True)


# add protobuff per service
import src.v1.protofiles.user_pb2_grpc as user_pb2_grpc
import src.v1.protofiles.testcase_pb2_grpc as testcase_pb2_grpc
import src.v1.protofiles.tag_pb2_grpc as tag_pb2_grpc
import src.v1.protofiles.report_pb2_grpc as report_pb2_grpc
from src.v1.gateways.rpc import User, Testcase, Tag, Report

user_pb2_grpc.add_UserServicer_to_server(User(), server)
testcase_pb2_grpc.add_TestcaseServicer_to_server(Testcase(), server)
tag_pb2_grpc.add_TagServicer_to_server(Tag(), server)
report_pb2_grpc.add_ReportServicer_to_server(Report(), server)


# init db model
init_db()

if __name__ == '__main__':
    serve()