# Generated by Django 4.1.4 on 2022-12-21 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hello", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="ФИО")),
                (
                    "date_of_birth",
                    models.CharField(max_length=10, verbose_name="Дата рождения"),
                ),
                ("admission_year", models.IntegerField(verbose_name="Год поступления")),
            ],
        ),
        migrations.CreateModel(
            name="University",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "full_name",
                    models.CharField(max_length=150, verbose_name="Полное название"),
                ),
                (
                    "short_name",
                    models.CharField(
                        max_length=20, verbose_name="Сокращенное название"
                    ),
                ),
                (
                    "creation_date",
                    models.CharField(max_length=10, verbose_name="Дата создания"),
                ),
            ],
        ),
        migrations.DeleteModel(name="Member",),
        migrations.AddField(
            model_name="student",
            name="university",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="hello.university",
                verbose_name="Университет",
            ),
        ),
    ]
