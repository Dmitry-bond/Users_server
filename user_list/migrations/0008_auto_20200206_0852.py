# Generated by Django 3.0.2 on 2020-02-06 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_list', '0007_auto_20200206_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='photo',
            field=models.ImageField(upload_to='media/user_list/users/images/no-img.jpg'),
        ),
    ]
