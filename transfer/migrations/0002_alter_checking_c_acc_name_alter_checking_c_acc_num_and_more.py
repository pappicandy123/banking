# Generated by Django 4.1.3 on 2022-11-16 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checking',
            name='c_acc_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='checking',
            name='c_acc_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='checking',
            name='c_balance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='checking',
            name='c_bank',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='checking',
            name='c_debit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='checking',
            name='c_purpose',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='saving',
            name='s_acc_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='saving',
            name='s_acc_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='saving',
            name='s_balance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='saving',
            name='s_bank',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='saving',
            name='s_debit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='saving',
            name='s_purpose',
            field=models.TextField(blank=True, null=True),
        ),
    ]