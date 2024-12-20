# Generated by Django 4.1 on 2024-12-16 17:02

import cinema.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to=cinema.models.movie_image_file_path
            ),
        ),
    ]
