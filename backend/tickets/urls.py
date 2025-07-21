from rest_framework.routers import DefaultRouter
from .views import TicketViewSet, UserProfileViewSet # Importa ambos ViewSets

router = DefaultRouter()
router.register(r'tickets', TicketViewSet, basename='ticket')
router.register(r'userprofiles', UserProfileViewSet, basename='userprofile') # Para gestionar UserProfiles

urlpatterns = router.urls
    