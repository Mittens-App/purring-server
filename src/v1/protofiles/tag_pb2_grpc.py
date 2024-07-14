# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import tag_pb2 as protofiles_dot_tag__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in protofiles/tag_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class TagStub(object):
    """Tag Service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/src.v1.tag.Tag/Create',
                request_serializer=protofiles_dot_tag__pb2.CreateRequest.SerializeToString,
                response_deserializer=protofiles_dot_tag__pb2.CreateResponse.FromString,
                _registered_method=True)
        self.Get = channel.unary_unary(
                '/src.v1.tag.Tag/Get',
                request_serializer=protofiles_dot_tag__pb2.GetRequest.SerializeToString,
                response_deserializer=protofiles_dot_tag__pb2.GetResponse.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/src.v1.tag.Tag/Delete',
                request_serializer=protofiles_dot_tag__pb2.DeleteRequest.SerializeToString,
                response_deserializer=protofiles_dot_tag__pb2.DeleteResponse.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/src.v1.tag.Tag/Update',
                request_serializer=protofiles_dot_tag__pb2.UpdateRequest.SerializeToString,
                response_deserializer=protofiles_dot_tag__pb2.UpdateResponse.FromString,
                _registered_method=True)
        self.DeleteAll = channel.unary_unary(
                '/src.v1.tag.Tag/DeleteAll',
                request_serializer=protofiles_dot_tag__pb2.DeleteAllRequest.SerializeToString,
                response_deserializer=protofiles_dot_tag__pb2.DeleteAllResponse.FromString,
                _registered_method=True)


class TagServicer(object):
    """Tag Service
    """

    def Create(self, request, context):
        """Create new tag
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Return list of tags
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete tags
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Update existing tag
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAll(self, request, context):
        """Delete All tags
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TagServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=protofiles_dot_tag__pb2.CreateRequest.FromString,
                    response_serializer=protofiles_dot_tag__pb2.CreateResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=protofiles_dot_tag__pb2.GetRequest.FromString,
                    response_serializer=protofiles_dot_tag__pb2.GetResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=protofiles_dot_tag__pb2.DeleteRequest.FromString,
                    response_serializer=protofiles_dot_tag__pb2.DeleteResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=protofiles_dot_tag__pb2.UpdateRequest.FromString,
                    response_serializer=protofiles_dot_tag__pb2.UpdateResponse.SerializeToString,
            ),
            'DeleteAll': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAll,
                    request_deserializer=protofiles_dot_tag__pb2.DeleteAllRequest.FromString,
                    response_serializer=protofiles_dot_tag__pb2.DeleteAllResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'src.v1.tag.Tag', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('src.v1.tag.Tag', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Tag(object):
    """Tag Service
    """

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/src.v1.tag.Tag/Create',
            protofiles_dot_tag__pb2.CreateRequest.SerializeToString,
            protofiles_dot_tag__pb2.CreateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/src.v1.tag.Tag/Get',
            protofiles_dot_tag__pb2.GetRequest.SerializeToString,
            protofiles_dot_tag__pb2.GetResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/src.v1.tag.Tag/Delete',
            protofiles_dot_tag__pb2.DeleteRequest.SerializeToString,
            protofiles_dot_tag__pb2.DeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/src.v1.tag.Tag/Update',
            protofiles_dot_tag__pb2.UpdateRequest.SerializeToString,
            protofiles_dot_tag__pb2.UpdateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/src.v1.tag.Tag/DeleteAll',
            protofiles_dot_tag__pb2.DeleteAllRequest.SerializeToString,
            protofiles_dot_tag__pb2.DeleteAllResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
