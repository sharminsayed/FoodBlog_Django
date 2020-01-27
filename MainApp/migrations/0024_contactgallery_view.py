# Generated by Django 2.2.9 on 2020-01-27 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0023_delete_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactgallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='contact/')),
                ('image2', models.ImageField(upload_to='contact/')),
                ('image3', models.ImageField(upload_to='contact/')),
                ('image4', models.ImageField(upload_to='contact/')),
                ('image5', models.ImageField(upload_to='contact/')),
                ('image6', models.ImageField(upload_to='contact/')),
            ],
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='view/')),
            ],
        ),
    ]
