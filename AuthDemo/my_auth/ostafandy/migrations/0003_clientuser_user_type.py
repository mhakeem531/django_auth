# Generated by Django 3.0 on 2019-12-06 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ostafandy', '0002_auto_20191206_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientuser',
            name='user_type',
            field=models.BooleanField(default=True),
        ),
    ]
