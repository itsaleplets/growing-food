# Generated by Django 3.1.2 on 2022-06-15 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_auto_20220615_0200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vegetable',
            name='user',
        ),
    ]