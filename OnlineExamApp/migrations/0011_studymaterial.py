# Generated by Django 5.1.7 on 2025-04-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineExamApp', '0010_alter_exam_created_by_alter_result_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('file', models.FileField(upload_to='materials/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
