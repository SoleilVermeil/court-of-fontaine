# Generated by Django 4.2.7 on 2023-11-30 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "uid",
                    models.CharField(max_length=9, primary_key=True, serialize=False),
                ),
                ("nickname", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Character",
            fields=[
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=20)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.player"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Artifact",
            fields=[
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                (
                    "equiptype",
                    models.CharField(
                        choices=[
                            ("EQUIP_BRACER", "Flower"),
                            ("EQUIP_NECKLACE", "Feather"),
                            ("EQUIP_SHOES", "Sands"),
                            ("EQUIP_RING", "Goblet"),
                            ("EQUIP_DRESS", "Circlet"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "FIGHT_PROP_BASE_ATTACK",
                    models.DecimalField(
                        decimal_places=1, max_digits=4, verbose_name="Base ATK"
                    ),
                ),
                (
                    "FIGHT_PROP_HP",
                    models.DecimalField(
                        decimal_places=1, max_digits=4, verbose_name="Flat HP"
                    ),
                ),
                (
                    "FIGHT_PROP_ATTACK",
                    models.DecimalField(
                        decimal_places=1, max_digits=4, verbose_name="Flat ATK"
                    ),
                ),
                (
                    "FIGHT_PROP_DEFENSE",
                    models.DecimalField(
                        decimal_places=1, max_digits=4, verbose_name="Flat DEF"
                    ),
                ),
                (
                    "FIGHT_PROP_HP_PERCENT",
                    models.DecimalField(
                        decimal_places=1, max_digits=4, verbose_name="HP%"
                    ),
                ),
                (
                    "FIGHT_PROP_ATTACK_PERCENT",
                    models.DecimalField(
                        decimal_places=1, max_digits=4, verbose_name="ATK%"
                    ),
                ),
                (
                    "FIGHT_PROP_DEFENSE_PERCENT",
                    models.DecimalField(
                        decimal_places=1, max_digits=4, verbose_name="DEF%"
                    ),
                ),
                (
                    "FIGHT_PROP_CRITICAL",
                    models.DecimalField(
                        decimal_places=1, max_digits=4, verbose_name="Crit RATE"
                    ),
                ),
                (
                    "FIGHT_PROP_CRITICAL_HURT",
                    models.DecimalField(
                        decimal_places=1, max_digits=4, verbose_name="Crit DMG"
                    ),
                ),
                (
                    "FIGHT_PROP_CHARGE_EFFICIENCY",
                    models.DecimalField(
                        decimal_places=1, max_digits=4, verbose_name="Energy Recharge"
                    ),
                ),
                (
                    "FIGHT_PROP_HEAL_ADD",
                    models.DecimalField(
                        decimal_places=1, max_digits=4, verbose_name="Healing Bonus"
                    ),
                ),
                (
                    "FIGHT_PROP_ELEMENT_MASTERY",
                    models.DecimalField(
                        decimal_places=1, max_digits=4, verbose_name="Elemental Mastery"
                    ),
                ),
                (
                    "FIGHT_PROP_PHYSICAL_ADD_HURT",
                    models.DecimalField(
                        decimal_places=1,
                        max_digits=4,
                        verbose_name="Physical DMG Bonus",
                    ),
                ),
                (
                    "FIGHT_PROP_FIRE_ADD_HURT",
                    models.DecimalField(
                        decimal_places=1, max_digits=4, verbose_name="Pyro DMG Bonus"
                    ),
                ),
                (
                    "FIGHT_PROP_ELEC_ADD_HURT",
                    models.DecimalField(
                        decimal_places=1, max_digits=4, verbose_name="Electro DMG Bonus"
                    ),
                ),
                (
                    "FIGHT_PROP_WATER_ADD_HURT",
                    models.DecimalField(
                        decimal_places=1, max_digits=4, verbose_name="Hydro DMG Bonus"
                    ),
                ),
                (
                    "FIGHT_PROP_WIND_ADD_HURT",
                    models.DecimalField(
                        decimal_places=1, max_digits=4, verbose_name="Anemo DMG Bonus"
                    ),
                ),
                (
                    "FIGHT_PROP_ICE_ADD_HURT",
                    models.DecimalField(
                        decimal_places=1, max_digits=4, verbose_name="Cryo DMG Bonus"
                    ),
                ),
                (
                    "FIGHT_PROP_ROCK_ADD_HURT",
                    models.DecimalField(
                        decimal_places=1, max_digits=4, verbose_name="Geo DMG Bonus"
                    ),
                ),
                (
                    "FIGHT_PROP_GRASS_ADD_HURT",
                    models.DecimalField(
                        decimal_places=1, max_digits=4, verbose_name="Dendro DMG Bonus"
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.character"
                    ),
                ),
            ],
        ),
    ]
