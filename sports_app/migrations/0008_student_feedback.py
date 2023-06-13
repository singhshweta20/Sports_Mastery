# Generated by Django 4.1.7 on 2023-03-29 16:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sports_app', '0007_user_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_id', models.CharField(default=None, max_length=40)),
                ('c_id', models.CharField(default=None, max_length=40)),
                ('feedback_text', models.TextField()),
                ('rating', models.CharField(max_length=6)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
