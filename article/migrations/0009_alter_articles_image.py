# Generated by Django 3.2.7 on 2021-11-07 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_alter_articles_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='封面图'),
        ),
    ]
