# Generated by Django 2.2.2 on 2020-12-07 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0023_auto_20201207_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='item',
            field=models.CharField(max_length=100, verbose_name='Item(s)'),
        ),
    ]
