# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: data_service.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'data_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x64\x61ta_service.proto\x12\x0c\x46\x65\x61tureForge\"M\n\x0b\x44\x61taPayload\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tdata_type\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\",\n\x08Response\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2P\n\rDataIngestion\x12?\n\x08SendData\x12\x19.FeatureForge.DataPayload\x1a\x16.FeatureForge.Response\"\x00\x42\'Z%github.com/carpx05/FeatureForge/protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'data_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z%github.com/carpx05/FeatureForge/proto'
  _globals['_DATAPAYLOAD']._serialized_start=36
  _globals['_DATAPAYLOAD']._serialized_end=113
  _globals['_RESPONSE']._serialized_start=115
  _globals['_RESPONSE']._serialized_end=159
  _globals['_DATAINGESTION']._serialized_start=161
  _globals['_DATAINGESTION']._serialized_end=241
# @@protoc_insertion_point(module_scope)