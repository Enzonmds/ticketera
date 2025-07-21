from django.db import models
from django.utils import timezone
import uuid

class Ticket(models.Model):
    ticket_id = models.CharField(max_length=100, unique=True, default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=255)
    original_email_content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    assigned_to = models.ForeignKey(
        'users.UserProfile', 
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=[
            ('open', 'Abierto'),
            ('assigned', 'Asignado'),
            ('closed', 'Cerrado'),
        ],
        default='open'
    )

    def __str__(self):
        return f"Ticket {self.ticket_id}: {self.subject}"

    class Meta:
        ordering = ['-created_at']
