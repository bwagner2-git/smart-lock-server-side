# Generated by Django 3.0.3 on 2020-08-15 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200811_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='relationship_status',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('in a relationship', 'in a relationship'), ("it's complicated", "it's complicated")], default='prefer not to say', max_length=32),
        ),
    ]
