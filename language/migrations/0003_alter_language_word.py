# Generated by Django 3.2.25 on 2024-05-12 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0002_auto_20240512_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='word',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
