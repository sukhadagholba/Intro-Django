# Generated by Django 2.1.2 on 2018-10-23 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0004_auto_20181023_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pages1',
            field=models.IntegerField(default=0),
        ),
    ]