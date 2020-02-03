# Generated by Django 3.0.2 on 2020-02-03 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0031_delete_myorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imię', models.CharField(max_length=128)),
                ('nazwisko', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('data', models.IntegerField(choices=[(0, '03-02-2020'), (1, '04-02-2020'), (2, '05-02-2020'), (3, '06-02-2020'), (4, '07-02-2020'), (5, '08-02-2020'), (6, '09-02-2020')])),
                ('trasa', models.IntegerField(choices=[(0, 'Krutyń - Młyn (3km)'), (1, 'Krutyń - Rosocha (6km)'), (2, 'Krutyń - Ukta (13km)'), (3, 'Krutyń - Jezioro Mokre - Krutyń (10km)')])),
                ('godzina', models.IntegerField(choices=[(0, '9:00'), (1, '9:15'), (2, '9:30'), (3, '9:45'), (4, '10:00'), (5, '10:15'), (5, '10:30'), (7, '10:45'), (8, '11:00'), (9, '11:15'), (10, '11:30'), (11, '11:45'), (12, '12:00')])),
                ('sprzęt', models.ManyToManyField(to='main.EquipmentToChose')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
