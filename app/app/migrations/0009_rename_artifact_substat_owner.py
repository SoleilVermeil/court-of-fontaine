# Generated by Django 4.2.7 on 2023-12-01 09:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0008_alter_artifact_equiptype"),
    ]

    operations = [
        migrations.RenameField(
            model_name="substat",
            old_name="artifact",
            new_name="owner",
        ),
    ]
