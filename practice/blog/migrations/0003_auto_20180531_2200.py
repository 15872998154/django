# Generated by Django 2.0.5 on 2018-05-31 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180528_1437'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='readnum',
            options={'verbose_name': '博客统计', 'verbose_name_plural': '博客统计'},
        ),
    ]
