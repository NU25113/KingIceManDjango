# Generated by Django 3.1.6 on 2021-09-28 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMain', '0014_remove_list_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cost',
            old_name='sum_price',
            new_name='price',
        ),
    ]