# Generated by Django 2.1.2 on 2018-10-11 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('remajor', '0008_delete_rebuild'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=32, verbose_name='选修课程')),
            ],
        ),
        migrations.CreateModel(
            name='Rebuild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.CharField(max_length=12, verbose_name='学号')),
                ('stu_name', models.CharField(max_length=32, verbose_name='姓名')),
                ('profession', models.CharField(max_length=32, verbose_name='专业')),
                ('choice', models.IntegerField(choices=[(1, '普通'), (2, '刷分')], verbose_name='重修方式')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remajor.Course')),
            ],
            options={
                'verbose_name_plural': '学生重修管理',
            },
        ),
    ]
