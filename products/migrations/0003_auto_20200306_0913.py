# Generated by Django 2.2 on 2020-03-06 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200305_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
