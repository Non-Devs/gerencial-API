from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import Students
from .serializers import StudentsSerializer
from API.users.permissions import IsUserOrReadOnly


class StudentsViewSet(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = (IsUserOrReadOnly,)


class StudentsCreateViewSet(mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)