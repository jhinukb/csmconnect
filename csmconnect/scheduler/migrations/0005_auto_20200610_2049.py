# Generated by Django 3.0.6 on 2020-06-10 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_auto_20200610_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.CharField(choices=[('Wed, Jun 10', 'Wed, Jun 10'), ('Thu, Jun 11', 'Thu, Jun 11'), ('Fri, Jun 12', 'Fri, Jun 12'), ('Sat, Jun 13', 'Sat, Jun 13'), ('Sun, Jun 14', 'Sun, Jun 14'), ('Mon, Jun 15', 'Mon, Jun 15'), ('Tue, Jun 16', 'Tue, Jun 16')], max_length=20),
        ),
    ]