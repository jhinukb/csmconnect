# Generated by Django 3.0.6 on 2020-06-20 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0010_auto_20200617_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]