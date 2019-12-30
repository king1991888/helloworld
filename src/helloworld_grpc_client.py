# coding=utf-8


import grpc

import helloworld_pb2_grpc, helloworld_pb2


def run():
    channel=grpc.insecure_channel("192.168.189.129:50051")
    stub=helloworld_pb2_grpc.GreeterStub(channel)
    response=stub.SayHello(helloworld_pb2.HelloRequest(name="我来拉",flag=True))
    print(response.message)


if __name__ == '__main__':
    run()
