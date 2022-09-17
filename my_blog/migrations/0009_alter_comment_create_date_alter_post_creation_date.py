# Generated by Django 4.1 on 2022-08-18 22:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0008_alter_comment_create_date_alter_post_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Time of creation'),
        ),
    ]
