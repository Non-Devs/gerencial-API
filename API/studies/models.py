from django.db import models
from API.users.models import User


class Students(models.Model):

    first_name = models.CharField(
        max_length=30,
        blank=False,
        null=True,
    )

    last_name = models.CharField(
        max_length=30,
        blank=False,
        null=True,
    )

    responsible_name = models.CharField(
        max_length=30,
        blank=False,
        null=True,
    )

    telephone = models.CharField(
        blank=False,
        null=True,
        max_length=14,
        # validators=[validate_phone],
    )

    birthday = models.DateField(
        blank=False,
        null=True
    )

    school = models.CharField(
        max_length=50,
        blank=False,
        null=True,
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
        ('9a', '9º ano - fundamental'),
        ('1em', '1º ano - médio'),
        ('2em', '1º ano - médio'),
        ('3em', '1º ano - médio'),
        ('others', 'Outro'),
    )

    grade = models.CharField(
        choices=grade_choices,
        blank=False,
        max_length=20,
        null=True,
    )

    adress = models.TextField(
        max_length=400
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
        blank=False,
        max_length=20,
        null=True,
    )

    teacher = models.ForeignKey(
        User,
        related_name='teacher',
        on_delete=models.CASCADE,
    )
