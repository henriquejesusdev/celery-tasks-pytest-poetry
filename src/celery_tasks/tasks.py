"""Tasks Celery do exercício.

- soma: soma dois números
- fatorial: calcula fatorial de um número (com caso de borda n=0)
"""

from __future__ import annotations

from .celery_app import celery_app


@celery_app.task(name="tasks.soma")
def soma(a: int, b: int) -> int:
    """Retorna a soma de dois inteiros."""
    return a + b


@celery_app.task(name="tasks.fatorial")
def fatorial(n: int) -> int:
    """Calcula o fatorial de um inteiro não-negativo.

    Regras:
    - fatorial(0) == 1
    - para n < 0: levanta ValueError
    """
    if n < 0:
        raise ValueError("n deve ser >= 0")

    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
