# Generated by Django 4.1.7 on 2023-10-26 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webyops", "0011_contactusform"),
    ]

    operations = [
        migrations.CreateModel(
            name="todolist",
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
                ("task", models.CharField(max_length=500)),
                ("taskdetails", models.CharField(max_length=500)),
                ("checkmark", models.CharField(max_length=20)),
                ("comments", models.TextField()),
                ("completed_on", models.CharField(max_length=20)),
            ],
        ),
    ]
