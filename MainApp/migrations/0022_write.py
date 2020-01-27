# Generated by Django 2.2.9 on 2020-01-27 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0021_auto_20200127_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Write',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('rating', models.IntegerField()),
                ('level', models.CharField(max_length=100)),
                ('list', models.CharField(max_length=100)),
                ('descrip', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
