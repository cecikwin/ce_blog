# Generated by Django 3.2.7 on 2021-10-25 13:33

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20210927_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='text',
            field=martor.models.MartorField(),
        ),
    ]
