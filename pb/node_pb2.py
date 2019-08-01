# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pb/node.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pb/node.proto',
  package='pb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rpb/node.proto\x12\x02pb\"g\n\x08NodeData\x12\x12\n\npublic_key\x18\x01 \x01(\x0c\x12\x16\n\x0ewebsocket_port\x18\x02 \x01(\r\x12\x15\n\rjson_rpc_port\x18\x03 \x01(\r\x12\x18\n\x10protocol_version\x18\x04 \x01(\r*\\\n\tSyncState\x12\x14\n\x10WAIT_FOR_SYNCING\x10\x00\x12\x10\n\x0cSYNC_STARTED\x10\x01\x12\x11\n\rSYNC_FINISHED\x10\x02\x12\x14\n\x10PERSIST_FINISHED\x10\x03\x62\x06proto3')
)

_SYNCSTATE = _descriptor.EnumDescriptor(
  name='SyncState',
  full_name='pb.SyncState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WAIT_FOR_SYNCING', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYNC_STARTED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYNC_FINISHED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERSIST_FINISHED', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=126,
  serialized_end=218,
)
_sym_db.RegisterEnumDescriptor(_SYNCSTATE)

SyncState = enum_type_wrapper.EnumTypeWrapper(_SYNCSTATE)
WAIT_FOR_SYNCING = 0
SYNC_STARTED = 1
SYNC_FINISHED = 2
PERSIST_FINISHED = 3



_NODEDATA = _descriptor.Descriptor(
  name='NodeData',
  full_name='pb.NodeData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_key', full_name='pb.NodeData.public_key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='websocket_port', full_name='pb.NodeData.websocket_port', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='json_rpc_port', full_name='pb.NodeData.json_rpc_port', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protocol_version', full_name='pb.NodeData.protocol_version', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=21,
  serialized_end=124,
)

DESCRIPTOR.message_types_by_name['NodeData'] = _NODEDATA
DESCRIPTOR.enum_types_by_name['SyncState'] = _SYNCSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NodeData = _reflection.GeneratedProtocolMessageType('NodeData', (_message.Message,), dict(
  DESCRIPTOR = _NODEDATA,
  __module__ = 'pb.node_pb2'
  # @@protoc_insertion_point(class_scope:pb.NodeData)
  ))
_sym_db.RegisterMessage(NodeData)


# @@protoc_insertion_point(module_scope)
