from django.test import TestCase
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import check_password
from nose.tools import eq_, ok_
from .factories import UserFactory
from ..serializers import CreateUserSerializer


class TestCreateUserSerializer(TestCase):

    def setUp(self):
        self.user_data = model_to_dict(UserFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = CreateUserSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = CreateUserSerializer(data=self.user_data)
        ok_(serializer.is_valid())

    def test_serializer_hashes_password(self):
        serializer = CreateUserSerializer(data=self.user_data)
        ok_(serializer.is_valid())

        user = serializer.save()
        ok_(check_password(self.user_data.get('password'), user.password))

    def test_contains_expected_fields(self):
        serializer = CreateUserSerializer(data=self.user_data)
        serializer.is_valid()
        data = serializer.data

        self.assertEqual(set(data.keys()), set(['gender', 'birthday', 'formation', 'username',
                                                'email', 'first_name', 'last_name']))

    def test_gender_field_content(self):
        serializer = CreateUserSerializer(data=self.user_data)
        serializer.is_valid()
        data = serializer.data

        self.assertEqual(data['gender'], self.user_data['gender'])