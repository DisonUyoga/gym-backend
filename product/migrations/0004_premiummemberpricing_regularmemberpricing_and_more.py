# Generated by Django 4.2.3 on 2023-11-13 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_alter_class_category_amount_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PremiumMemberPricing",
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
                ("member_type", models.CharField(max_length=255)),
                ("service", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=15)),
                ("period", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="RegularMemberPricing",
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
                ("member_type", models.CharField(max_length=255)),
                ("service", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=15)),
                ("period", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="StandardMemberPricing",
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
                ("member_type", models.CharField(max_length=255)),
                ("service", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=15)),
                ("period", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="class_category",
            name="amount",
        ),
        migrations.AddField(
            model_name="class_category",
            name="premium",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="standard",
                to="product.regularmemberpricing",
            ),
        ),
        migrations.AddField(
            model_name="class_category",
            name="regular",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="regular",
                to="product.regularmemberpricing",
            ),
        ),
        migrations.AddField(
            model_name="class_category",
            name="standard",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="premium",
                to="product.regularmemberpricing",
            ),
        ),
    ]