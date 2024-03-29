# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: events.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='events.proto',
  package='dundaa.contracts',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0c\x65vents.proto\x12\x10\x64undaa.contracts\"\xa7\x01\n\x05\x45vent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08location\x18\x02 \x01(\t\x12\x12\n\nstart_date\x18\x03 \x01(\x02\x12\x10\n\x08\x65nd_date\x18\x04 \x01(\x02\x12\x12\n\nstart_time\x18\x05 \x01(\x02\x12\x10\n\x08\x65nd_time\x18\x06 \x01(\x02\x12\x12\n\nbanner_url\x18\x07 \x01(\t\x12\x11\n\tsite_name\x18\x08 \x01(\t\x12\x0b\n\x03url\x18\t \x01(\t\"1\n\x06\x45vents\x12\'\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x17.dundaa.contracts.Eventb\x06proto3')
)




_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='dundaa.contracts.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dundaa.contracts.Event.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='dundaa.contracts.Event.location', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='dundaa.contracts.Event.start_date', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_date', full_name='dundaa.contracts.Event.end_date', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='dundaa.contracts.Event.start_time', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='dundaa.contracts.Event.end_time', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='banner_url', full_name='dundaa.contracts.Event.banner_url', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='site_name', full_name='dundaa.contracts.Event.site_name', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='dundaa.contracts.Event.url', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=35,
  serialized_end=202,
)


_EVENTS = _descriptor.Descriptor(
  name='Events',
  full_name='dundaa.contracts.Events',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='dundaa.contracts.Events.events', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=204,
  serialized_end=253,
)

_EVENTS.fields_by_name['events'].message_type = _EVENT
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['Events'] = _EVENTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'events_pb2'
  # @@protoc_insertion_point(class_scope:dundaa.contracts.Event)
  })
_sym_db.RegisterMessage(Event)

Events = _reflection.GeneratedProtocolMessageType('Events', (_message.Message,), {
  'DESCRIPTOR' : _EVENTS,
  '__module__' : 'events_pb2'
  # @@protoc_insertion_point(class_scope:dundaa.contracts.Events)
  })
_sym_db.RegisterMessage(Events)


# @@protoc_insertion_point(module_scope)
