# Generated by Django 2.0 on 2018-11-04 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('feedfox', '0003_delete_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=60)),
                ('content', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Novel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('novel_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='novel_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedfox.Novel'),
        ),
    ]
