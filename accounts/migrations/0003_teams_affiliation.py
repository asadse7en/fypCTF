# Generated by Django 4.2 on 2023-05-17 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_teams_first_name_teams_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='affiliation',
            field=models.CharField(default='Student', max_length=500),
        ),
    ]
