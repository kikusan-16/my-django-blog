# Generated by Django 2.2.7 on 2020-08-10 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_mediamodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MediaModel',
            new_name='Media',
        ),
    ]