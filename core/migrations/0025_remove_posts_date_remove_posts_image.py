# Generated by Django 4.2.7 on 2023-11-08 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_alter_posts_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='date',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='image',
        ),
    ]
