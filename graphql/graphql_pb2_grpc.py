# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from graphql import graphql_pb2 as graphql_dot_graphql__pb2


class GraphQLStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Execute = channel.unary_stream(
            "/dfuse.graphql.v1.GraphQL/Execute",
            request_serializer=graphql_dot_graphql__pb2.Request.SerializeToString,
            response_deserializer=graphql_dot_graphql__pb2.Response.FromString,
        )


class GraphQLServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Execute(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_GraphQLServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Execute": grpc.unary_stream_rpc_method_handler(
            servicer.Execute,
            request_deserializer=graphql_dot_graphql__pb2.Request.FromString,
            response_serializer=graphql_dot_graphql__pb2.Response.SerializeToString,
        )
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "dfuse.graphql.v1.GraphQL", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class GraphQL(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Execute(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/dfuse.graphql.v1.GraphQL/Execute",
            graphql_dot_graphql__pb2.Request.SerializeToString,
            graphql_dot_graphql__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
