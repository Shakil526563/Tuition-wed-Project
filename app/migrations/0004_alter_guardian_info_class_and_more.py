# Generated by Django 4.0.3 on 2022-04-01 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_guardian_info_class_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guardian_info',
            name='Class',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='guardian_info',
            name='Subject',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='guardian_info',
            name='Teacher',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
