# Generated by Django 2.2.2 on 2020-12-06 10:31

from django.db import migrations, models
import tracker.models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0008_auto_20201206_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasecategory',
            name='id',
        ),
        migrations.AddField(
            model_name='purchasecategory',
            name='category_created_datetime',
            field=models.DateTimeField(default=tracker.models.current_datetime, verbose_name='Category Created DateTime'),
        ),
        migrations.AlterField(
            model_name='purchasecategory',
            name='category',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Category'),
        ),
    ]
