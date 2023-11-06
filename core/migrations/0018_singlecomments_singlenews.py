# Generated by Django 4.2.6 on 2023-11-05 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_navbarstart'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='user_info/')),
                ('user_name', models.CharField(max_length=255)),
                ('comment', models.TextField()),
                ('button', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SingleNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='user_info/')),
                ('date', models.DateField()),
                ('header', models.CharField(max_length=255)),
                ('paragraph', models.TextField()),
                ('hed_img', models.ImageField(upload_to='user_info/')),
            ],
        ),
    ]