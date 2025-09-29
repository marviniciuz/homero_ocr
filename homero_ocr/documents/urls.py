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

app_name = "documents"

urlpatterns = [
    path("upload/audio/", views.upload_audio, name="upload_audio"),
    path("upload/pdf/", views.upload_pdf, name="upload_pdf"),
    path("process/audio/", views.process_audio, name="process_audio"),
    path("process/pdf/", views.process_pdf, name="process_pdf"),
]
