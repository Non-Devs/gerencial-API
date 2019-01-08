# Generated by Django 2.1.4 on 2019-01-07 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0002_auto_20190105_2326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.TimeField()),
                ('duration', models.IntegerField()),
                ('value', models.IntegerField()),
                ('final_hour', models.TimeField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='studies.Students')),
            ],
        ),
    ]