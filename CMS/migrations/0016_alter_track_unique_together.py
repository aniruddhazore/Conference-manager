# Generated by Django 4.2.3 on 2023-09-29 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0015_rename_description_track_subdomains'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='track',
            unique_together={('conference', 'title')},
        ),
    ]
