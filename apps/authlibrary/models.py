from django.conf import settings
from django.db import models

class Client(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        default=1,
        on_delete=models.CASCADE,
        related_name='client_user',
    )

    def __str__(self):
        return self.user.username
