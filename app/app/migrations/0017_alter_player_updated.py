# Generated by Django 4.2.7 on 2024-01-03 15:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0016_alter_player_updated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
