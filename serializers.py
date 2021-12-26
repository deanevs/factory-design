import json
import xml.etree.ElementTree as et


class ObjectSerializer:
    def serialize(self, ser_obj, req_fmt):
        obj_serializer = factory.get_serializer(req_fmt)
        ser_obj.song_serialize(obj_serializer)
        return obj_serializer.to_str()


class SerializerFactory:

    def __init__(self):
        self._creators = {}

    def register_format(self, fmt, creator):
        self._creators[fmt] = creator

    def get_serializer(self, fmt):
        creator = self._creators.get(fmt)
        print("Creator = {}".format(creator))
        if not creator:
            raise ValueError(fmt)
        return creator()


class JsonSerializer:
    def __init__(self):
        self._current_object = None

    def start_object(self, object_name, object_id):
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class XmlSerializer:
    def __init__(self):
        self._element = None

    def start_object(self, object_name, object_id):
        self._element = et.Element(object_name, attrib={'id': object_id})

    def add_property(self, name, value):
        prop = et.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return et.tostring(self._element, encoding='unicode')

    def register_format(self, format, creator):
        self._creators[format] = creator

    def get_serializer(self, format):
        creator = self._creators.get(format)
        if not creator:
            raise ValueError(format)
        return creator()


factory = SerializerFactory()
factory.register_format('JSON', JsonSerializer)
factory.register_format('XML', XmlSerializer)