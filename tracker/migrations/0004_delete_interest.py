# Generated by Django 4.2.2 on 2023-06-19 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_category_slug_provider_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Interest',
        ),
    ]
