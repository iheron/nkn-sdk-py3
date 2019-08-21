# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pb/sigchain.proto

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
  name='pb/sigchain.proto',
  package='pb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11pb/sigchain.proto\x12\x02pb\"\x8d\x01\n\x0cSigChainElem\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x13\n\x0bnext_pubkey\x18\x02 \x01(\x0c\x12\x0e\n\x06mining\x18\x03 \x01(\x08\x12\x11\n\tsignature\x18\x04 \x01(\x0c\x12\x1d\n\x08sig_algo\x18\x05 \x01(\x0e\x32\x0b.pb.SigAlgo\x12\x0b\n\x03vrf\x18\x06 \x01(\x0c\x12\r\n\x05proof\x18\x07 \x01(\x0c\"\xab\x01\n\x08SigChain\x12\r\n\x05nonce\x18\x01 \x01(\r\x12\x11\n\tdata_size\x18\x02 \x01(\r\x12\x12\n\nblock_hash\x18\x03 \x01(\x0c\x12\x0e\n\x06src_id\x18\x04 \x01(\x0c\x12\x12\n\nsrc_pubkey\x18\x05 \x01(\x0c\x12\x0f\n\x07\x64\x65st_id\x18\x06 \x01(\x0c\x12\x13\n\x0b\x64\x65st_pubkey\x18\x07 \x01(\x0c\x12\x1f\n\x05\x65lems\x18\x08 \x03(\x0b\x32\x10.pb.SigChainElem*!\n\x07SigAlgo\x12\r\n\tSIGNATURE\x10\x00\x12\x07\n\x03VRF\x10\x01\x62\x06proto3')
)

_SIGALGO = _descriptor.EnumDescriptor(
  name='SigAlgo',
  full_name='pb.SigAlgo',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SIGNATURE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VRF', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=343,
  serialized_end=376,
)
_sym_db.RegisterEnumDescriptor(_SIGALGO)

SigAlgo = enum_type_wrapper.EnumTypeWrapper(_SIGALGO)
SIGNATURE = 0
VRF = 1



_SIGCHAINELEM = _descriptor.Descriptor(
  name='SigChainElem',
  full_name='pb.SigChainElem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pb.SigChainElem.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_pubkey', full_name='pb.SigChainElem.next_pubkey', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mining', full_name='pb.SigChainElem.mining', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='pb.SigChainElem.signature', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sig_algo', full_name='pb.SigChainElem.sig_algo', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vrf', full_name='pb.SigChainElem.vrf', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proof', full_name='pb.SigChainElem.proof', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=26,
  serialized_end=167,
)


_SIGCHAIN = _descriptor.Descriptor(
  name='SigChain',
  full_name='pb.SigChain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nonce', full_name='pb.SigChain.nonce', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_size', full_name='pb.SigChain.data_size', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_hash', full_name='pb.SigChain.block_hash', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='src_id', full_name='pb.SigChain.src_id', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='src_pubkey', full_name='pb.SigChain.src_pubkey', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest_id', full_name='pb.SigChain.dest_id', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest_pubkey', full_name='pb.SigChain.dest_pubkey', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='elems', full_name='pb.SigChain.elems', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=170,
  serialized_end=341,
)

_SIGCHAINELEM.fields_by_name['sig_algo'].enum_type = _SIGALGO
_SIGCHAIN.fields_by_name['elems'].message_type = _SIGCHAINELEM
DESCRIPTOR.message_types_by_name['SigChainElem'] = _SIGCHAINELEM
DESCRIPTOR.message_types_by_name['SigChain'] = _SIGCHAIN
DESCRIPTOR.enum_types_by_name['SigAlgo'] = _SIGALGO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SigChainElem = _reflection.GeneratedProtocolMessageType('SigChainElem', (_message.Message,), dict(
  DESCRIPTOR = _SIGCHAINELEM,
  __module__ = 'pb.sigchain_pb2'
  # @@protoc_insertion_point(class_scope:pb.SigChainElem)
  ))
_sym_db.RegisterMessage(SigChainElem)

SigChain = _reflection.GeneratedProtocolMessageType('SigChain', (_message.Message,), dict(
  DESCRIPTOR = _SIGCHAIN,
  __module__ = 'pb.sigchain_pb2'
  # @@protoc_insertion_point(class_scope:pb.SigChain)
  ))
_sym_db.RegisterMessage(SigChain)


# @@protoc_insertion_point(module_scope)