# Generated by Django 5.0.4 on 2024-04-23 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='content_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='posts',
            old_name='content_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='posts',
            old_name='content_title',
            new_name='title',
        ),
    ]