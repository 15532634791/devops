# Generated by Django 4.2 on 2023-09-11 08:30

import APPS.ProjectManage.DeploymentBuild.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeploymentBuild', '0002_alter_deploybuildmodel_jarbuildcommand'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeployBuildFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=APPS.ProjectManage.DeploymentBuild.models.custom_upload_to)),
            ],
        ),
    ]
