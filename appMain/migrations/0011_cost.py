# Generated by Django 3.1.6 on 2021-09-17 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMain', '0010_budget'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum_price', models.IntegerField(blank=True, null=True)),
                ('staff', models.CharField(max_length=100)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Name_budget', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='appMain.budget')),
            ],
            options={
                'verbose_name_plural': 'ข้อมูลค่าใช้จ่าย',
            },
        ),
    ]