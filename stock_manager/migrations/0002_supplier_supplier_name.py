# Generated by Django 4.0.6 on 2022-08-19 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='supplier_name',
            field=models.CharField(default='Default', max_length=100),
        ),
    ]
