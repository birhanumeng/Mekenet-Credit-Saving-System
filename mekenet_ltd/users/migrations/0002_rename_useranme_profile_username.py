# Generated by Django 4.2.2 on 2023-07-11 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='useranme',
            new_name='username',
        ),
    ]