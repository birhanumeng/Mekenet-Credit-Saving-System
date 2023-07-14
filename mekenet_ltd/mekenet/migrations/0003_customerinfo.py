# Generated by Django 4.2.2 on 2023-07-08 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mekenet', '0002_rename_defect_customersaving_undue'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerInfo',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('sex', models.CharField(max_length=50)),
                ('shares', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('membership', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=200)),
            ],
        ),
    ]