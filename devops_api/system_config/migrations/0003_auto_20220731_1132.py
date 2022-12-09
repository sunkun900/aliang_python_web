# Generated by Django 3.2 on 2022-07-31 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_config', '0002_notify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notify',
            name='dingding_webhook',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='钉钉Webhook'),
        ),
        migrations.AlterField(
            model_name='notify',
            name='weixin_webhook',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='企业微信Webhook'),
        ),
    ]