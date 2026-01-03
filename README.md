# Celery Tasks + Pytest (Poetry)

Projeto de exemplo para praticar testes unitarios de tasks assincronas usando Celery sem precisar subir broker/worker (os testes chamam as tasks diretamente).

## Estrutura

```
src/
  celery_tasks/
    __init__.py
    celery_app.py
    tasks.py
tests/
  test_tasks.py
```

## Como rodar (poetry no PATH)

```powershell
poetry install
poetry run pytest
```

### Se o comando `poetry` nao for reconhecido (Windows)
- Usar o modulo direto:
  ```powershell
  py -m poetry install
  py -m poetry run pytest
  ```
- Ou ajustar o `PATH` para incluir a pasta de scripts do Python 3.14 e entao usar `poetry` normalmente:
  ```powershell
  $env:Path="$env:APPDATA\Python\Python314\Scripts;$env:Path"
  poetry install
  poetry run pytest
  ```

## Observacao importante

Para este exercicio, os testes chamam as tasks diretamente (ex.: `soma(2,3)` ou `soma.run(2,3)`), entao voce nao precisa iniciar Redis/RabbitMQ nem rodar `celery worker`. Ainda assim, o arquivo `celery_app.py` deixa o projeto pronto para uso real.
