from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user_id = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='client_user',
    )

    def __str__(self):
        return self.user_id.username
