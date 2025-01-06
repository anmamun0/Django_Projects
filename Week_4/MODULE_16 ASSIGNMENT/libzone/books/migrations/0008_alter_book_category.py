# Generated by Django 5.0.7 on 2025-01-05 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='books', to='books.category'),
        ),
    ]
