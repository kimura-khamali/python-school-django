# Generated by Django 5.0.6 on 2024-08-19 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_remove_courses_course_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_instructor',
            field=models.CharField(default='Default name', max_length=20),
        ),
    ]