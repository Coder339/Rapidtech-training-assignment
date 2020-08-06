# Generated by Django 3.0.9 on 2020-08-06 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0002_traineeinfo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='traineeinfo',
            name='trainer',
            field=models.CharField(editable=False, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='traineeinfo',
            name='address_line2',
            field=models.CharField(editable=False, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='traineeinfo',
            name='rate',
            field=models.FloatField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='traineeinfo',
            name='t_e_d',
            field=models.DateField(editable=False, verbose_name='Training End Date'),
        ),
        migrations.AlterField(
            model_name='traineeinfo',
            name='t_s_d',
            field=models.DateField(editable=False, verbose_name='Training Start Date'),
        ),
    ]
