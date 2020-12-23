from django.contrib import admin
# registrando as classes no admin
from .models import Produto, Cliente

# criando uma classes  para listar as informações na administração do django.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


# registrando as classes no admin

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)