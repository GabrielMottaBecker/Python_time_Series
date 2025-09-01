
"""
Exercícios de Funções Python

Este módulo contém implementações de funções básicas para praticar
conceitos fundamentais de programação em Python.

Autor: Gabriel Becker
Data: 01/09/2025
Versão: 1.0
"""

import re


def e_par(n: int) -> bool:
    """Retorna True se n é par, senão False."""
    return n % 2 == 0


def fatorial(n: int) -> int:
    """Retorna n! (n fatorial). Para n<0, levante ValueError."""
    if n < 0:
        raise ValueError("Fatorial não é definido para números negativos")
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def maximo(nums):
    """Retorna o maior elemento de uma lista não vazia, sem usar max()."""
    if not nums:
        raise ValueError("Lista não pode estar vazia")
    
    maior = nums[0]
    for num in nums[1:]:
        if num > maior:
            maior = num
    return maior


def limpa_texto(s: str) -> str:
    """Deixa minúsculo e remove pontuação comum."""

    s_limpo = s.lower()

    pontuacoes = r'[,.;:!?\'"()\-_]'
    s_limpo = re.sub(pontuacoes, '', s_limpo)
    return s_limpo


def conta_vogais(s: str) -> int:
    """Conta vogais (a,e,i,o,u) em s (desconsidere acentos)."""
    vogais = 'aeiou'
    contador = 0
    for char in s.lower():
        if char in vogais:
            contador += 1
    return contador


def palindromo(s: str) -> bool:
    """Retorna True se s é palíndromo ignorando espaços e pontuação."""

    s_normalizado = re.sub(r'[^a-zA-Z0-9]', '', s.lower())

    return s_normalizado == s_normalizado[::-1]


def total_por_vendedor(vendas):
    """
    vendas: lista de tuplas (nome, valor).
    Retorna: dict {nome: soma_valores}
    """
    totais = {}
    for nome, valor in vendas:
        if nome in totais:
            totais[nome] += valor
        else:
            totais[nome] = valor
    return totais
