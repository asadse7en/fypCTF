# Generated by Django 4.2 on 2023-06-19 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0012_remove_challengessolvedby_first_blood'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengessolvedby',
            name='first_blood',
            field=models.BooleanField(default=False),
        ),
    ]
