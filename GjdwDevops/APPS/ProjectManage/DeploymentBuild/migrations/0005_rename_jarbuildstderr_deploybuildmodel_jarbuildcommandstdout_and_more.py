# Generated by Django 4.2 on 2023-09-22 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DeploymentBuild', '0004_deploybuildmodel_jarbuildreturncode_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deploybuildmodel',
            old_name='jarBuildStderr',
            new_name='jarBuildCommandStdout',
        ),
        migrations.RemoveField(
            model_name='deploybuildmodel',
            name='jarBuildReturnCode',
        ),
        migrations.RemoveField(
            model_name='deploybuildmodel',
            name='jarBuildStdout',
        ),
    ]
