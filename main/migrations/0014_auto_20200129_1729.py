# Generated by Django 3.0.2 on 2020-01-29 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_myorder_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myorder',
            name='user',
            field=models.CharField(default='', max_length=140),
        ),
    ]
