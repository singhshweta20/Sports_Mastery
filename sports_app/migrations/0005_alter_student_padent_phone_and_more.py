# Generated by Django 4.1.7 on 2023-03-15 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports_app', '0004_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='padent_phone',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_phone',
            field=models.IntegerField(max_length=10),
        ),
    ]
