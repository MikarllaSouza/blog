from django.shortcuts import render, get_object_or_404
from .models import Aluno, ImagemAluno


def home(request):
    alunos = Aluno.objects.all()
    fotos = ImagemAluno.objects.all()

    context = {"alunos": alunos, "fotos": fotos}

    return render(request, "index.html", context)


def perfil(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    fotos = ImagemAluno.objects.filter(aluno_id=id)
    context = {"aluno": aluno, "fotos": fotos}

    return render(request, "perfil.html", context)
