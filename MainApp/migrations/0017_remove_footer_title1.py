# Generated by Django 2.2.9 on 2020-01-23 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0016_remove_footer_image2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footer',
            name='title1',
        ),
    ]
