from rest_framework import viewsets
from .models import Document
from .serializers import DocumentSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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
