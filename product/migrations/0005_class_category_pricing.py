# Generated by Django 4.2.3 on 2023-11-13 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0004_premiummemberpricing_regularmemberpricing_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="class_category",
            name="pricing",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pricing",
                to="product.pricing",
            ),
        ),
    ]
