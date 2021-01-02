# Generated by Django 2.2.2 on 2021-01-01 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0017_auto_20210101_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account_to_use',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profiles_1', to='tracker.Account', verbose_name='Account to Use'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='credit_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profiles_2', to='tracker.Account', verbose_name='Credit Account'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='debit_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profiles_3', to='tracker.Account', verbose_name='Debit Account'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='secondary_debit_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profiles_4', to='tracker.Account', verbose_name='Secondary Debit Account'),
        ),
    ]
