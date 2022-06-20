import grpc
from concurrent import futures
import time
import hello_pb2_grpc as pb2_grpc
import hello_pb2 as pb2


class HelloService(pb2_grpc.HelloServiceServicer):

    def __init__(self, *args, **kwargs):
        pass


    def sayHello(self, request, context):
        return pb2.HelloResp(Result="Hello {}!".format(request.Name))


    # def sayHelloStrict(self, request, context):
    #     """Only responds when Name is less than 10 Characters
    #     """
    #     context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    #     context.set_details('Method not implemented!')
    #     raise NotImplementedError('Method not implemented!')

    def sayHelloStrict(self, request, context):
       if len(request.Name) >= 1:
           msg = 'Length of Name must be more than 10 characters'
           context.set_code(grpc.StatusCode.FAILED_PRECONDITION)
           context.set_details(msg)
           return pb2.HelloResp()
       return pb2.HelloResp(Result = "Hello {}!".format(request.Name))



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_HelloServiceServicer_to_server(HelloService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
