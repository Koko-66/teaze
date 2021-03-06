# Generated by Django 3.2.9 on 2021-12-05 14:29

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('featured_image', cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, verbose_name='image')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(related_name='quiz', to='categories.Category')),
            ],
            options={
                'verbose_name_plural': 'Quizzes',
            },
        ),
    ]
