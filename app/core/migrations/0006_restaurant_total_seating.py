# Generated by Django 3.0.3 on 2020-05-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_user_is_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='total_seating',
            field=models.IntegerField(default=0),
        ),
    ]