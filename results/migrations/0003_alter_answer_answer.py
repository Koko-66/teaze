# Generated by Django 3.2.9 on 2022-02-07 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_auto_20220206_2321'),
        ('results', '0002_alter_answer_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='answer_option', to='questions.option'),
        ),
    ]
