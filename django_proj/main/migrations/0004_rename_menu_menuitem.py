# Generated by Django 5.0.2 on 2024-02-13 21:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_rename_category_menu"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Menu",
            new_name="MenuItem",
        ),
    ]
