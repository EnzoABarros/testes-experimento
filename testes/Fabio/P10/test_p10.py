import importlib.util
from pathlib import Path

# O arquivo contendo a solução deve ser salvo como solution.py na mesma pasta
# deste teste.

SOLUTION = Path(__file__).with_name("solution.py")

spec = importlib.util.spec_from_file_location("solution", SOLUTION)
if spec is None or spec.loader is None:
    raise ImportError("Não foi possível carregar solution.py")

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert hasattr(module, "agendar_tarefas"), (
    "A solução deve possuir a função agendar_tarefas"
)

agendar_tarefas = module.agendar_tarefas


def assert_valid_order(tarefas, resultado):
    # Todas as tarefas, inclusive as que aparecem apenas como dependência,
    # devem estar presentes exatamente uma vez.
    esperadas = set(tarefas)
    for deps in tarefas.values():
        esperadas.update(deps)

    assert set(resultado) == esperadas
    assert len(resultado) == len(esperadas)
    assert len(resultado) == len(set(resultado))

    pos = {tarefa: i for i, tarefa in enumerate(resultado)}

    for tarefa, deps in tarefas.items():
        for dep in deps:
            assert pos[dep] < pos[tarefa], (
                f"{dep} deve aparecer antes de {tarefa}"
            )


def test_empty():
    assert agendar_tarefas({}) == []


def test_linear_dependencies():
    tarefas = {
        "compilar": ["testar"],
        "testar": ["implementar"],
        "implementar": [],
    }

    resultado = agendar_tarefas(tarefas)

    assert resultado == ["implementar", "testar", "compilar"]


def test_lexicographic_tie_break():
    tarefas = {
        "B": [],
        "A": [],
        "C": ["A", "B"],
    }

    resultado = agendar_tarefas(tarefas)

    assert resultado == ["A", "B", "C"]


def test_dependency_only_nodes():
    tarefas = {
        "deploy": ["build"],
        "build": ["compile"],
    }

    resultado = agendar_tarefas(tarefas)

    assert resultado == ["compile", "build", "deploy"]


def test_multiple_independent_tasks():
    tarefas = {
        "D": ["B"],
        "C": [],
        "B": [],
        "A": [],
    }

    resultado = agendar_tarefas(tarefas)

    assert resultado == ["A", "B", "C", "D"]


def test_cycle():
    tarefas = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"],
    }

    try:
        agendar_tarefas(tarefas)
    except ValueError:
        pass
    else:
        raise AssertionError("Dependência circular deveria lançar ValueError")


def test_does_not_modify_input():
    tarefas = {
        "C": ["A", "B"],
        "A": [],
        "B": [],
    }

    original = {
        chave: list(deps)
        for chave, deps in tarefas.items()
    }

    agendar_tarefas(tarefas)

    assert tarefas == original
