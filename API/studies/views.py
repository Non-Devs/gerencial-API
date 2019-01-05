from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


class StudentsViewset(viewsets.ModelViewSet):
    queryset = models.Students.objects.all()
    serializer_class = serializers.StudentsSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)