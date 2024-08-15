# Generated by Django 5.0.6 on 2024-08-14 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_period', '0002_rename_class_id_class_period_id_and_more'),
        ('courses', '0001_initial'),
        ('teacher', '0002_remove_teacher_teacher_class_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='class_period',
            name='courses',
            field=models.ManyToManyField(to='courses.courses'),
        ),
        migrations.AddField(
            model_name='class_period',
            name='teacher',
            field=models.ManyToManyField(to='teacher.teacher'),
        ),
    ]