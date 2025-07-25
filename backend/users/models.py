from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=50,
        choices=[
            ('admin', 'Administrador'),
            ('agent', 'Agente'),
            ('client', 'Cliente'),
        ],
        default='agent'
    )

    def __str__(self):
        return self.user.username