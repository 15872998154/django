# Generated by Django 2.0 on 2018-11-10 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedfox', '0014_auto_20181110_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='novel',
            name='image',
        ),
    ]
