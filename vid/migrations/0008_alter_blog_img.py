# Generated by Django 3.2.5 on 2021-07-31 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vid', '0007_blog_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(upload_to='images'),
        ),
    ]