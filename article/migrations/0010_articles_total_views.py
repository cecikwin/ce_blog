# Generated by Django 3.2.7 on 2022-04-10 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_alter_articles_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='total_views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
