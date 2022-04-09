# Generated by Django 4.0.3 on 2022-04-01 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='guardian_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, null=True)),
                ('Class', models.TextField(max_length=100, null=True)),
                ('Subject', models.TextField(max_length=100, null=True)),
                ('Teacher', models.TextField(max_length=100, null=True)),
                ('Area', models.CharField(max_length=100, null=True)),
                ('Email', models.EmailField(max_length=100, null=True)),
                ('Text', models.TextField(max_length=500, null=True)),
            ],
        ),
    ]
