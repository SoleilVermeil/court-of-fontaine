# Generated by Django 4.2.7 on 2023-11-30 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_substatfield_remove_artifact_substats"),
    ]

    operations = [
        migrations.AddField(
            model_name="artifact",
            name="substat",
            field=models.ForeignKey(
                default=0, on_delete=django.db.models.deletion.CASCADE, to="app.substat"
            ),
            preserve_default=False,
        ),
    ]
