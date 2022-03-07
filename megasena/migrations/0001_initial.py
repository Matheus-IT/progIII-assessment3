# Generated by Django 4.0.3 on 2022-03-07 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Draw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Data')),
                ('ball1', models.IntegerField(verbose_name='Bola1')),
                ('ball2', models.IntegerField(verbose_name='Bola2')),
                ('ball3', models.IntegerField(verbose_name='Bola3')),
                ('ball4', models.IntegerField(verbose_name='Bola4')),
                ('ball5', models.IntegerField(verbose_name='Bola5')),
                ('ball6', models.IntegerField(verbose_name='Bola6')),
            ],
        ),
    ]
