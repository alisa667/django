# Generated by Django 4.1.4 on 2022-12-22 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hello", "0003_alter_student_admission_year_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="university",
            name="creation_date",
            field=models.DateField(max_length=10),
        ),
    ]
