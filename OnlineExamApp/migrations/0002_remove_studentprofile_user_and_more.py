# Generated by Django 5.1.7 on 2025-04-03 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineExamApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='teacherprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='AdminProfile',
        ),
        migrations.DeleteModel(
            name='StudentProfile',
        ),
        migrations.DeleteModel(
            name='TeacherProfile',
        ),
    ]
