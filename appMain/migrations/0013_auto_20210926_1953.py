# Generated by Django 3.1.6 on 2021-09-26 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMain', '0012_income'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agency_rent',
            name='total',
        ),
        migrations.AlterField(
            model_name='income',
            name='total_price',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
