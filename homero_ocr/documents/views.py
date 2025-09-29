from rest_framework import viewsets
from .models import Document
from .serializers import DocumentSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


def history(request):
    docs = Document.objects.filter(user=request.user).order_by('-uploaded_at')
    return render(request, 'documents/history.html', {'documents': docs})


@login_required
def dashboard(request):
    return render(request, "documents/dashboard.html")


def process_choice(request):
    option = request.GET.get("option")
    if option == "audio":
        return render(request, "documents/upload_audio.html")
    elif option == "pdf":
        return render(request, "documents/upload_pdf.html")
    return render(request, "documents/dashboard.html", {"error": "Opçao invalida"})


@login_required
def upload_audio(request):
    return render(request, "documents/upload_audio.html")

@login_required
def upload_pdf(request):
    return render(request, "documents/upload_pdf.html")

@login_required
def process_audio(request):
    if request.method == "POST" and request.FILES.get("document"):
        file = request.FILES["document"]
        # TODO: adicionar OCR + TTS
        return render(request, "documents/result.html", {
            "message": f"Áudio gerado para {file.name} (simulado 🚀)"
        })
    return JsonResponse({"error": "Arquivo inválido"}, status=400)

@login_required
def process_pdf(request):
    if request.method == "POST" and request.FILES.get("document"):
        file = request.FILES["document"]
        # TODO: adicionar PDF melhorado
        return render(request, "documents/result.html", {
            "message": f"PDF melhorado para {file.name} (simulado 🚀)"
        })
    return JsonResponse({"error": "Arquivo inválido"}, status=400)
