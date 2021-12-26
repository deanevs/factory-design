

from songs import *
from serializers import *
import yaml_serializer

song = Song('1', 'Water of Love', 'Dire Straits')

my_serializer = ObjectSerializer()

print(my_serializer.serialize(song, 'JSON'))
print(my_serializer.serialize(song, 'XML'))
print(my_serializer.serialize(song, 'YAML'))




