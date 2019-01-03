from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import User
import datetime 
import factory


class AccountTests(APITestCase):
    def setUp(self):
        """
        Ensure we can create a new User.
        """
        self.user1 = User.objects.create(
            id='2881a0cc-1499-45b1-bbb4-3bfd32f025e9', 
            username='jao', 
            password='senhadeteste123',
            first_name='Joao', 
            last_name='Das neves', 
            email='teste@teste.com',
            formation='Teacher', 
            gender='M', 
            birthday='2000-11-11'
        )

        self.user2 = User.objects.create(
            id='43fb1a04-f329-49af-be58-079987eeeb7b', 
            username='ssss', 
            password='senhadeteste123',
            first_name='Jsoao', 
            last_name='Das neves', 
            email='tesste@teste.com',
            formation='Teacher', 
            gender='F', 
            birthday='2000-11-11'
        )

    def test_create_account(self):
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(self.user1.username, 'jao')
        self.assertEqual(self.user1.gender, 'M')
        self.assertEqual(self.user2.gender, 'F')
        self.assertEqual(self.user1.birthday, '2000-11-11')

