# Generated by Django 2.2.9 on 2020-01-23 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0013_auto_20200123_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
