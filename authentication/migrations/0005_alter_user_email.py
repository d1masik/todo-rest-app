# Generated by Django 3.2.5 on 2021-07-25 21:22

import authentication.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=0, error_messages={'unique': 'A user with that username already exists.'}, max_length=254, unique=True, validators=[authentication.validators.ExcludeEmailValidator(excludelist=['gmail.com', 'icloud.com'])], verbose_name='Email address'),
            preserve_default=False,
        ),
    ]
