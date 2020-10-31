# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ListSerializer


class CreateSerializerMixin:

    def create(self, validated_data):

        # Remove related data from validated_data
        nested_data = {
            name: validated_data.pop(name)
            for name, field in self.fields.items()
            if isinstance(field, (ListSerializer, ModelSerializer))
        }

        # Create instance
        instance = super().create(validated_data)
        
        # Create related data
        model_fields_map = self.Meta.model._meta.fields_map
        for name, nested_val_data in nested_data.items():
            serializer_field = self.fields[name]
            if isinstance(serializer_field, ListSerializer):
                for data in nested_val_data:
                    field_name = model_fields_map[name].remote_field.name
                    data[field_name] = instance
                    serializer_field.child.create(data)
        
        return instance