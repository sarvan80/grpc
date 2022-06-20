from itertools import count
import grpc
from concurrent import futures
import time
import heartbeat_pb2_grpc as pb2_grpc
import heartbeat_pb2 as pb2


class HeartBeatService(pb2_grpc.HeartBeatServicer):

    def __init__(self, *args, **kwargs):
        pass

    def Beats(self, request, context):
        print("Beats: {}".format(request.count))

        def response():
            i = 0;
            while context.is_active():
                print("Streaming {}".format(i))
                result = pb2.Counter(count=i)
                i += 1
                time.sleep(1)
                yield result

        return response()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_HeartBeatServicer_to_server(HeartBeatService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()