import pytest

from celery_tasks.tasks import soma, fatorial


def test_task_soma_calcula_corretamente():
    # Chamando a task diretamente (sem Celery rodando)
    assert soma(2, 3) == 5
    assert soma(-10, 4) == -6


def test_task_fatorial_calcula_corretamente():
    assert fatorial(5) == 120
    assert fatorial(1) == 1
    assert fatorial(3) == 6


def test_task_fatorial_caso_borda_zero():
    assert fatorial(0) == 1


def test_task_fatorial_nao_aceita_negativo():
    with pytest.raises(ValueError):
        fatorial(-1)


def test_tasks_com_run_tambem_funciona():
    # Alternativa: chamar o método .run (útil quando você quer ignorar wrapper do Celery)
    assert soma.run(10, 5) == 15
    assert fatorial.run(6) == 720
