from django.test import TestCase
from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import check_password
from nose.tools import ok_, eq_
from rest_framework.test import APITestCase, APIClient, \
                                force_authenticate, APIRequestFactory
from rest_framework import status
from faker import Faker
from API.users.models import User
from API.users.test.factories import UserFactory
from API.studies.models import Students, Lesson


class TestUserListTestCase(APITestCase):
    """
    Tests /lesson list operations.
    """

    def setUp(self):
        self.url = reverse('lesson-list')
        self.user = User.objects.create_user(
            username='Teste',
            password='12d34d56f78',
            birthday='2000-11-11'
        )
        self.student = Students.objects.create(
            first_name='Joao',
            last_name='das Neves',
            responsible_name='Ned',
            telephone='992789954',
            birthday='2000-11-11',
            school='Stella',
            grade='1em',
            adress='Sla',
            subject='geo',
            teacher=self.user,
        )

    def test_post_request_with_lesson_data_succeeds(self):

        self.lesson_data = ({
            'student': self.student.pk,
            'hour': '10:10:10',
            'duration': '10',
            'value': '10',
            'weekdays': ['seg', 'qua'],
        })

        self.client.force_authenticate(self.user)
        response = self.client.post(self.url, self.lesson_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

    def test_post_request_with_lesson_data2_succeeds(self):

        self.lesson_data2 = ({
            'student': self.student.pk,
            'hour': '08:00:10',
            'duration': '70',
            'value': '10',
            'weekdays': ['seg','qua'],
        })

        self.client.force_authenticate(self.user)
        response = self.client.post(self.url, self.lesson_data2)
        eq_(response.status_code, status.HTTP_201_CREATED)

    def test_post_request_with_no_weekdays(self):

        self.lesson_data3 = ({
            'student': self.student.pk,
            'hour': '08:00:10',
            'duration': '70',
            'value': '10',
            'weekdays': [],
        })

        self.client.force_authenticate(self.user)
        response = self.client.post(self.url, self.lesson_data3)
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_more_than_5_weekdays(self):

        self.lesson_data4 = ({
            'student': self.student.pk,
            'hour': '08:00:10',
            'duration': '70',
            'value': '10',
            'weekdays': ['seg', 'ter', 'qua', 'qui', 'sex', 'sab'],
        })

        self.client.force_authenticate(self.user)
        response = self.client.post(self.url, self.lesson_data4)
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_request(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

class TestLessonDetailTestCase(APITestCase):
    """
    Tests /lesson detail operations.
    """

    def setUp(self):
        self.user1 = User.objects.create_user(
            username='Teste',
            password='12d34d56f78',
            birthday='2000-11-11',
        )
        self.student1 = Students.objects.create(
            first_name='Joao',
            last_name='das Neves',
            responsible_name='Ned',
            telephone='992789954',
            birthday='2000-11-11',
            school='Stella',
            grade='1em',
            adress='Sla',
            subject='geo',
            teacher=self.user1,
        )
        self.lesson = Lesson.objects.create(
            student=self.student1,
            hour='10:10:10',
            duration='10',
            value='10',
            final_hour='10:10:10',
            weekdays=['seg', 'qua'],
        )
        self.url = reverse('lesson-detail', kwargs={'pk': self.lesson.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user1.auth_token}')

    def test_put_request_updates_a_lesson_less_than_1h(self):
        hour = "15:02:00"
        duration = 20
        value = 15
        weekdays = ['seg', 'qua']
        payload = {
                    "student": self.student1.pk,
                    "hour": hour,
                    "duration": duration,
                    "value": value,
                    "weekdays": weekdays,
                   }
        response = self.client.put(self.url, payload)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_put_request_updates_a_lesson_more_than_1h(self):
        hour = "15:02:00"
        duration = 75
        value = 15
        weekdays = ['seg', 'qua']
        payload = {
                    "student": self.student1.pk,
                    "hour": hour,
                    "duration": duration,
                    "value": value,
                    "weekdays": weekdays,
                   }
        response = self.client.put(self.url, payload)
        eq_(response.status_code, status.HTTP_200_OK)