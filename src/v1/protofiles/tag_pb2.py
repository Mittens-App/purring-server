# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protofiles/tag.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14protofiles/tag.proto\x12\nsrc.v1.tag\":\n\rCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12\r\n\x05\x63olor\x18\x03 \x01(\t\"1\n\x0e\x43reateResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1d\n\nGetRequest\x12\x0f\n\x07keyword\x18\x01 \x01(\t\"E\n\x0bGetResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12&\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x18.src.v1.tag.DataResponse\"E\n\x0c\x44\x61taResponse\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12\r\n\x05\x63olor\x18\x04 \x01(\t\"\x1b\n\rDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\r\"1\n\x0e\x44\x65leteResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"F\n\rUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12\r\n\x05\x63olor\x18\x04 \x01(\t\"1\n\x0eUpdateResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x12\n\x10\x44\x65leteAllRequest\"4\n\x11\x44\x65leteAllResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t2\xd4\x02\n\x03Tag\x12\x41\n\x06\x43reate\x12\x19.src.v1.tag.CreateRequest\x1a\x1a.src.v1.tag.CreateResponse\"\x00\x12\x38\n\x03Get\x12\x16.src.v1.tag.GetRequest\x1a\x17.src.v1.tag.GetResponse\"\x00\x12\x41\n\x06\x44\x65lete\x12\x19.src.v1.tag.DeleteRequest\x1a\x1a.src.v1.tag.DeleteResponse\"\x00\x12\x41\n\x06Update\x12\x19.src.v1.tag.UpdateRequest\x1a\x1a.src.v1.tag.UpdateResponse\"\x00\x12J\n\tDeleteAll\x12\x1c.src.v1.tag.DeleteAllRequest\x1a\x1d.src.v1.tag.DeleteAllResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protofiles.tag_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CREATEREQUEST']._serialized_start=36
  _globals['_CREATEREQUEST']._serialized_end=94
  _globals['_CREATERESPONSE']._serialized_start=96
  _globals['_CREATERESPONSE']._serialized_end=145
  _globals['_GETREQUEST']._serialized_start=147
  _globals['_GETREQUEST']._serialized_end=176
  _globals['_GETRESPONSE']._serialized_start=178
  _globals['_GETRESPONSE']._serialized_end=247
  _globals['_DATARESPONSE']._serialized_start=249
  _globals['_DATARESPONSE']._serialized_end=318
  _globals['_DELETEREQUEST']._serialized_start=320
  _globals['_DELETEREQUEST']._serialized_end=347
  _globals['_DELETERESPONSE']._serialized_start=349
  _globals['_DELETERESPONSE']._serialized_end=398
  _globals['_UPDATEREQUEST']._serialized_start=400
  _globals['_UPDATEREQUEST']._serialized_end=470
  _globals['_UPDATERESPONSE']._serialized_start=472
  _globals['_UPDATERESPONSE']._serialized_end=521
  _globals['_DELETEALLREQUEST']._serialized_start=523
  _globals['_DELETEALLREQUEST']._serialized_end=541
  _globals['_DELETEALLRESPONSE']._serialized_start=543
  _globals['_DELETEALLRESPONSE']._serialized_end=595
  _globals['_TAG']._serialized_start=598
  _globals['_TAG']._serialized_end=938
# @@protoc_insertion_point(module_scope)
