from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')  # Campos a mostrar en la lista
    search_fields = ('user__username', 'role')  # Campos para búsqueda
    list_filter = ('role',)  # Filtros en la barra lateral
