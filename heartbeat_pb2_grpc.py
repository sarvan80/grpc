# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import heartbeat_pb2 as heartbeat__pb2


class HeartBeatStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Beats = channel.unary_stream(
                '/heartbeat.HeartBeat/Beats',
                request_serializer=heartbeat__pb2.Counter.SerializeToString,
                response_deserializer=heartbeat__pb2.Counter.FromString,
                )


class HeartBeatServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Beats(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HeartBeatServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Beats': grpc.unary_stream_rpc_method_handler(
                    servicer.Beats,
                    request_deserializer=heartbeat__pb2.Counter.FromString,
                    response_serializer=heartbeat__pb2.Counter.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'heartbeat.HeartBeat', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HeartBeat(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Beats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/heartbeat.HeartBeat/Beats',
            heartbeat__pb2.Counter.SerializeToString,
            heartbeat__pb2.Counter.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
