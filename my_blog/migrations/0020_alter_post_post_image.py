# Generated by Django 4.1 on 2022-09-13 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0019_post_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='my_blog/images/', verbose_name='Post Thumbnail'),
        ),
    ]
