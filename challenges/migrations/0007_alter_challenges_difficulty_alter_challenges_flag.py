# Generated by Django 4.2 on 2023-05-12 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0006_challenges_difficulty_challenges_solve_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='difficulty',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='challenges',
            name='flag',
            field=models.CharField(max_length=500),
        ),
    ]
