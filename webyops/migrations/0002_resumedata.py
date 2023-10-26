# Generated by Django 4.1.7 on 2023-10-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webyops", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ResumeData",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("phone", models.CharField(max_length=15)),
                ("message", models.TextField()),
                ("resume", models.TextField()),
            ],
        ),
    ]
