# Generated by Django 3.2.9 on 2021-12-23 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import phonenumber_field.modelfields
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('supplier_full_name', models.CharField(max_length=100, verbose_name='Supplier Full Name')),
                ('supplier_address', models.CharField(max_length=100, verbose_name='Supplier Address')),
                ('supplier_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('supplier_email', models.EmailField(max_length=254, unique=True, verbose_name='Supplier Email')),
                ('supplier_zip_code', models.CharField(max_length=10)),
                ('supplier_country', django_countries.fields.CountryField(max_length=2)),
                ('supplier_fax', models.BigIntegerField(blank=True, null=True, verbose_name='Supplier Fax')),
                ('supplier_previous_balance', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Supplier Previous Balance')),
                ('supplier_ledger', models.ManyToManyField(to='customers.Ledger', verbose_name='Supplier Ledger')),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
            },
        ),
        migrations.CreateModel(
            name='HistoricalSupplier',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('supplier_full_name', models.CharField(max_length=100, verbose_name='Supplier Full Name')),
                ('supplier_address', models.CharField(max_length=100, verbose_name='Supplier Address')),
                ('supplier_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('supplier_email', models.EmailField(db_index=True, max_length=254, verbose_name='Supplier Email')),
                ('supplier_zip_code', models.CharField(max_length=10)),
                ('supplier_country', django_countries.fields.CountryField(max_length=2)),
                ('supplier_fax', models.BigIntegerField(blank=True, null=True, verbose_name='Supplier Fax')),
                ('supplier_previous_balance', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Supplier Previous Balance')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Supplier',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
