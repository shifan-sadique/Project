# Generated by Django 3.2 on 2021-05-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0035_razorpay_razorpay_order_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sd_id', models.IntegerField()),
                ('sd_name', models.CharField(max_length=50)),
                ('leave_type', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('reason', models.CharField(max_length=250)),
                ('half_day', models.BooleanField(default=False)),
            ],
        ),
    ]
