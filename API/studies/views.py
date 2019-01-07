from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import Students, Lesson
from .serializers import StudentsSerializer, LessonSerializer
from API.users.permissions import IsUserOrReadOnly
import datetime

class StudentsViewSet(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    """
    Updates and retrieves students
    """
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    # Verificar sobre essa permissão, pois não está permitindo um usuário editar 
    # o que ele mesmo criou
    permission_classes = (IsUserOrReadOnly,)


class StudentsCreateViewSet(mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    """
    Creates students
    """
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class LessonViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    """
    Updates and retrieves lessons
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    # Verificar sobre essa permissão, pois não está permitindo um usuário editar 
    # o que ele mesmo criou
    permission_classes = (IsUserOrReadOnly,)


class LessonCreateViewSet(mixins.CreateModelMixin,
                          viewsets.GenericViewSet):
    """
    Creates lessons
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (AllowAny,)
