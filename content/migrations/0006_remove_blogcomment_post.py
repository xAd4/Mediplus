# Generated by Django 5.0.7 on 2024-08-02 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_remove_postblog_comments_blogcomment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='post',
        ),
    ]
