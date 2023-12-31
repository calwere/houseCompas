# Generated by Django 4.2.2 on 2023-06-28 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campass', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facilities',
            name='latitude',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
        migrations.AlterField(
            model_name='facilities',
            name='longitude',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
        migrations.AlterField(
            model_name='house',
            name='latitude',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
        migrations.AlterField(
            model_name='house',
            name='longitude',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
    ]
