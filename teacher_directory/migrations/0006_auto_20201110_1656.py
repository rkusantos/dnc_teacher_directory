# Generated by Django 2.2.6 on 2020-11-10 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_directory', '0005_auto_20201110_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='profile_picture',
            field=models.ImageField(blank=True, default='images/empty_profile.png', null=True, upload_to='images/'),
        ),
    ]