# Generated by Django 5.0.1 on 2024-02-03 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_likes_blog_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='catergryy',
        ),
        migrations.AddField(
            model_name='blog',
            name='catergryy',
            field=models.ManyToManyField(blank=True, null=True, to='blog.catergry'),
        ),
    ]