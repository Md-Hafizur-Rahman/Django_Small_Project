# Generated by Django 4.1.1 on 2022-09-10 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("modelrelation", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="favourite",
            field=models.BooleanField(default=False),
        ),
    ]