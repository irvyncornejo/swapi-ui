# Generated by Django 4.2.13 on 2024-06-10 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_films_external_reference_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='release_date',
            field=models.DateField(),
        ),
    ]