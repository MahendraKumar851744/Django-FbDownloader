# Generated by Django 4.1.5 on 2023-02-01 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_appmodel_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appmodel',
            name='url',
            field=models.CharField(max_length=5000),
        ),
    ]
