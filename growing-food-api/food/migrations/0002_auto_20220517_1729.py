# Generated by Django 3.1.2 on 2022-05-17 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VegetableType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='vegetable',
            name='veg_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.vegetabletype'),
        ),
    ]
