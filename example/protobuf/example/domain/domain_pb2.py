# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example/protobuf/example/domain/domain.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,example/protobuf/example/domain/domain.proto\x12\x0e\x65xample.domain\"\x1d\n\x08JoeState\x12\x11\n\tlanguages\x18\x01 \x03(\t\"\x1b\n\x07Request\x12\x10\n\x08language\x18\x01 \x01(\t\"\x19\n\x05Reply\x12\x10\n\x08response\x18\x01 \x01(\tB:\n\"eigr.functions.spawn.example.stateB\x12JoeStateStateProtoP\x01\x62\x06proto3')



_JOESTATE = DESCRIPTOR.message_types_by_name['JoeState']
_REQUEST = DESCRIPTOR.message_types_by_name['Request']
_REPLY = DESCRIPTOR.message_types_by_name['Reply']
JoeState = _reflection.GeneratedProtocolMessageType('JoeState', (_message.Message,), {
  'DESCRIPTOR' : _JOESTATE,
  '__module__' : 'example.protobuf.example.domain.domain_pb2'
  # @@protoc_insertion_point(class_scope:example.domain.JoeState)
  })
_sym_db.RegisterMessage(JoeState)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'example.protobuf.example.domain.domain_pb2'
  # @@protoc_insertion_point(class_scope:example.domain.Request)
  })
_sym_db.RegisterMessage(Request)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), {
  'DESCRIPTOR' : _REPLY,
  '__module__' : 'example.protobuf.example.domain.domain_pb2'
  # @@protoc_insertion_point(class_scope:example.domain.Reply)
  })
_sym_db.RegisterMessage(Reply)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"eigr.functions.spawn.example.stateB\022JoeStateStateProtoP\001'
  _JOESTATE._serialized_start=64
  _JOESTATE._serialized_end=93
  _REQUEST._serialized_start=95
  _REQUEST._serialized_end=122
  _REPLY._serialized_start=124
  _REPLY._serialized_end=149
# @@protoc_insertion_point(module_scope)