from django.db import models

class Pessoa(models.Model):
    cpf = models.CharField(max_length=14, unique=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    data_nascimento = models.DateField()
    cep = models.CharField(max_length=10)
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.nome} - {self.cpf}'
