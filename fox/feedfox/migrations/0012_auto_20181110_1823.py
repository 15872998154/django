# Generated by Django 2.0 on 2018-11-10 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedfox', '0011_auto_20181110_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novel',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
