# Generated by Django 5.0.7 on 2025-01-06 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_category_slug'),
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='book',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='viewer', to='books.book'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.IntegerField(choices=[(1, 'Deposite'), (2, 'Return'), (3, 'Purchase')], null=True),
        ),
    ]
