from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import UserManager
from authentication.validators import ExcludeEmailValidator, first_name_validator, last_name_validator


class EmailUserManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user = self.model(
           email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    email = models.EmailField(_('Email address'),
                              validators=[ExcludeEmailValidator(excludelist=['gmail.com', 'icloud.com'])],
                              unique=True,
                              error_messages={
                                  'unique': _("A user with that email already exists."),
                              },
                              )
    username = models.CharField(
        _('username'),
        max_length=150,
    )

    ipaddress = models.CharField(_('Ip address'), max_length=255, blank=True, null=True)
    first_name = models.CharField(_('first name'), max_length=150, blank=True, validators=[first_name_validator])
    last_name = models.CharField(_('last name'), max_length=150, blank=True, validators=[last_name_validator])

    password = models.CharField(_('password'), max_length=16)

    objects = EmailUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

