# Generated by Django 2.1.4 on 2018-12-26 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='author',
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]
