# Generated by Django 3.0.9 on 2020-08-05 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Financials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_Rate', models.FloatField(blank=True, null=True)),
                ('pay_Rate', models.FloatField(blank=True, null=True)),
                ('tax', models.FloatField(blank=True, null=True)),
                ('margin', models.FloatField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Financials',
            },
        ),
    ]
