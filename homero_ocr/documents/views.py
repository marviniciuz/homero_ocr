import os
from rest_framework import viewsets
from .models import Document
from .serializers import DocumentSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings
from .utils import extract_text_from_file, text_to_speech
from pathlib import Path


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
    return render(request, 
                  "documents/dashboard.html",
                  {"error": "Opçao invalida"})


@login_required
def upload_audio(request):
    return render(request, "documents/upload_audio.html")


@login_required
def upload_pdf(request):
    return render(request, "documents/upload_pdf.html")


@login_required
def process_pdf(request):
    if request.method == "POST" and request.FILES.get("document"):
        file = request.FILES["document"]
        # TODO: adicionar PDF melhorado
        return render(request, "documents/result.html", {
            "message": f"PDF melhorado para {file.name} (simulado 🚀)"
        })
    return JsonResponse({"error": "Arquivo inválido"}, status=400)


@login_required
def process_audio(request):
    if request.method == "POST" and request.FILES.get("document"):
        file = request.FILES["document"]

        # Salva o arquivo original
        doc = Document.objects.create(user=request.user, original_file=file)

        # Caminho completo do arquivo salvo
        file_path = doc.original_file.path

        # Extrair texto
        extracted_text = extract_text_from_file(file_path)
        doc.processed_text = extracted_text

        # Gerar áudio
        audio_filename = Path(doc.original_file.name).with_suffix(".mp3").name
        audio_dir = os.path.join(settings.MEDIA_ROOT, "audios")
        os.makedirs(audio_dir, exist_ok=True)
        audio_path = os.path.join(audio_dir, audio_filename)

        text_to_speech(extracted_text, audio_path)

        # Salvar caminho relativo do áudio
        doc.audio_file.name = f"audios/{audio_filename}"
        doc.save()

        return render(request, "documents/result.html", {
            "message": "Áudio gerado com sucesso 🚀",
            "audio_url": doc.audio_file.url,
            "text": extracted_text,
        })

    return render(request, "documents/result.html", {
        "message": "Erro: nenhum arquivo enviado ❌"
    })


def upload_file(request):
    if request.method == "POST" and request.FILES.get("file"):
        file = request.FILES["file"]
        file_path = f"media/{file.name}"

        # salvar o arquivo
        with open(file_path, "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # extrair texto
        text = extract_text_from_file(file_path)
        return JsonResponse({"texto": text})

    return render(request, "documents/upload.html")


def dashboard_view(request):
    """
    Exibe o dashboard principal com as três opções.
    """
    return render(request, "documents/dashboard.html")


def upload_view(request, option):
    """
    Exibe a tela de upload específica da opção escolhida.
    """
    valid_options = ["melhorar", "extrair", "audio"]

    if option not in valid_options:
        return render(request,
                      "documents/dashboard.html", 
                      {"error": "Opção inválida"})

    context = {"option": option}
    return render(request, "documents/upload.html", context)
