import factory, factory.fuzzy
from ..models import User
from random import choice

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'users.User'
        django_get_or_create = ('username',)

    id = factory.Faker('uuid4')
    username = factory.Sequence(lambda n: f'testuser{n}')
    password = factory.Faker('password', length=10, special_chars=True, digits=True,
                             upper_case=True, lower_case=True)
    email = factory.Faker('email')
    birthday = factory.Faker('date_this_century')
    gender = factory.LazyAttribute(lambda x: choice(User.gender_choices)[0])
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    formation = factory.fuzzy.FuzzyText(length=12)
    is_active = True
    is_staff = False
