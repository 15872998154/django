# Generated by Django 2.1.2 on 2018-10-11 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remajor', '0011_course_rebuild'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rebuild',
            name='course',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Rebuild',
        ),
    ]
