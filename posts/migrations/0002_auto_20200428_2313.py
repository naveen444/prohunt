# Generated by Django 2.2 on 2020-04-29 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='product_summary',
            new_name='post_summary',
        ),
    ]