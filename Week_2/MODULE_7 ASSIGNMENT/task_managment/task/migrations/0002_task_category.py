# Generated by Django 5.0.7 on 2024-12-18 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_category_tasks'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ManyToManyField(to='category.category'),
        ),
    ]
