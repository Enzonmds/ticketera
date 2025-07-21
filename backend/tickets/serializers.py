from rest_framework import serializers
from .models import Ticket
from users.models import UserProfile
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)


    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'role', 'user']

class TicketSerializer(serializers.ModelSerializer):
    assigned_to = UserProfileSerializer(read_only=True)
    assigned_to_id = serializers.PrimaryKeyRelatedField(
        queryset=UserProfile.objects.all(), source='assigned_to', write_only=True, required=False
    )

    class Meta:
        model = Ticket
        fields = [
            'ticket_id',
            'subject',
            'original_email_content',
            'created_at',
            'assigned_to',
            'assigned_to_id',
            'status'
        ]
        read_only_fields = ['ticket_id', 'created_at']
