# coding=utf-8

from concurrent import futures
import time
import grpc
import os
from log import Log
logger = Log(__name__).getlog()

import helloworld_pb2_grpc, helloworld_pb2



class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self,request,context):
        logger.info("打印日志")
        print(request.flag)
        print(request.input)
        return helloworld_pb2.HelloReply(message="python返回值")

def service():
    logger.info('准备启动grpc服务')
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(),server)
    logger.info(os.environ.get('port'))
    if os.environ.get('port') is None:
        server.add_insecure_port('[::]:50051')
    else:
        server.add_insecure_port(os.environ.get('port'))
    server.start()
    logger.info('grpc服务启动完毕')
    try:
        while True:
            time.sleep(60*60*24)   #
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    service()
