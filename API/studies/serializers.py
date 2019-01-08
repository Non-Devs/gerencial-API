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
            hour = self.initial_data['hour'][:5]
            datetime_hour = datetime.datetime.strptime(str(hour), '%H:%M')
            duration = int(float(self.initial_data['duration']))

            if duration > 60:
                fhhour = duration//60
                duration = duration % 60
            else:
                fhhour = 0

            fhour = datetime_hour + datetime.timedelta(minutes=duration) + datetime.timedelta(hours=fhhour)
            self.instance.final_hour = fhour.time()
        else:
            hour = self.initial_data['hour'][:5]
            datetime_hour = datetime.datetime.strptime(str(hour), '%H:%M')
            duration = int(float(self.initial_data['duration']))

            if duration > 60:
                fhhour = duration//60
                duration = duration % 60
            else:
                fhhour = 0

            fhour = datetime_hour + datetime.timedelta(minutes=duration) + datetime.timedelta(hours=fhhour)
            print(fhour)
            self.instance = Lesson.objects.create(**validated_data, final_hour=fhour.time())

        return self.instance

    def __init__(self, *args, **kwargs):
        super(LessonSerializer, self).__init__(*args, **kwargs)
        request_user = self.context['request'].user
        self.fields['student'].queryset = Students.objects.filter(teacher=request_user)
