# Generated by Django 4.2.3 on 2023-11-13 09:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0006_service_alter_pricing_service"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="class_category",
            name="premium",
        ),
        migrations.RemoveField(
            model_name="class_category",
            name="regular",
        ),
        migrations.RemoveField(
            model_name="class_category",
            name="standard",
        ),
    ]
