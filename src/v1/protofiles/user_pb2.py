# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protofiles/user.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15protofiles/user.proto\x12\x0bsrc.v1.user\"2\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"@\n\rLoginResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\"\r\n\x0bPingRequest\"\x1e\n\x0cPingResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2\x87\x01\n\x04User\x12@\n\x05Login\x12\x19.src.v1.user.LoginRequest\x1a\x1a.src.v1.user.LoginResponse\"\x00\x12=\n\x04Ping\x12\x18.src.v1.user.PingRequest\x1a\x19.src.v1.user.PingResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protofiles.user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_LOGINREQUEST']._serialized_start=38
  _globals['_LOGINREQUEST']._serialized_end=88
  _globals['_LOGINRESPONSE']._serialized_start=90
  _globals['_LOGINRESPONSE']._serialized_end=154
  _globals['_PINGREQUEST']._serialized_start=156
  _globals['_PINGREQUEST']._serialized_end=169
  _globals['_PINGRESPONSE']._serialized_start=171
  _globals['_PINGRESPONSE']._serialized_end=201
  _globals['_USER']._serialized_start=204
  _globals['_USER']._serialized_end=339
# @@protoc_insertion_point(module_scope)
