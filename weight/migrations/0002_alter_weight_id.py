# Generated by Django 5.1.6 on 2025-02-07 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
