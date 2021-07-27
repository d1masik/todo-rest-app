# Generated by Django 3.2.5 on 2021-07-26 19:00

import authentication.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True, validators=[authentication.validators.ExcludeEmailValidator(excludelist=['gmail.com', 'icloud.com'])], verbose_name='Email address'),
        ),
    ]
