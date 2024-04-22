# Generated by Django 5.0.4 on 2024-04-16 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("skills", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Job",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("company", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                (
                    "job_type",
                    models.CharField(
                        choices=[
                            ("FULL_TIME", "Full Time"),
                            ("PART_TIME", "Part Time"),
                            ("FREELANCE", "Freelance"),
                            ("INTERSHIP", "Intership"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "job_level",
                    models.CharField(
                        choices=[
                            ("JUNIOR", "Junior"),
                            ("MIDDLE", "Middle"),
                            ("SENIOR", "Senior"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "salary",
                    models.DecimalField(decimal_places=2, max_digits=10, null=True),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "skills",
                    models.ManyToManyField(related_name="jobs", to="skills.skill"),
                ),
            ],
            options={
                "ordering": ("id",),
            },
        ),
    ]