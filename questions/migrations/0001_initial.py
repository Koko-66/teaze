# Generated by Django 3.2.9 on 2021-12-05 14:29

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=350, unique=True)),
                ('featured_image', cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255, verbose_name='image')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Approved')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(related_name='question', to='categories.Category')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quiz.quiz')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=50, verbose_name='option')),
                ('position', models.IntegerField(verbose_name='position')),
                ('is_correct', models.BooleanField(default=False)),
                ('feedback_correct', models.CharField(default='You are correct!', max_length=200)),
                ('feedback_incorrect', models.CharField(default='Sorry, you got this wrong.', max_length=220)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='questions.question')),
            ],
            options={
                'verbose_name_plural': 'Answer options',
                'ordering': ['position'],
                'unique_together': {('question', 'position'), ('question', 'option')},
            },
        ),
    ]
