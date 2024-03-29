# Generated by Django 4.2 on 2023-09-25 07:15

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeploymentBuild', '0005_rename_jarbuildstderr_deploybuildmodel_jarbuildcommandstdout_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deploybuildmodel',
            name='jarBuildImageAddress',
            field=models.TextField(default=builtins.print),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deploybuildmodel',
            name='jarBuildStatus',
            field=models.CharField(default=builtins.print, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deploybuildmodel',
            name='jarBuildUser',
            field=models.CharField(default=builtins.print, max_length=255),
            preserve_default=False,
        ),
    ]
