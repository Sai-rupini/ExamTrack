# Generated by Django 5.1.7 on 2025-04-05 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineExamApp', '0008_alter_question_correct_option'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='option1',
            new_name='option_a',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='option2',
            new_name='option_b',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='option3',
            new_name='option_c',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='option4',
            new_name='option_d',
        ),
    ]
