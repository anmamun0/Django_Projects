# Generated by Django 5.0.7 on 2024-12-26 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slub',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
