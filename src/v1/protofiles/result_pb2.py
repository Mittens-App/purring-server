# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protofiles/result.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17protofiles/result.proto\x12\rsrc.v1.result\"J\n\nGetRequest\x12\x0e\n\x06\x66ilter\x18\x01 \x01(\t\x12\x0f\n\x07keyword\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\r\x12\x0c\n\x04page\x18\x04 \x01(\r\"{\n\x0bGetResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12)\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x1b.src.v1.result.DataResponse\x12\x31\n\x08metadata\x18\x03 \x01(\x0b\x32\x1f.src.v1.result.MetaDataResponse\"\xb9\x01\n\x0c\x44\x61taResponse\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0c\x65xecute_date\x18\x03 \x01(\t\x12\x10\n\x08\x64uration\x18\x04 \x01(\x02\x12\x13\n\x0btest_status\x18\x05 \x01(\t\x12\x14\n\x0c\x65\x66\x65\x63tiveness\x18\x06 \x01(\x02\x12\x10\n\x08\x65xecutor\x18\x07 \x01(\t\x12*\n\x07\x44\x61taTag\x18\x08 \x03(\x0b\x32\x19.src.v1.result.DataDetail\")\n\nDataDetail\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x63olor\x18\x03 \x01(\t\"\\\n\x10MetaDataResponse\x12\x14\n\x0c\x63urrent_page\x18\x01 \x01(\r\x12\x10\n\x08per_page\x18\x02 \x01(\r\x12\r\n\x05total\x18\x03 \x01(\r\x12\x11\n\tlast_page\x18\x04 \x01(\r2H\n\x06Result\x12>\n\x03Get\x12\x19.src.v1.result.GetRequest\x1a\x1a.src.v1.result.GetResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protofiles.result_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETREQUEST']._serialized_start=42
  _globals['_GETREQUEST']._serialized_end=116
  _globals['_GETRESPONSE']._serialized_start=118
  _globals['_GETRESPONSE']._serialized_end=241
  _globals['_DATARESPONSE']._serialized_start=244
  _globals['_DATARESPONSE']._serialized_end=429
  _globals['_DATADETAIL']._serialized_start=431
  _globals['_DATADETAIL']._serialized_end=472
  _globals['_METADATARESPONSE']._serialized_start=474
  _globals['_METADATARESPONSE']._serialized_end=566
  _globals['_RESULT']._serialized_start=568
  _globals['_RESULT']._serialized_end=640
# @@protoc_insertion_point(module_scope)
