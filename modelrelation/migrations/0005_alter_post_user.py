# Generated by Django 4.1.1 on 2022-09-11 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("modelrelation", "0004_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="modelrelation.user",
            ),
        ),
    ]