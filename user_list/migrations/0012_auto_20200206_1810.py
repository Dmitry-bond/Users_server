# Generated by Django 3.0.2 on 2020-02-06 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_list', '0011_auto_20200206_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='photo',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
