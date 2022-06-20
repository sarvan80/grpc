from __future__ import print_function
import grpc
from concurrent import futures
import time
import heartbeat_pb2_grpc as pb2_grpc
import heartbeat_pb2 as pb2


def getBeats(stub):
    try:
        result_it = stub.Beats(pb2.Counter(count=0))
        for result in result_it:
            print("count :{}".format(result.count))
            if result.count >= 5:
                result_it.cancel()
    except grpc.RpcError as rpc_error:
        if rpc_error.code() == grpc.StatusCode.CANCELLED:
            print("Cancelled: " + rpc_error.details())


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb2_grpc.HeartBeatStub(channel)
        getBeats(stub)


if __name__ == '__main__':
    run()