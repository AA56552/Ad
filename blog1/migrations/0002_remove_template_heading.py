# Generated by Django 4.1.7 on 2023-04-10 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog1", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="template", name="heading",),
    ]
