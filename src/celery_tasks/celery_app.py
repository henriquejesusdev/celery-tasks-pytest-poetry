"""Configuração do app Celery.

Para este exercício, os testes chamam as tasks diretamente (sem broker).
Ainda assim, ter o app Celery deixa o projeto organizado e pronto para uso real.
"""

from __future__ import annotations

from celery import Celery

celery_app = Celery(
    "celery_tasks",
    broker="memory://",
    backend="cache+memory://",
)

# Config útil para ambiente de testes (não é obrigatório, mas ajuda se alguém usar delay/apply_async)
celery_app.conf.update(
    task_always_eager=True,          # executa tasks sincronamente (sem broker)
    task_eager_propagates=True,      # propaga exceções
    result_backend="cache+memory://",
)
