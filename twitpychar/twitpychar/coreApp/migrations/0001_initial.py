# Generated by Django 4.1.4 on 2023-01-02 08:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Контент')),
                ('postDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='date')),
                ('postImg', models.CharField(blank=True, max_length=500, null=True, verbose_name='image')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
        ),
    ]