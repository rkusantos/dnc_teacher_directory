# Generated by Django 2.2.6 on 2020-11-09 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(upload_to='images/')),
                ('email_address', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.IntegerField(max_length=10)),
                ('room_number', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('email_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher_directory.Teacher')),
            ],
        ),
    ]
