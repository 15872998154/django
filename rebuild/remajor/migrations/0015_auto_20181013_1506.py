# Generated by Django 2.1.2 on 2018-10-13 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remajor', '0014_student'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': '学生管理'},
        ),
        migrations.AlterField(
            model_name='rebuild',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remajor.Course', verbose_name='重修课程'),
        ),
    ]
