# Generated by Django 4.1.5 on 2023-02-01 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appmodel',
            name='url',
            field=models.URLField(),
        ),
    ]
