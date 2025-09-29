from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_file = models.FileField(upload_to="uploads/")
    processed_text = models.TextField(blank=True, null=True)
    audio_file = models.FileField(upload_to="audios/", blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
 
    STATUS_CHOICES = [
        ("pending", "Pendente"),
        ("processing", "Processando"),
        ("done", "Concluído"),
        ("error", "Erro"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"{self.original_file.name} ({self.status})"
