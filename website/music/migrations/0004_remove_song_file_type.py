# Generated by Django 3.0.5 on 2020-05-31 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20200524_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='file_type',
        ),
    ]
