from __future__ import print_function, unicode_literals
from rest_framework3.serializers import ModelSerializer
from rest_framework_bulk3.serializers import BulkListSerializer, BulkSerializerMixin

from .models import SimpleModel


class SimpleSerializer(BulkSerializerMixin,  # only required in DRF3
                       ModelSerializer):
    class Meta(object):
        model = SimpleModel
        # only required in DRF3
        list_serializer_class = BulkListSerializer
