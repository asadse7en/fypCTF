# Generated by Django 4.2 on 2023-05-09 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='first_name',
            field=models.CharField(default='lastname', max_length=50),
        ),
        migrations.AddField(
            model_name='teams',
            name='last_name',
            field=models.CharField(default='lastname', max_length=50),
        ),
    ]
