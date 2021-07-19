# Generated by Django 3.0.5 on 2021-07-19 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('dob', models.DateField()),
                ('number', models.IntegerField()),
                ('date_of_creation', models.DateField(auto_now_add=True)),
                ('date_of_modification', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
