# Generated by Django 5.0.1 on 2024-01-09 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
