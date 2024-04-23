from django.shortcuts import render

# other modules.
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# self modules 
from .models import *
from .serializers import ProjectSerializer, ProjectSerializerModel, TaskSerializer
from .permissions import IsMemberOrOwner

# utils
from datetime import datetime


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializerModel
    permission_classes = [
        IsAuthenticated
    ]


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    permission_classes = [
        IsAuthenticated,
        IsMemberOrOwner
    ]


    def filter_queryset(self, queryset):
        
        request_user = self.request.user
        queryset = queryset.filter(ownerstasks__user = request_user)

        return queryset



    @action(detail=True, methods=['post'])
    def complete_task(self, request, pk=None):
        
        task = self.get_object()
        task.is_complete = True
        task.save()

        task_data = self.get_serializer_class() (task).data
        return Response(task_data)
