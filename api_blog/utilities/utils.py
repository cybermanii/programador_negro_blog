import json
from django.core import serializers

def json_serializer(value):
    return json.loads(serializers.serialize('json', value))