# Generated by Django 3.1 on 2020-09-05 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='duration',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='cardtocard',
            name='duration',
            field=models.TimeField(null=True),
        ),
    ]
