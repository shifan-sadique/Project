# Generated by Django 3.2 on 2021-06-05 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0045_alter_notification_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='notification',
            name='temp',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
