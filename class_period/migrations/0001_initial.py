# Generated by Django 5.0.6 on 2024-07-14 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class_Period',
            fields=[
                ('name', models.CharField(default='Default Name', max_length=100)),
                ('class_id', models.AutoField(primary_key=True, serialize=False)),
                ('class_period_classroom', models.CharField(max_length=20)),
                ('class_period_course_taught', models.CharField(max_length=20)),
                ('class_period_start_time', models.TimeField()),
                ('class_period_end_time', models.TimeField()),
                ('class_period_Day_of_the_week', models.CharField(max_length=20)),
            ],
        ),
    ]