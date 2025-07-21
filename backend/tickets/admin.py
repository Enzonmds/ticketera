from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_id', 'subject', 'created_at', 'assigned_to', 'status')
    search_fields = ('ticket_id', 'subject', 'original_email_content')
    list_filter = ('status', 'assigned_to__user__username')
    readonly_fields = ('ticket_id', 'created_at')