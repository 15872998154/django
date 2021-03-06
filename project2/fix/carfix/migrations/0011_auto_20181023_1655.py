# Generated by Django 2.0.2 on 2018-10-23 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carfix', '0010_auto_20181023_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20, verbose_name='用户名')),
                ('only_record', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='worker',
            name='worker_type',
            field=models.IntegerField(choices=[(1, '高级员工'), (2, '中级员工'), (3, '初级员工')], default=1, verbose_name='员工类型'),
        ),
    ]
