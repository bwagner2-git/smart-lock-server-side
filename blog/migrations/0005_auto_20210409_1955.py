# Generated by Django 3.0.3 on 2021-04-10 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200912_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='sponsored_post',
        ),
        migrations.DeleteModel(
            name='post',
        ),
    ]