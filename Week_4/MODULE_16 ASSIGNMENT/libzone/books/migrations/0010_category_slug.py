# Generated by Django 5.0.7 on 2025-01-05 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
