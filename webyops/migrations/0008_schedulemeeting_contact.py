# Generated by Django 4.1.7 on 2023-10-17 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webyops", "0007_schedulemeeting"),
    ]

    operations = [
        migrations.AddField(
            model_name="schedulemeeting",
            name="contact",
            field=models.CharField(max_length=20, null=True),
        ),
    ]
