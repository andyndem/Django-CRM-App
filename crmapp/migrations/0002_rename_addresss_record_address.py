# Generated by Django 4.2 on 2023-04-22 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='addresss',
            new_name='address',
        ),
    ]
