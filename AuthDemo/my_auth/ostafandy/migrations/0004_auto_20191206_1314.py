# Generated by Django 3.0 on 2019-12-06 13:14

from django.db import migrations, models
import ostafandy.models


class Migration(migrations.Migration):

    dependencies = [
        ('ostafandy', '0003_clientuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientuser',
            name='craft',
            field=models.IntegerField(choices=[(1, 'Carpentry'), (2, 'Electrical'), (3, 'Plumbing')], default=0),
        ),
        migrations.AlterField(
            model_name='clientuser',
            name='phone_number',
            field=models.CharField(max_length=12, unique=True, validators=[ostafandy.models.validate_phone_number]),
        ),
    ]