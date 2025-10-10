from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

# Router da API REST
router = DefaultRouter()
router.register(r'documents', views.DocumentViewSet)

app_name = "documents"

urlpatterns = [
    # Dashboard principal
    path("", views.dashboard_view, name="dashboard"),
    path("upload-option/<str:option>/", views.process_choice, name="upload_option"),

    # Uploads
    path("upload/audio/", views.upload_audio, name="upload_audio"),
    path("upload/pdf/", views.upload_pdf, name="upload_pdf"),
    path("upload/<str:option>/", views.upload_view, name="upload"),

    # Processamentos
    path("process_choice/", views.process_choice, name="process_choice"),
    path("process/audio/", views.process_audio, name="process_audio"),
    path("process/pdf/", views.process_pdf, name="process_pdf"),

    # Histórico (opcional)
    path("history/", views.history, name="history"),
]

# Adiciona as rotas da API do router
urlpatterns += router.urls
