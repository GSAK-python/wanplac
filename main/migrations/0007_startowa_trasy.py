# Generated by Django 3.0.2 on 2020-01-23 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_startowa'),
    ]

    operations = [
        migrations.AddField(
            model_name='startowa',
            name='trasy',
            field=models.TextField(default=''),
        ),
    ]