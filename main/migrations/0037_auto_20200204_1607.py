# Generated by Django 3.0.2 on 2020-02-04 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_delete_jedynki'),
    ]

    operations = [
        migrations.AddField(
            model_name='myorder',
            name='eoli',
            field=models.IntegerField(blank=True, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0),
        ),
        migrations.AddField(
            model_name='myorder',
            name='family',
            field=models.IntegerField(blank=True, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')], default=0),
        ),
        migrations.AddField(
            model_name='myorder',
            name='finder',
            field=models.IntegerField(blank=True, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24')], default=0),
        ),
        migrations.AddField(
            model_name='myorder',
            name='jett',
            field=models.IntegerField(blank=True, choices=[(0, '0'), (1, '1')], default=0),
        ),
        migrations.AddField(
            model_name='myorder',
            name='kanu',
            field=models.IntegerField(blank=True, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')], default=0),
        ),
        migrations.AddField(
            model_name='myorder',
            name='koga',
            field=models.IntegerField(blank=True, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')], default=0),
        ),
        migrations.AddField(
            model_name='myorder',
            name='protour',
            field=models.IntegerField(blank=True, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')], default=0),
        ),
        migrations.AddField(
            model_name='myorder',
            name='traper',
            field=models.IntegerField(blank=True, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')], default=0),
        ),
    ]
