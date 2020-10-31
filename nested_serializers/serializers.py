# -*- coding: utf-8 -*-

from rest_framework.serializers import ModelSerializer

from .mixins import CreateSerializerMixin

class NestedSerializer(
    CreateSerializerMixin,
    ModelSerializer
):
    pass