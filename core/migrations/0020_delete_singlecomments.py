# Generated by Django 4.2.6 on 2023-11-05 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_rename_hed_img_singlenews_hed2_img_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SingleComments',
        ),
    ]
