# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eigr/actor.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='eigr/actor.proto',
  package='eigr.actors',
  syntax='proto3',
  serialized_options=b'\n!io.eigr.functions.protocol.actorsZ-github.com/eigr/go-support/eigr/actors;actors',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x65igr/actor.proto\x12\x0b\x65igr.actors\x1a\x19google/protobuf/any.proto\"\x80\x01\n\x08Registry\x12\x31\n\x06\x61\x63tors\x18\x01 \x03(\x0b\x32!.eigr.actors.Registry.ActorsEntry\x1a\x41\n\x0b\x41\x63torsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.eigr.actors.Actor:\x02\x38\x01\"D\n\x0b\x41\x63torSystem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\'\n\x08registry\x18\x02 \x01(\x0b\x32\x15.eigr.actors.Registry\"T\n\x15\x41\x63torSnapshotStrategy\x12/\n\x07timeout\x18\x01 \x01(\x0b\x32\x1c.eigr.actors.TimeoutStrategyH\x00\x42\n\n\x08strategy\"V\n\x17\x41\x63torDeactivateStrategy\x12/\n\x07timeout\x18\x01 \x01(\x0b\x32\x1c.eigr.actors.TimeoutStrategyH\x00\x42\n\n\x08strategy\"\"\n\x0fTimeoutStrategy\x12\x0f\n\x07timeout\x18\x01 \x01(\x03\"\x8f\x01\n\nActorState\x12/\n\x04tags\x18\x01 \x03(\x0b\x32!.eigr.actors.ActorState.TagsEntry\x12#\n\x05state\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xd3\x01\n\x05\x41\x63tor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\npersistent\x18\x02 \x01(\x08\x12&\n\x05state\x18\x03 \x01(\x0b\x32\x17.eigr.actors.ActorState\x12=\n\x11snapshot_strategy\x18\x04 \x01(\x0b\x32\".eigr.actors.ActorSnapshotStrategy\x12\x41\n\x13\x64\x65\x61\x63tivate_strategy\x18\x05 \x01(\x0b\x32$.eigr.actors.ActorDeactivateStrategyBR\n!io.eigr.functions.protocol.actorsZ-github.com/eigr/go-support/eigr/actors;actorsb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_REGISTRY_ACTORSENTRY = _descriptor.Descriptor(
  name='ActorsEntry',
  full_name='eigr.actors.Registry.ActorsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='eigr.actors.Registry.ActorsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='eigr.actors.Registry.ActorsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=189,
)

_REGISTRY = _descriptor.Descriptor(
  name='Registry',
  full_name='eigr.actors.Registry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='actors', full_name='eigr.actors.Registry.actors', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_REGISTRY_ACTORSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=189,
)


_ACTORSYSTEM = _descriptor.Descriptor(
  name='ActorSystem',
  full_name='eigr.actors.ActorSystem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='eigr.actors.ActorSystem.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='registry', full_name='eigr.actors.ActorSystem.registry', index=1,
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
  serialized_start=191,
  serialized_end=259,
)


_ACTORSNAPSHOTSTRATEGY = _descriptor.Descriptor(
  name='ActorSnapshotStrategy',
  full_name='eigr.actors.ActorSnapshotStrategy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeout', full_name='eigr.actors.ActorSnapshotStrategy.timeout', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='strategy', full_name='eigr.actors.ActorSnapshotStrategy.strategy',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=261,
  serialized_end=345,
)


_ACTORDEACTIVATESTRATEGY = _descriptor.Descriptor(
  name='ActorDeactivateStrategy',
  full_name='eigr.actors.ActorDeactivateStrategy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeout', full_name='eigr.actors.ActorDeactivateStrategy.timeout', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='strategy', full_name='eigr.actors.ActorDeactivateStrategy.strategy',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=347,
  serialized_end=433,
)


_TIMEOUTSTRATEGY = _descriptor.Descriptor(
  name='TimeoutStrategy',
  full_name='eigr.actors.TimeoutStrategy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeout', full_name='eigr.actors.TimeoutStrategy.timeout', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=435,
  serialized_end=469,
)


_ACTORSTATE_TAGSENTRY = _descriptor.Descriptor(
  name='TagsEntry',
  full_name='eigr.actors.ActorState.TagsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='eigr.actors.ActorState.TagsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='eigr.actors.ActorState.TagsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=572,
  serialized_end=615,
)

_ACTORSTATE = _descriptor.Descriptor(
  name='ActorState',
  full_name='eigr.actors.ActorState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tags', full_name='eigr.actors.ActorState.tags', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='eigr.actors.ActorState.state', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ACTORSTATE_TAGSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=472,
  serialized_end=615,
)


_ACTOR = _descriptor.Descriptor(
  name='Actor',
  full_name='eigr.actors.Actor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='eigr.actors.Actor.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='persistent', full_name='eigr.actors.Actor.persistent', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='eigr.actors.Actor.state', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='snapshot_strategy', full_name='eigr.actors.Actor.snapshot_strategy', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deactivate_strategy', full_name='eigr.actors.Actor.deactivate_strategy', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=618,
  serialized_end=829,
)

_REGISTRY_ACTORSENTRY.fields_by_name['value'].message_type = _ACTOR
_REGISTRY_ACTORSENTRY.containing_type = _REGISTRY
_REGISTRY.fields_by_name['actors'].message_type = _REGISTRY_ACTORSENTRY
_ACTORSYSTEM.fields_by_name['registry'].message_type = _REGISTRY
_ACTORSNAPSHOTSTRATEGY.fields_by_name['timeout'].message_type = _TIMEOUTSTRATEGY
_ACTORSNAPSHOTSTRATEGY.oneofs_by_name['strategy'].fields.append(
  _ACTORSNAPSHOTSTRATEGY.fields_by_name['timeout'])
_ACTORSNAPSHOTSTRATEGY.fields_by_name['timeout'].containing_oneof = _ACTORSNAPSHOTSTRATEGY.oneofs_by_name['strategy']
_ACTORDEACTIVATESTRATEGY.fields_by_name['timeout'].message_type = _TIMEOUTSTRATEGY
_ACTORDEACTIVATESTRATEGY.oneofs_by_name['strategy'].fields.append(
  _ACTORDEACTIVATESTRATEGY.fields_by_name['timeout'])
_ACTORDEACTIVATESTRATEGY.fields_by_name['timeout'].containing_oneof = _ACTORDEACTIVATESTRATEGY.oneofs_by_name['strategy']
_ACTORSTATE_TAGSENTRY.containing_type = _ACTORSTATE
_ACTORSTATE.fields_by_name['tags'].message_type = _ACTORSTATE_TAGSENTRY
_ACTORSTATE.fields_by_name['state'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_ACTOR.fields_by_name['state'].message_type = _ACTORSTATE
_ACTOR.fields_by_name['snapshot_strategy'].message_type = _ACTORSNAPSHOTSTRATEGY
_ACTOR.fields_by_name['deactivate_strategy'].message_type = _ACTORDEACTIVATESTRATEGY
DESCRIPTOR.message_types_by_name['Registry'] = _REGISTRY
DESCRIPTOR.message_types_by_name['ActorSystem'] = _ACTORSYSTEM
DESCRIPTOR.message_types_by_name['ActorSnapshotStrategy'] = _ACTORSNAPSHOTSTRATEGY
DESCRIPTOR.message_types_by_name['ActorDeactivateStrategy'] = _ACTORDEACTIVATESTRATEGY
DESCRIPTOR.message_types_by_name['TimeoutStrategy'] = _TIMEOUTSTRATEGY
DESCRIPTOR.message_types_by_name['ActorState'] = _ACTORSTATE
DESCRIPTOR.message_types_by_name['Actor'] = _ACTOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Registry = _reflection.GeneratedProtocolMessageType('Registry', (_message.Message,), {

  'ActorsEntry' : _reflection.GeneratedProtocolMessageType('ActorsEntry', (_message.Message,), {
    'DESCRIPTOR' : _REGISTRY_ACTORSENTRY,
    '__module__' : 'eigr.actor_pb2'
    # @@protoc_insertion_point(class_scope:eigr.actors.Registry.ActorsEntry)
    })
  ,
  'DESCRIPTOR' : _REGISTRY,
  '__module__' : 'eigr.actor_pb2'
  # @@protoc_insertion_point(class_scope:eigr.actors.Registry)
  })
_sym_db.RegisterMessage(Registry)
_sym_db.RegisterMessage(Registry.ActorsEntry)

ActorSystem = _reflection.GeneratedProtocolMessageType('ActorSystem', (_message.Message,), {
  'DESCRIPTOR' : _ACTORSYSTEM,
  '__module__' : 'eigr.actor_pb2'
  # @@protoc_insertion_point(class_scope:eigr.actors.ActorSystem)
  })
_sym_db.RegisterMessage(ActorSystem)

ActorSnapshotStrategy = _reflection.GeneratedProtocolMessageType('ActorSnapshotStrategy', (_message.Message,), {
  'DESCRIPTOR' : _ACTORSNAPSHOTSTRATEGY,
  '__module__' : 'eigr.actor_pb2'
  # @@protoc_insertion_point(class_scope:eigr.actors.ActorSnapshotStrategy)
  })
_sym_db.RegisterMessage(ActorSnapshotStrategy)

ActorDeactivateStrategy = _reflection.GeneratedProtocolMessageType('ActorDeactivateStrategy', (_message.Message,), {
  'DESCRIPTOR' : _ACTORDEACTIVATESTRATEGY,
  '__module__' : 'eigr.actor_pb2'
  # @@protoc_insertion_point(class_scope:eigr.actors.ActorDeactivateStrategy)
  })
_sym_db.RegisterMessage(ActorDeactivateStrategy)

TimeoutStrategy = _reflection.GeneratedProtocolMessageType('TimeoutStrategy', (_message.Message,), {
  'DESCRIPTOR' : _TIMEOUTSTRATEGY,
  '__module__' : 'eigr.actor_pb2'
  # @@protoc_insertion_point(class_scope:eigr.actors.TimeoutStrategy)
  })
_sym_db.RegisterMessage(TimeoutStrategy)

ActorState = _reflection.GeneratedProtocolMessageType('ActorState', (_message.Message,), {

  'TagsEntry' : _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ACTORSTATE_TAGSENTRY,
    '__module__' : 'eigr.actor_pb2'
    # @@protoc_insertion_point(class_scope:eigr.actors.ActorState.TagsEntry)
    })
  ,
  'DESCRIPTOR' : _ACTORSTATE,
  '__module__' : 'eigr.actor_pb2'
  # @@protoc_insertion_point(class_scope:eigr.actors.ActorState)
  })
_sym_db.RegisterMessage(ActorState)
_sym_db.RegisterMessage(ActorState.TagsEntry)

Actor = _reflection.GeneratedProtocolMessageType('Actor', (_message.Message,), {
  'DESCRIPTOR' : _ACTOR,
  '__module__' : 'eigr.actor_pb2'
  # @@protoc_insertion_point(class_scope:eigr.actors.Actor)
  })
_sym_db.RegisterMessage(Actor)


DESCRIPTOR._options = None
_REGISTRY_ACTORSENTRY._options = None
_ACTORSTATE_TAGSENTRY._options = None
# @@protoc_insertion_point(module_scope)
