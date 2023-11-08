# Generated by Django 4.2.7 on 2023-11-08 09:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_singlecomments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('work_place', models.CharField(max_length=255)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
