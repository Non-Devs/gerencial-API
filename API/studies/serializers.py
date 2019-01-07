from rest_framework import serializers
from .models import Students, Lesson
import datetime
from dateutil.relativedelta import relativedelta


class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = ('id', 'first_name', 'last_name', 'responsible_name', 'telephone', 'birthday', 'school',
                  'grade', 'adress', 'subject', 'teacher',)
        read_only_fields = ('teacher', )


class LessonSerializer(serializers.ModelSerializer):



    class Meta:
        model = Lesson
        fields = ('id', 'student', 'hour', 'duration', 'value', 'final_hour')
        read_only_fields = ('final_hour', )

    def save(self, **kwargs):
        
        validated_data = dict(
            list(self.validated_data.items()) +
            list(kwargs.items())
        )

        if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
            self.instance.final_hour = self.initial_data['hour']
        else:
            self.instance = Lesson.objects.create(**validated_data, final_hour=self.initial_data['hour'])

        return self.instance