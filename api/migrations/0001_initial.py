# Generated by Django 4.2.1 on 2023-05-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jadwal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.CharField(max_length=20)),
                ('imsyak', models.TimeField()),
                ('subuh', models.TimeField()),
                ('terbit', models.TimeField()),
                ('duha', models.TimeField()),
                ('zuhur', models.TimeField()),
                ('asar', models.TimeField()),
                ('magrib', models.TimeField()),
                ('isya', models.TimeField()),
            ],
            options={
                'db_table': 'jadwal',
            },
        ),
    ]
