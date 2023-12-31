# Generated by Django 4.2.2 on 2023-11-25 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campass', '0002_alter_facilities_latitude_alter_facilities_longitude_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={},
        ),
    ]
