# Generated by Django 3.2 on 2021-06-06 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0046_auto_20210605_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='closed',
            field=models.DateField(null=True),
        ),
    ]
