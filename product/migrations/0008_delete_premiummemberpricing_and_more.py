# Generated by Django 4.2.3 on 2023-11-13 09:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0007_remove_class_category_premium_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="PremiumMemberPricing",
        ),
        migrations.DeleteModel(
            name="RegularMemberPricing",
        ),
        migrations.DeleteModel(
            name="StandardMemberPricing",
        ),
    ]
