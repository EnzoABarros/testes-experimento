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

assert hasattr(module, "LRUCache"), (
    "A solução deve possuir a classe LRUCache"
)

LRUCache = module.LRUCache


def test_invalid_capacity():
    for capacidade in [0, -1, -10, 1.5, "2", None]:
        try:
            LRUCache(capacidade)
        except ValueError:
            pass
        else:
            raise AssertionError(
                f"Capacidade inválida {capacidade!r} deveria lançar ValueError"
            )


def test_basic_put_get_and_len():
    cache = LRUCache(3)

    assert len(cache) == 0
    cache.put("a", 10)
    cache.put("b", 20)

    assert cache.get("a") == 10
    assert cache.get("b") == 20
    assert len(cache) == 2


def test_missing_key_returns_none():
    cache = LRUCache(2)
    cache.put("a", 1)

    assert cache.get("inexistente") is None
    assert len(cache) == 1


def test_eviction_of_least_recently_used():
    cache = LRUCache(2)

    cache.put("a", 1)
    cache.put("b", 2)

    # "a" é a menos recentemente usada.
    cache.put("c", 3)

    assert cache.get("a") is None
    assert cache.get("b") == 2
    assert cache.get("c") == 3
    assert len(cache) == 2


def test_get_updates_recency():
    cache = LRUCache(2)

    cache.put("a", 1)
    cache.put("b", 2)

    # "a" passa a ser a mais recentemente usada.
    assert cache.get("a") == 1

    # Agora "b" deve ser removida.
    cache.put("c", 3)

    assert cache.get("a") == 1
    assert cache.get("b") is None
    assert cache.get("c") == 3


def test_put_existing_key_updates_value_and_recency():
    cache = LRUCache(2)

    cache.put("a", 1)
    cache.put("b", 2)

    cache.put("a", 100)
    cache.put("c", 3)

    assert cache.get("a") == 100
    assert cache.get("b") is None
    assert cache.get("c") == 3


def test_capacity_one():
    cache = LRUCache(1)

    cache.put("a", 1)
    assert len(cache) == 1
    assert cache.get("a") == 1

    cache.put("b", 2)

    assert len(cache) == 1
    assert cache.get("a") is None
    assert cache.get("b") == 2


def test_hashable_keys_and_arbitrary_values():
    cache = LRUCache(3)

    chave_tupla = (1, 2)
    valor = {"lista": [1, 2, 3], "ativo": True}

    cache.put(chave_tupla, valor)

    assert cache.get(chave_tupla) == valor


def test_complex_sequence():
    cache = LRUCache(3)

    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)

    assert cache.get("a") == 1
    cache.put("d", 4)

    # Depois do get("a"), "b" é a menos recentemente usada.
    assert cache.get("b") is None
    assert cache.get("a") == 1
    assert cache.get("c") == 3
    assert cache.get("d") == 4

    # Atualizar "c" também deve torná-la a mais recente.
    cache.put("c", 30)
    cache.put("e", 5)

    # Agora "a" é a menos recentemente usada.
    assert cache.get("a") is None
    assert cache.get("c") == 30
    assert cache.get("d") == 4
    assert cache.get("e") == 5
