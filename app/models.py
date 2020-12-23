from django.db import models

# Create your models here.

class Produto (models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade dem  Estoque')



    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length = 100)
    email = models.EmailField('E-mail',max_length=100)

    

# Criando uns função str para aparecer a string da classe
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'