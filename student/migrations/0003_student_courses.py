# Generated by Django 5.0.6 on 2024-08-08 07:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0001_initial"),
        ("student", "0002_rename_phone_number_student_phone_number_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="courses",
            field=models.ManyToManyField(to="courses.courses"),
        ),
    ]
