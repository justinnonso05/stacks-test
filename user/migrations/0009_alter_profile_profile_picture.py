# Generated by Django 4.2.1 on 2023-07-02 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Profile_picture',
            field=models.ImageField(blank=True, default='', null=True, upload_to='profile_pics'),
        ),
    ]
