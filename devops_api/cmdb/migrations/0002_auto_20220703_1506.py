# Generated by Django 3.2 on 2022-07-03 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='disk',
            field=models.JSONField(blank=True, null=True, verbose_name='硬盘'),
        ),
        migrations.AlterField(
            model_name='server',
            name='private_ip',
            field=models.JSONField(blank=True, null=True, verbose_name='内网IP'),
        ),
        migrations.AlterField(
            model_name='server',
            name='public_ip',
            field=models.JSONField(blank=True, null=True, verbose_name='公网IP'),
        ),
    ]
