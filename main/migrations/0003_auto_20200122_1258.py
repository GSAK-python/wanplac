# Generated by Django 3.0.2 on 2020-01-22 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200122_1255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='hour',
            new_name='data',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='Imię',
            new_name='imię',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='surname',
            new_name='nazwisko',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='equipment',
            new_name='sprzęt',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='route',
            new_name='trasa',
        ),
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
    ]
