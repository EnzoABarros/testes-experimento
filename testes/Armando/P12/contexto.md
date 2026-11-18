# P12 — Menor rota de transporte

**Grau de dificuldade:** Difícil

## 1. Contexto do problema

Uma empresa distribui componentes entre diferentes centros de distribuição e precisa organizar seus trajetos de transporte. Cada trecho possui um custo específico e só pode ser percorrido no sentido indicado.

Como existem alternativas para chegar a um mesmo destino, a equipe de logística necessita identificar a rota de menor custo entre dois centros.

## 2. O que se espera que o programa faça

Desenvolver, em Python 3.10 ou superior, uma função que receba os trechos disponíveis, o centro de origem e o centro de destino e determine o caminho dirigido de menor custo.

A função deverá considerar caminhos indiretos, ciclos, múltiplos trechos entre os mesmos centros e situações em que não existe conexão até o destino.

**Assinatura da função:**

```python
def calcular_rota(trechos: list[tuple[str, str, int]], origem: str, destino: str) -> dict | None:
```

## 3. Dados envolvidos, regras e restrições

- A implementação deve ser salva em `p12.py`, com a função `calcular_rota` e a assinatura indicada.
- Cada elemento de `trechos` é uma tupla `(centro_origem, centro_destino, custo)`, e o trajeto só existe no sentido informado.
- Os identificadores de centros são strings não vazias de letras maiúsculas A–Z e dígitos 0–9, sem espaços. A ordenação segue a ordem lexicográfica do Python.
- Todos os custos são inteiros estritamente positivos. Podem existir ciclos e trechos paralelos, inclusive com custos diferentes.
- Não é permitido repetir centros na rota.
- Em caso de empate no custo mínimo, deve ser escolhida a menor sequência completa de centros em ordem lexicográfica, mesmo que possua mais trechos.
- Quando a origem e o destino forem iguais, retornar custo zero e a rota contendo apenas esse centro, mesmo que ele não esteja na lista de trechos.
- Quando não houver caminho disponível, retornar `None`.
- As entradas respeitam o formato especificado e não exigem validação adicional.
- Limites: até 500 centros e até 10.000 trechos. A solução deve ser compatível com esses limites.

## 4. Resultado esperado

Quando houver caminho, o programa deverá retornar um dicionário contendo exatamente duas chaves:

- `custo`: inteiro correspondente ao menor custo total.
- `rota`: lista de strings contendo os centros na ordem percorrida.

Caso não exista caminho, deverá retornar `None`.

**Exemplo de entrada:**

```python
calcular_rota(
    [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('C', 'B', 1),
        ('B', 'D', 3),
        ('C', 'D', 7)
    ],
    'A',
    'D'
)
```

**Saída esperada:**

```python
{
    'custo': 6,
    'rota': ['A', 'C', 'B', 'D']
}
```
