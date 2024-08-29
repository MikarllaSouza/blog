from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.nome


class ImagemAluno(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    foto = models.ImageField(
        default=None, upload_to="images/covers/%Y/%m/%d/", blank=True
    )
    descricao = models.CharField(max_length=100, default="")
