# Generated by Django 2.2.16 on 2020-10-14 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCustomUser', '0002_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=25, null=True, unique=True),
        ),
    ]
