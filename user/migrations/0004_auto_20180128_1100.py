# Generated by Django 2.0.1 on 2018-01-28 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20180120_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.IntegerField(max_length=1),
        ),
    ]
