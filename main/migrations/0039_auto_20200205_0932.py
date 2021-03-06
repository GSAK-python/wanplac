# Generated by Django 3.0.2 on 2020-02-05 08:32

from django.db import migrations, models
import main.templatetags.kod_generator


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_auto_20200204_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myorder',
            name='data',
            field=models.IntegerField(choices=[(0, '05-02-2020'), (1, '06-02-2020'), (2, '07-02-2020'), (3, '08-02-2020'), (4, '09-02-2020'), (5, '10-02-2020'), (6, '11-02-2020')]),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='kod',
            field=models.CharField(default=main.templatetags.kod_generator.random_string, max_length=6),
        ),
    ]
