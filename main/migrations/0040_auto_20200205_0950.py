# Generated by Django 3.0.2 on 2020-02-05 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_auto_20200205_0932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myorder',
            old_name='imię',
            new_name='imie',
        ),
    ]
