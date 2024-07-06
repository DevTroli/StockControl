import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

import string
import timeit
from random import choice, randint, random

from produto.models import Produto


class Utils:
    """Métodos genéricos."""

    @staticmethod
    def gen_digits(max_length):
        return str("".join(choice(string.digits) for i in range(max_length)))


class ProdutoClass:
    @staticmethod
    def criar_produtos(produtos):
        Produto.objects.all().delete()
        aux = []
        for produto in produtos:
            data = dict(
                produto=produto,
                preco=random() * randint(10, 50),
                nivel_estoquei=None,
                estoque=randint(10, 200),
                ncm=Utils.gen_digits(8),
            )
            obj = Produto(**data)
            aux.append(obj)
        Produto.objects.bulk_create(aux)


produtos = (
    "Coca 1L",
    "Coca 2L",
    "Coca 350ml",
    "Pepsi 2L",
    "Pepsi 1L",
    "Pepsi 350ml",
    "H2O 1,5L",
    "H2O 510ml",
    "Xando: Suco de Laranja 500ml",
    "Natural One: Laranja 500ml",
    "Del Valle: Suco de Uva 350ml",
    "Água Mineral 300ml",
    "Água Mineral 1,5L",
)

tic = timeit.default_timer()

ProdutoClass.criar_produtos(produtos)


toc = timeit.default_timer()

print("Tempo:", toc - tic)
