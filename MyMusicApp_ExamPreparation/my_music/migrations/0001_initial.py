# Generated by Django 3.2.19 on 2023-06-20 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=30, unique=True)),
                ('artist', models.CharField(max_length=30)),
                ('genre', models.CharField(choices=[('1', 'Pop Music'), ('2', 'Jazz Music'), ('3', 'R&B Music'), ('4', 'Rock Music'), ('5', 'Country Music'), ('6', 'Dance Music'), ('7', 'Hip Hop Music'), ('8', 'Other')], max_length=30)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveIntegerField()),
            ],
        ),
    ]