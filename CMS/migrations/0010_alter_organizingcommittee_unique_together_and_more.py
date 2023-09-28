# Generated by Django 4.2.3 on 2023-09-22 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0009_advisorycommittee_insititute'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='organizingcommittee',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='organizingcommittee',
            name='conferenceTitle',
        ),
        migrations.AddField(
            model_name='conference',
            name='committee_images',
            field=models.FileField(null=True, upload_to='desktop'),
        ),
        migrations.AddField(
            model_name='conference',
            name='conference_images',
            field=models.FileField(null=True, upload_to='desktop'),
        ),
        migrations.DeleteModel(
            name='AdvisoryCommittee',
        ),
        migrations.DeleteModel(
            name='OrganizingCommittee',
        ),
    ]
