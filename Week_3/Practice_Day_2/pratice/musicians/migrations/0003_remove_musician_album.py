# Generated by Django 5.0.7 on 2024-12-27 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicians', '0002_musician_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musician',
            name='album',
        ),
    ]
