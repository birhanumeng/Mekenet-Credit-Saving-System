# Generated by Django 4.2.2 on 2023-07-12 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
