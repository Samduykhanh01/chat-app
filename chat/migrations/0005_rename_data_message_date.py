# Generated by Django 4.2.9 on 2024-01-31 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='data',
            new_name='date',
        ),
    ]