# Generated by Django 2.2.9 on 2020-01-23 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='review/')),
                ('date', models.DateField(auto_now=True)),
                ('rating', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]
