# Generated by Django 2.1.2 on 2018-10-19 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='车辆编号')),
                ('car_brand', models.CharField(max_length=32, verbose_name='车牌号')),
                ('car_broken_part', models.CharField(max_length=32, verbose_name='损坏部位')),
            ],
            options={
                'verbose_name_plural': '车辆管理',
            },
        ),
        migrations.CreateModel(
            name='FixList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='订单编号')),
                ('begin_fix_time', models.DateTimeField(auto_now=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carfix.Car')),
            ],
            options={
                'verbose_name_plural': '维修列表',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('goods_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='配件编号')),
                ('goods_name', models.CharField(max_length=32, verbose_name='配件名称')),
                ('goods_price', models.IntegerField(verbose_name='配件价格')),
                ('goods_desciption', models.CharField(max_length=32, verbose_name='配件描述')),
                ('goods_count', models.IntegerField(verbose_name='配件数量')),
            ],
            options={
                'verbose_name_plural': '配件管理',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=32, verbose_name='用户姓名')),
                ('user_tel', models.CharField(max_length=32, verbose_name='用户联系方式')),
                ('user_addr', models.CharField(max_length=32, verbose_name='地址')),
                ('user_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carfix.Car')),
            ],
            options={
                'verbose_name_plural': '用户管理',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('worker_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='工号')),
                ('worker_name', models.CharField(max_length=32, verbose_name='姓名')),
                ('worker_tel', models.CharField(max_length=32, verbose_name='联系方式')),
                ('worker_addr', models.CharField(max_length=32, verbose_name='地址')),
                ('worker_positon', models.CharField(max_length=32, verbose_name='职务')),
                ('worker_type', models.IntegerField(choices=[(1, '高级员工'), (2, '中级员工'), (3, '初级员工')], verbose_name='员工类型')),
            ],
            options={
                'verbose_name_plural': '员工管理',
            },
        ),
        migrations.AddField(
            model_name='fixlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carfix.User'),
        ),
        migrations.AddField(
            model_name='fixlist',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carfix.Worker'),
        ),
        migrations.AddField(
            model_name='car',
            name='use_goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carfix.Goods'),
        ),
    ]
