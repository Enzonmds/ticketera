from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Ticket
from .serializers import TicketSerializer, UserProfileSerializer
from users.models import UserProfile
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

@method_decorator(csrf_exempt, name='dispatch')
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = 'ticket_id'

    def get_queryset(self):
        return Ticket.objects.all()

    @action(detail=True, methods=['post'])
    def assign(self, request, ticket_id=None):
        ticket = self.get_object()
        user_profile_id = request.data.get('assigned_to_id')

        if not user_profile_id:
            return Response({'detail': 'Se requiere el ID del perfil de usuario para asignar.'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            user_profile = UserProfile.objects.get(id=user_profile_id)
            ticket.assigned_to = user_profile
            ticket.status = 'assigned'
            ticket.save()
            serializer = self.get_serializer(ticket)
            return Response(serializer.data)
        except UserProfile.DoesNotExist:
            return Response({'detail': 'Perfil de usuario no encontrado.'},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['post'])
    def close(self, request, ticket_id=None):
        ticket = self.get_object()
        ticket.status = 'closed'
        ticket.save()
        serializer = self.get_serializer(ticket)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def content(self, request, ticket_id=None):
        ticket = self.get_object()
        return Response({'original_email_content': ticket.original_email_content})
