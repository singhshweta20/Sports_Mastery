# Generated by Django 4.2.2 on 2023-06-23 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sports_app", "0015_event_event_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="PredictedHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("game", models.CharField(max_length=255)),
                ("team_1", models.CharField(max_length=255)),
                ("team_2", models.CharField(max_length=255)),
                ("result", models.CharField(max_length=255)),
                ("predicted_on", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]