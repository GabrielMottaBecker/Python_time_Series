# Cabeçalho em um arquivo Python:
# Não é algo obrigatório pela linguagem, mas sim uma convenção que desenvolvedores usam para documentar informações gerais sobre o arquivo.
# Normalmente colocado nas primeiras linhas do arquivo, antes mesmo dos imports.
# Pode incluir:
# Nome do arquivo
# Autor(es)
# Data de criação
# Descrição do objetivo do arquivo
# Versão, licença etc.
# Cabeçalho é mais voltado à documentação do arquivo em si.

#Doc String:
# É uma string especial de documentação em Python.
# Diferente de um comentário comum, ela pode ser acessada em tempo de execução via help() ou obj.__doc__.
# Usada em:
# Módulos (arquivo inteiro)
# Classes
# Funções e método
# Docstring é voltada à documentação do código executável (funções, classes, módulos).

# Cabeçalho: comentário simples, não acessível em tempo de execução, usado para metadados do arquivo.
# Docstring: string de documentação, acessível em runtime, usada para explicar o propósito e uso de módulos, classes e funções.


# formate o cabeçalho deste arquivo, e complete as funções abaixo

def e_par(n: int) -> bool:
    """Retorna True se n é par, senão False."""
    # TODO: retorne se n é par
    ...

def fatorial(n: int) -> int:
    """Retorna n! (n fatorial). Para n<0, levante ValueError."""
    # TODO: implemente de forma iterativa (sem recursão)
    ...

def maximo(nums):
    """Retorna o maior elemento de uma lista não vazia, sem usar max()."""
    # TODO: percorra a lista guardando o maior atual
    ...

import re

def limpa_texto(s: str) -> str:
    """Deixa minúsculo e remove pontuação comum."""
    # TODO: converta s para minúsculo e remova pontuações como ,.;:!?'"()-_
    ...

def conta_vogais(s: str) -> int:
    """Conta vogais (a,e,i,o,u) em s (desconsidere acentos)."""
    # TODO: conte as vogais simples
    ...

def palindromo(s: str) -> bool:
    """Retorna True se s é palíndromo ignorando espaços e pontuação."""
    # TODO: normalizar (minúsculo, remover não alfanumérico) e comparar com o reverso
    ...

def total_por_vendedor(vendas):
    """
    vendas: lista de tuplas (nome, valor).
    Retorna: dict {nome: soma_valores}
    """
    # TODO: inicialize um dict e vá somando
    ...

def melhor_vendedor(totais: dict):
    """
    Retorna (nome, total) com o maior total.
    Se dict vazio, levante ValueError.
    """
    # TODO: encontre o par com maior total (sem ordenar a lista inteira)
    ...

