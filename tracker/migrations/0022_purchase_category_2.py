# Generated by Django 2.2.2 on 2020-12-07 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0021_auto_20201207_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='category_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_2', to='tracker.PurchaseCategory', verbose_name='Category 2'),
        ),
    ]
