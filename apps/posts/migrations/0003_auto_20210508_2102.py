# Generated by Django 3.1.9 on 2021-05-09 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210508_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_added',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_modified',
            field=models.DateTimeField(blank=True, editable=False),
        ),
    ]
