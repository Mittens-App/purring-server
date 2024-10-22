# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protofiles/testcase.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19protofiles/testcase.proto\x12\x0fsrc.v1.testcase\"J\n\nGetRequest\x12\x0e\n\x06\x66ilter\x18\x01 \x01(\t\x12\x0f\n\x07keyword\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\r\x12\x0c\n\x04page\x18\x04 \x01(\r\"\x7f\n\x0bGetResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12+\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x1d.src.v1.testcase.DataResponse\x12\x33\n\x08metadata\x18\x03 \x01(\x0b\x32!.src.v1.testcase.MetaDataResponse\"\\\n\x10MetaDataResponse\x12\x14\n\x0c\x63urrent_page\x18\x01 \x01(\r\x12\x10\n\x08per_page\x18\x02 \x01(\r\x12\r\n\x05total\x18\x03 \x01(\r\x12\x11\n\tlast_page\x18\x04 \x01(\r\"\xb1\x01\n\x0c\x44\x61taResponse\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12\x0c\n\x04\x66ile\x18\x04 \x01(\t\x12\"\n\x04tags\x18\x05 \x03(\x0b\x32\x14.src.v1.testcase.Tag\x12\x0f\n\x07\x63reator\x18\x06 \x01(\t\x12\x19\n\x11last_execute_date\x18\x07 \x01(\t\x12\x1b\n\x13last_execute_result\x18\x08 \x01(\t\"\"\n\x03Tag\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x63olor\x18\x02 \x01(\t\"J\n\rCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12\x0c\n\x04\x66ile\x18\x03 \x01(\t\x12\x0f\n\x07tag_ids\x18\x04 \x03(\r\"1\n\x0e\x43reateResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"V\n\rUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12\x0c\n\x04\x66ile\x18\x04 \x01(\t\x12\x0f\n\x07tag_ids\x18\x05 \x03(\r\"1\n\x0eUpdateResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1b\n\rDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\r\"1\n\x0e\x44\x65leteResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x18\n\nRunRequest\x12\n\n\x02id\x18\x01 \x01(\r\".\n\x0bRunResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1b\n\x0bViewRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\"\x81\x01\n\x0cViewResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x11\n\tclassname\x18\x03 \x01(\t\x12\x0c\n\x04path\x18\x04 \x01(\t\x12/\n\tfunctions\x18\x05 \x03(\x0b\x32\x1c.src.v1.testcase.DefFunction\",\n\x0b\x44\x65\x66\x46unction\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\"\x12\n\x10\x44\x65leteAllRequest\"4\n\x11\x44\x65leteAllResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t2\x96\x04\n\x08Testcase\x12\x42\n\x03Get\x12\x1b.src.v1.testcase.GetRequest\x1a\x1c.src.v1.testcase.GetResponse\"\x00\x12K\n\x06\x43reate\x12\x1e.src.v1.testcase.CreateRequest\x1a\x1f.src.v1.testcase.CreateResponse\"\x00\x12K\n\x06Update\x12\x1e.src.v1.testcase.UpdateRequest\x1a\x1f.src.v1.testcase.UpdateResponse\"\x00\x12K\n\x06\x44\x65lete\x12\x1e.src.v1.testcase.DeleteRequest\x1a\x1f.src.v1.testcase.DeleteResponse\"\x00\x12\x42\n\x03Run\x12\x1b.src.v1.testcase.RunRequest\x1a\x1c.src.v1.testcase.RunResponse\"\x00\x12\x45\n\x04View\x12\x1c.src.v1.testcase.ViewRequest\x1a\x1d.src.v1.testcase.ViewResponse\"\x00\x12T\n\tDeleteAll\x12!.src.v1.testcase.DeleteAllRequest\x1a\".src.v1.testcase.DeleteAllResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protofiles.testcase_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETREQUEST']._serialized_start=46
  _globals['_GETREQUEST']._serialized_end=120
  _globals['_GETRESPONSE']._serialized_start=122
  _globals['_GETRESPONSE']._serialized_end=249
  _globals['_METADATARESPONSE']._serialized_start=251
  _globals['_METADATARESPONSE']._serialized_end=343
  _globals['_DATARESPONSE']._serialized_start=346
  _globals['_DATARESPONSE']._serialized_end=523
  _globals['_TAG']._serialized_start=525
  _globals['_TAG']._serialized_end=559
  _globals['_CREATEREQUEST']._serialized_start=561
  _globals['_CREATEREQUEST']._serialized_end=635
  _globals['_CREATERESPONSE']._serialized_start=637
  _globals['_CREATERESPONSE']._serialized_end=686
  _globals['_UPDATEREQUEST']._serialized_start=688
  _globals['_UPDATEREQUEST']._serialized_end=774
  _globals['_UPDATERESPONSE']._serialized_start=776
  _globals['_UPDATERESPONSE']._serialized_end=825
  _globals['_DELETEREQUEST']._serialized_start=827
  _globals['_DELETEREQUEST']._serialized_end=854
  _globals['_DELETERESPONSE']._serialized_start=856
  _globals['_DELETERESPONSE']._serialized_end=905
  _globals['_RUNREQUEST']._serialized_start=907
  _globals['_RUNREQUEST']._serialized_end=931
  _globals['_RUNRESPONSE']._serialized_start=933
  _globals['_RUNRESPONSE']._serialized_end=979
  _globals['_VIEWREQUEST']._serialized_start=981
  _globals['_VIEWREQUEST']._serialized_end=1008
  _globals['_VIEWRESPONSE']._serialized_start=1011
  _globals['_VIEWRESPONSE']._serialized_end=1140
  _globals['_DEFFUNCTION']._serialized_start=1142
  _globals['_DEFFUNCTION']._serialized_end=1186
  _globals['_DELETEALLREQUEST']._serialized_start=1188
  _globals['_DELETEALLREQUEST']._serialized_end=1206
  _globals['_DELETEALLRESPONSE']._serialized_start=1208
  _globals['_DELETEALLRESPONSE']._serialized_end=1260
  _globals['_TESTCASE']._serialized_start=1263
  _globals['_TESTCASE']._serialized_end=1797
# @@protoc_insertion_point(module_scope)
