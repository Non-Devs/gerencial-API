from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import Students, Lesson
from .serializers import StudentsSerializer, LessonSerializer
from .permissions import IsOwnerStudents, IsOwnerLesson


class StudentsViewSet(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    """
    Updates and retrieves students
    """
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = (IsOwnerStudents,)


class StudentsCreateViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    """
    Creates students
    """
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

    def get_queryset(self):
        return Students.objects.filter(teacher=self.request.user)


class LessonViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    """
    Updates and retrieves lessons
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsOwnerLesson,)


class LessonCreateViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    """
    Creates lessons
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    def get_queryset(self):
        return Lesson.objects.filter(student__teacher=self.request.user)
