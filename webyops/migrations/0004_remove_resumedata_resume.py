# Generated by Django 4.1.7 on 2023-10-16 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("webyops", "0003_candidate_training"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="resumedata",
            name="resume",
        ),
    ]
