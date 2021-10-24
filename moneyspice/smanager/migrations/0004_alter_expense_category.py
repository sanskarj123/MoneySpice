# Generated by Django 3.2.8 on 2021-10-24 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smanager', '0003_auto_20211024_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('Food', 'FOD'), ('Shopping', 'SHP'), ('Transport', 'TRT'), ('Fuel', 'FUL'), ('Entertainment', 'ENT'), ('Health', 'HLT'), ('Bills', 'BIL'), ('Others', 'OTH')], default='OTH', max_length=20, verbose_name='Expense Category'),
        ),
    ]
