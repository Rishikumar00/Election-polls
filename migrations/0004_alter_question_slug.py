# Generated by Django 5.0.6 on 2024-06-20 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_question_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]
