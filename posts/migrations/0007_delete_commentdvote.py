# Generated by Django 2.2 on 2020-07-17 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_remove_comment_dislikes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Commentdvote',
        ),
    ]