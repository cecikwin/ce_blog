# Generated by Django 3.2.7 on 2021-11-07 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_articles_outline'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/%Y%m%d/'),
        ),
    ]
