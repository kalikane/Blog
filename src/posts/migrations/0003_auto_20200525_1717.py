# Generated by Django 3.0.6 on 2020-05-25 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_picture',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(upload_to=''),
        ),
    ]
