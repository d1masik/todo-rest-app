from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from authentication.models import User


class Card(models.Model):
    title = models.CharField(_('Заголовок'), max_length=255)
    body = models.TextField(_('Тело карточки'))
    created_dt = models.DateTimeField(_('Создано'), auto_now_add=True),
    updated_dt = models.DateTimeField(_('Обновлено'), auto_now=True)
    done = models.BooleanField(_('Сделано'), default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
