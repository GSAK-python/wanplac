# Generated by Django 3.0.2 on 2020-02-04 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20200203_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jedynki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kajak_jedynka', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='equipmenttochose',
            name='ilosc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='data',
            field=models.IntegerField(choices=[(0, '04-02-2020'), (1, '05-02-2020'), (2, '06-02-2020'), (3, '07-02-2020'), (4, '08-02-2020'), (5, '09-02-2020'), (6, '10-02-2020')]),
        ),
    ]
