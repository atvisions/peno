# Generated by Django 5.1.2 on 2024-10-29 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_voterecord"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="voterecord",
            unique_together={("vote_item",)},
        ),
        migrations.RemoveField(
            model_name="voterecord",
            name="ip_address",
        ),
    ]
