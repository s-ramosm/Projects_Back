from rest_framework import serializers
from .models import Project, Task
from datetime import datetime

from pytz import timezone


class ProjectSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

class ProjectSerializer(serializers.Serializer):
    
    name = serializers.CharField(max_length = 60)
    init_date = serializers.DateTimeField( required=False)
    end_date = serializers.DateTimeField()

    def validate(self, attrs):
        return super().validate(attrs)


    def create(self, validated_data):

        Project(**validated_data).save()
        return self.data
    





