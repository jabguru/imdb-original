# Generated by Django 2.2.5 on 2020-06-25 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20200624_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('english', 'ENGLISH'), ('german', 'GERMAN'), ('russian', 'RUSSIAN')], max_length=2),
        ),
    ]