# Generated by Django 4.2 on 2023-04-25 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.IntegerField(null=True),
        ),
    ]