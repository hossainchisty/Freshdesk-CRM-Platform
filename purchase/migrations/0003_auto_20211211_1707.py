# Generated by Django 3.2.5 on 2021-12-11 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_auto_20211130_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='invoice_number',
            field=models.CharField(default='8071', max_length=4, unique=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='purchase_id',
            field=models.CharField(default='32378222078', max_length=4, unique=True),
        ),
    ]