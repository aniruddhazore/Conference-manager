# Generated by Django 4.2.3 on 2023-10-12 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0018_remove_reviewer_areaofinterest'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='otherauthors',
            field=models.CharField(max_length=125, null=True),
        ),
    ]
