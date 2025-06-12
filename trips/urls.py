from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, BusinessTripViewSet, frontend_view
from .auth_views import register, login, logout

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'business-trips', BusinessTripViewSet)

urlpatterns = [
    path('', frontend_view, name='frontend'),
    path('api/', include(router.urls)),
    path('api/register/', register),
    path('api/login/', login),
    path('api/logout/', logout),
]