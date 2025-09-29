from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet
from django.urls import path
from . import views


router = DefaultRouter()
router.register(r'documents', DocumentViewSet)
urlpatterns = router.urls


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('process/', views.process_choice, name='process_choice'),
]
