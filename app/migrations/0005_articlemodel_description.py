# Generated by Django 2.2.7 on 2020-08-02 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200802_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemodel',
            name='description',
            field=models.TextField(null=True, verbose_name='概要'),
        ),
    ]
