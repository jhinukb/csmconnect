# Generated by Django 3.0.6 on 2020-06-10 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_auto_20200609_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.CharField(choices=[('6/10/2020', '6/10/2020'), ('6/11/2020', '6/11/2020'), ('6/12/2020', '6/12/2020'), ('6/13/2020', '6/13/2020'), ('6/14/2020', '6/14/2020'), ('6/15/2020', '6/15/2020'), ('6/16/2020', '6/16/2020')], max_length=10),
        ),
    ]