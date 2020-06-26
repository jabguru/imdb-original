# Generated by Django 2.2.5 on 2020-06-22 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cast',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='MovieLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('DW', 'DOWNLOAD_LINK'), ('W', 'WATCH_LINK')], max_length=1)),
                ('links', models.URLField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_watch_link', to='movie.Movie')),
            ],
        ),
    ]