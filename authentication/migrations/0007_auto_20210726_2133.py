# Generated by Django 3.2.5 on 2021-07-26 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_user_email'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='ipaddress',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ip address'),
        ),
    ]
