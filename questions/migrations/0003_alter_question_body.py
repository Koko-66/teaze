# Generated by Django 3.2.9 on 2021-12-05 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20211205_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='body',
            field=models.CharField(max_length=350, unique=True),
        ),
    ]
