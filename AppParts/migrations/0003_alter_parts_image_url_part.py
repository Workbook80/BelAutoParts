# Generated by Django 4.2.7 on 2023-12-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppParts', '0002_alter_parts_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parts',
            name='image_url_part',
            field=models.ImageField(upload_to='part_media'),
        ),
    ]