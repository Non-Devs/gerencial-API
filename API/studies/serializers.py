from rest_framework import serializers
from .models import Students


class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = ('id', 'first_name', 'last_name', 'responsible_name', 'telephone', 'birthday', 'school',
                  'grade', 'adress', 'subject', 'teacher',)
        read_only_fields = ('teacher', )
        extra_kwargs = {'teacher': {'write_only': True}}