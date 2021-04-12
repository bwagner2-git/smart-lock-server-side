# Generated by Django 3.0.3 on 2020-08-18 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20200817_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(blank=True, help_text='mm/dd/yyyy', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='denomination',
            field=models.CharField(choices=[('Catholic', 'Catholic'), ('Baptist', 'Baptist'), ('Nondenominational', 'Nondenominational'), ('Orthodox', 'Orthodox'), ('Prefer not to say', 'Prefer not to say'), ('Angelican', 'Angelican'), ('Methodist', 'Methodist'), ('Lutheran', 'Lutheran'), ('Anabaptist', 'Anabaptist'), ('Adventist', 'Adventist'), ('Assemblies of God', 'Assemblies of God'), ('Penecostalism', 'Penecostalism'), ('Calvinism', 'Calvinism'), ('Presbyterian', 'Presbyterian'), ('Anglican', 'Anglican'), ('Church of God', 'Church of God'), ('Church of the Nazarene', 'Church of the Nazarene'), ('Assyrian', 'Assyrian'), ('Church of England', 'Church of England')], default='Prefer not to say', max_length=32),
        ),
    ]
