# Generated by Django 3.0.3 on 2020-08-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200820_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, max_length=600),
        ),
        migrations.AlterField(
            model_name='sponsored_post',
            name='content',
            field=models.TextField(blank=True, max_length=600),
        ),
    ]
