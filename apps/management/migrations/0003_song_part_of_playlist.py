# Generated by Django 2.0.1 on 2018-10-20 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20181020_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='part_of_playlist',
            field=models.ManyToManyField(blank=True, to='management.Playlist'),
        ),
    ]
