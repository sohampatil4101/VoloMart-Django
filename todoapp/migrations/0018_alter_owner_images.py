# Generated by Django 4.1.5 on 2023-02-18 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0017_alter_item_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='images',
            field=models.ImageField(upload_to='images'),
        ),
    ]