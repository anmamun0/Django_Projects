# Generated by Django 5.0.7 on 2024-12-26 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_slub'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slub',
            new_name='slug',
        ),
    ]