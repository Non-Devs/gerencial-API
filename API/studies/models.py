from django.db import models
from API.users.models import User
from multiselectfield import MultiSelectField


class Students(models.Model):

    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=30,
    )

    responsible_name = models.CharField(
        max_length=30,
    )

    telephone = models.CharField(
        max_length=14,
    )

    birthday = models.DateField()

    school = models.CharField(
        max_length=50,
    )

    grade_choices = (
        ('1f', '1º ano - fundamental'),
        ('2f', '2º ano - fundamental'),
        ('3f', '3º ano - fundamental'),
        ('4f', '4º ano - fundamental'),
        ('5f', '5º ano - fundamental'),
        ('6f', '6º ano - fundamental'),
        ('7f', '7º ano - fundamental'),
        ('8f', '8º ano - fundamental'),
        ('9f', '9º ano - fundamental'),
        ('1em', '1º ano - médio'),
        ('2em', '2º ano - médio'),
        ('3em', '3º ano - médio'),
        ('others', 'Outro'),
    )

    grade = models.CharField(
        choices=grade_choices,
        max_length=20,
    )

    adress = models.TextField(
        max_length=400,
    )

    subject_choices = (
        ('mat', 'Matemática'),
        ('port', 'Português'),
        ('ingles', 'Inglês'),
        ('ciencia', 'Ciências'),
        ('geo', 'Geografia'),
        ('hist', 'História'),
        ('outra', 'Outra disciplina'),
    )

    subject = models.CharField(
        choices=subject_choices,
        max_length=20,
    )

    teacher = models.ForeignKey(
        User,
        related_name='teacher',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.first_name


class Lesson(models.Model):

    student = models.ForeignKey(
        Students,
        related_name='student',
        on_delete=models.CASCADE,
    )

    hour = models.TimeField()

    # In minutes
    duration = models.IntegerField()

    # In hour/class
    value = models.IntegerField()

    final_hour = models.TimeField()

    DAYS_OF_WEEK = (
        ('dom', 'Domingo'),
        ('seg', 'Segunda-feira'),
        ('ter', 'Terça-feira'),
        ('qua', 'Quarta-feira'),
        ('qui', 'Quinta-feira'),
        ('sex', 'Sexta-feira'),
        ('sab', 'Sábado'),
    )

    weekdays = MultiSelectField(
        choices=DAYS_OF_WEEK,
        max_choices=5,
        max_length=30,
    )
