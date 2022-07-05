# Generated by Django 4.0.5 on 2022-07-05 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bridge',
            old_name='actor_id',
            new_name='actor',
        ),
        migrations.RenameField(
            model_name='bridge',
            old_name='movies_id',
            new_name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(through='movie.Bridge', to='movie.actor'),
        ),
    ]
