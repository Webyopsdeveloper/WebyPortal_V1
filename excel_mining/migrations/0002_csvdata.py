# Generated by Django 4.1.7 on 2023-10-11 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("excel_mining", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CsvData",
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
                ("name", models.CharField(max_length=500)),
                ("csv_file", models.TextField()),
            ],
        ),
    ]
