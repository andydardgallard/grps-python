# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crud.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ncrud.proto\x12\x03\x61pi\"3\n\ngetRequest\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"2\n\x0bgetResponse\x12\x13\n\x0b\x63onfig_body\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\t\":\n\rcreateRequest\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x13\n\x0b\x63onfig_body\x18\x02 \x01(\t\"!\n\x0e\x63reateResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\"K\n\rupdateRequest\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x13\n\x0b\x63onfig_body\x18\x03 \x01(\t\" \n\x0eupdateResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"6\n\rdeleteRequest\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\" \n\x0e\x64\x65leteResponse\x12\x0e\n\x06result\x18\x01 \x01(\t2\xf1\x01\n\x0c\x43onfigMngmnt\x12\x30\n\tGetConfig\x12\x0f.api.getRequest\x1a\x10.api.getResponse\"\x00\x12\x39\n\x0c\x43reateConfig\x12\x12.api.createRequest\x1a\x13.api.createResponse\"\x00\x12\x39\n\x0cUpdateConfig\x12\x12.api.updateRequest\x1a\x13.api.updateResponse\"\x00\x12\x39\n\x0c\x44\x65leteConfig\x12\x12.api.deleteRequest\x1a\x13.api.deleteResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'crud_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETREQUEST._serialized_start=19
  _GETREQUEST._serialized_end=70
  _GETRESPONSE._serialized_start=72
  _GETRESPONSE._serialized_end=122
  _CREATEREQUEST._serialized_start=124
  _CREATEREQUEST._serialized_end=182
  _CREATERESPONSE._serialized_start=184
  _CREATERESPONSE._serialized_end=217
  _UPDATEREQUEST._serialized_start=219
  _UPDATEREQUEST._serialized_end=294
  _UPDATERESPONSE._serialized_start=296
  _UPDATERESPONSE._serialized_end=328
  _DELETEREQUEST._serialized_start=330
  _DELETEREQUEST._serialized_end=384
  _DELETERESPONSE._serialized_start=386
  _DELETERESPONSE._serialized_end=418
  _CONFIGMNGMNT._serialized_start=421
  _CONFIGMNGMNT._serialized_end=662
# @@protoc_insertion_point(module_scope)