# Generated by Django 2.0.13 on 2021-02-18 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_data',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='published_data',
            new_name='published_date',
        ),
    ]
