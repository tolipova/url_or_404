# Generated by Django 4.2.6 on 2023-11-05 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_singlecomments_singlenews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='singlenews',
            old_name='hed_img',
            new_name='hed2_img',
        ),
        migrations.RenameField(
            model_name='singlenews',
            old_name='paragraph',
            new_name='hed2_paragraph',
        ),
        migrations.AddField(
            model_name='singlenews',
            name='header2',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='singlenews',
            name='header3',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='singlenews',
            name='hed3_img',
            field=models.ImageField(default=11, upload_to='user_info/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='singlenews',
            name='hed3_paragraph',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='singlenews',
            name='paragraph1',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='singlenews',
            name='paragraph2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
