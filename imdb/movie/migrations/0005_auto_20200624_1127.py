# Generated by Django 2.2.5 on 2020-06-24 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20200622_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('action', 'ACTION'), ('drama', 'DRAMA'), ('comedy', 'COMEDY'), ('romance', 'ROMANCE')], max_length=10),
        ),
    ]
