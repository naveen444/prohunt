# Generated by Django 2.0.2 on 2020-08-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_delete_commentdvote'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='total_comments',
            field=models.IntegerField(default=0),
        ),
    ]
