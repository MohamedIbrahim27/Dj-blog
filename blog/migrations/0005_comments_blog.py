# Generated by Django 5.0.1 on 2024-02-04 02:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blog'),
        ),
    ]
