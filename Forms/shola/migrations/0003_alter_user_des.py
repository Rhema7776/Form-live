# Generated by Django 4.0.6 on 2022-07-13 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shola', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='des',
            field=models.TextField(max_length=200),
        ),
    ]
