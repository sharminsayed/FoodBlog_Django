# Generated by Django 2.2.9 on 2020-01-23 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0010_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('rating', models.IntegerField()),
                ('description', models.TextField()),
                ('ingredient', models.IntegerField()),
            ],
        ),
    ]
