# Generated by Django 3.1.4 on 2020-12-29 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop1', '0002_auto_20201227_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]
