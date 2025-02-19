from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ClientViewSet, RegisterView

router = DefaultRouter()
router.register('clients', ClientViewSet, basename='clients')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='auth_register'),

]