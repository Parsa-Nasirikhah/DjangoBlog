# Generated by Django 5.1.4 on 2025-02-21 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateField(auto_now=True),
        ),
    ]
