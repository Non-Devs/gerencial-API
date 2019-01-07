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

        self.lesson_data = ({
            'student': '1',
            'hour': '10:10:10',
            'duration': '10',
            'value': '10'
        })

    def test_post_request_with_valid_data_succeeds(self):

        self.client.force_authenticate(self.user)
        response = self.client.post(self.url, self.lesson_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        lesson = Lesson.objects.get(pk=response.data.get('id'))

