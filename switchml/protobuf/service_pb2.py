# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/service.proto',
  package='switchml',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16protobuf/service.proto\x12\x08switchml\"2\n\nParameters\x12\x0f\n\x07tensors\x18\x01 \x03(\x0c\x12\x13\n\x0btensor_type\x18\x02 \x01(\t\"\xa8\x01\n\x06\x46itRes\x12(\n\nparameters\x18\x02 \x01(\x0b\x32\x14.switchml.Parameters\x12\x14\n\x0cnum_examples\x18\x03 \x01(\x03\x12.\n\x07metrics\x18\x04 \x03(\x0b\x32\x1d.switchml.FitRes.MetricsEntry\x1a.\n\x0cMetricsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\"\x8e\x01\n\x07\x45valRes\x12\x0c\n\x04loss\x18\x01 \x01(\x02\x12\x14\n\x0cnum_examples\x18\x02 \x01(\x03\x12/\n\x07metrics\x18\x03 \x03(\x0b\x32\x1e.switchml.EvalRes.MetricsEntry\x1a.\n\x0cMetricsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\"[\n\x11WeightsInvocation\x12!\n\x07\x66it_res\x18\x01 \x01(\x0b\x32\x10.switchml.FitRes\x12#\n\x08\x65val_res\x18\x02 \x01(\x0b\x32\x11.switchml.EvalRes\"\xa1\x01\n\x0fWeightsResponse\x12(\n\nparameters\x18\x01 \x01(\x0b\x32\x14.switchml.Parameters\x12\x35\n\x06\x63onfig\x18\x02 \x03(\x0b\x32%.switchml.WeightsResponse.ConfigEntry\x1a-\n\x0b\x43onfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x62\x06proto3'
)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='switchml.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensors', full_name='switchml.Parameters.tensors', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tensor_type', full_name='switchml.Parameters.tensor_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=86,
)


_FITRES_METRICSENTRY = _descriptor.Descriptor(
  name='MetricsEntry',
  full_name='switchml.FitRes.MetricsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='switchml.FitRes.MetricsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='switchml.FitRes.MetricsEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=257,
)

_FITRES = _descriptor.Descriptor(
  name='FitRes',
  full_name='switchml.FitRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parameters', full_name='switchml.FitRes.parameters', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_examples', full_name='switchml.FitRes.num_examples', index=1,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='switchml.FitRes.metrics', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_FITRES_METRICSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=257,
)


_EVALRES_METRICSENTRY = _descriptor.Descriptor(
  name='MetricsEntry',
  full_name='switchml.EvalRes.MetricsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='switchml.EvalRes.MetricsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='switchml.EvalRes.MetricsEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=257,
)

_EVALRES = _descriptor.Descriptor(
  name='EvalRes',
  full_name='switchml.EvalRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='loss', full_name='switchml.EvalRes.loss', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_examples', full_name='switchml.EvalRes.num_examples', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='switchml.EvalRes.metrics', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EVALRES_METRICSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=260,
  serialized_end=402,
)


_WEIGHTSINVOCATION = _descriptor.Descriptor(
  name='WeightsInvocation',
  full_name='switchml.WeightsInvocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fit_res', full_name='switchml.WeightsInvocation.fit_res', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='eval_res', full_name='switchml.WeightsInvocation.eval_res', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=404,
  serialized_end=495,
)


_WEIGHTSRESPONSE_CONFIGENTRY = _descriptor.Descriptor(
  name='ConfigEntry',
  full_name='switchml.WeightsResponse.ConfigEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='switchml.WeightsResponse.ConfigEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='switchml.WeightsResponse.ConfigEntry.value', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=614,
  serialized_end=659,
)

_WEIGHTSRESPONSE = _descriptor.Descriptor(
  name='WeightsResponse',
  full_name='switchml.WeightsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parameters', full_name='switchml.WeightsResponse.parameters', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='switchml.WeightsResponse.config', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_WEIGHTSRESPONSE_CONFIGENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=498,
  serialized_end=659,
)

_FITRES_METRICSENTRY.containing_type = _FITRES
_FITRES.fields_by_name['parameters'].message_type = _PARAMETERS
_FITRES.fields_by_name['metrics'].message_type = _FITRES_METRICSENTRY
_EVALRES_METRICSENTRY.containing_type = _EVALRES
_EVALRES.fields_by_name['metrics'].message_type = _EVALRES_METRICSENTRY
_WEIGHTSINVOCATION.fields_by_name['fit_res'].message_type = _FITRES
_WEIGHTSINVOCATION.fields_by_name['eval_res'].message_type = _EVALRES
_WEIGHTSRESPONSE_CONFIGENTRY.containing_type = _WEIGHTSRESPONSE
_WEIGHTSRESPONSE.fields_by_name['parameters'].message_type = _PARAMETERS
_WEIGHTSRESPONSE.fields_by_name['config'].message_type = _WEIGHTSRESPONSE_CONFIGENTRY
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['FitRes'] = _FITRES
DESCRIPTOR.message_types_by_name['EvalRes'] = _EVALRES
DESCRIPTOR.message_types_by_name['WeightsInvocation'] = _WEIGHTSINVOCATION
DESCRIPTOR.message_types_by_name['WeightsResponse'] = _WEIGHTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), {
  'DESCRIPTOR' : _PARAMETERS,
  '__module__' : 'protobuf.service_pb2'
  # @@protoc_insertion_point(class_scope:switchml.Parameters)
  })
_sym_db.RegisterMessage(Parameters)

FitRes = _reflection.GeneratedProtocolMessageType('FitRes', (_message.Message,), {

  'MetricsEntry' : _reflection.GeneratedProtocolMessageType('MetricsEntry', (_message.Message,), {
    'DESCRIPTOR' : _FITRES_METRICSENTRY,
    '__module__' : 'protobuf.service_pb2'
    # @@protoc_insertion_point(class_scope:switchml.FitRes.MetricsEntry)
    })
  ,
  'DESCRIPTOR' : _FITRES,
  '__module__' : 'protobuf.service_pb2'
  # @@protoc_insertion_point(class_scope:switchml.FitRes)
  })
_sym_db.RegisterMessage(FitRes)
_sym_db.RegisterMessage(FitRes.MetricsEntry)

EvalRes = _reflection.GeneratedProtocolMessageType('EvalRes', (_message.Message,), {

  'MetricsEntry' : _reflection.GeneratedProtocolMessageType('MetricsEntry', (_message.Message,), {
    'DESCRIPTOR' : _EVALRES_METRICSENTRY,
    '__module__' : 'protobuf.service_pb2'
    # @@protoc_insertion_point(class_scope:switchml.EvalRes.MetricsEntry)
    })
  ,
  'DESCRIPTOR' : _EVALRES,
  '__module__' : 'protobuf.service_pb2'
  # @@protoc_insertion_point(class_scope:switchml.EvalRes)
  })
_sym_db.RegisterMessage(EvalRes)
_sym_db.RegisterMessage(EvalRes.MetricsEntry)

WeightsInvocation = _reflection.GeneratedProtocolMessageType('WeightsInvocation', (_message.Message,), {
  'DESCRIPTOR' : _WEIGHTSINVOCATION,
  '__module__' : 'protobuf.service_pb2'
  # @@protoc_insertion_point(class_scope:switchml.WeightsInvocation)
  })
_sym_db.RegisterMessage(WeightsInvocation)

WeightsResponse = _reflection.GeneratedProtocolMessageType('WeightsResponse', (_message.Message,), {

  'ConfigEntry' : _reflection.GeneratedProtocolMessageType('ConfigEntry', (_message.Message,), {
    'DESCRIPTOR' : _WEIGHTSRESPONSE_CONFIGENTRY,
    '__module__' : 'protobuf.service_pb2'
    # @@protoc_insertion_point(class_scope:switchml.WeightsResponse.ConfigEntry)
    })
  ,
  'DESCRIPTOR' : _WEIGHTSRESPONSE,
  '__module__' : 'protobuf.service_pb2'
  # @@protoc_insertion_point(class_scope:switchml.WeightsResponse)
  })
_sym_db.RegisterMessage(WeightsResponse)
_sym_db.RegisterMessage(WeightsResponse.ConfigEntry)


_FITRES_METRICSENTRY._options = None
_EVALRES_METRICSENTRY._options = None
_WEIGHTSRESPONSE_CONFIGENTRY._options = None
# @@protoc_insertion_point(module_scope)
