# P13 — Seleção ótima de projetos com dependências

**Grau de dificuldade:** Difícil

## 1. Contexto do problema

Uma empresa deseja escolher quais projetos de melhoria devem ser realizados durante o próximo período, mas dispõe de orçamento limitado.

Cada projeto apresenta um custo de implantação e um benefício estimado. Algumas iniciativas dependem da realização prévia de outras, como um sistema que só pode ser implantado depois de sua infraestrutura.

## 2. O que se espera que o programa faça

Desenvolver, em Python 3.10 ou superior, uma função que analise uma lista de projetos e o orçamento disponível, selecionando o conjunto que maximize o benefício total.

O programa precisa respeitar o limite financeiro, incluir as dependências obrigatórias de cada projeto escolhido e aplicar critérios de desempate.

**Assinatura da função:**

```python
def selecionar_projetos(projetos: list[dict], orcamento: int) -> dict:
```

## 3. Dados envolvidos, regras e restrições

- A implementação deve ser salva em `p13.py`, com a função `selecionar_projetos` e a assinatura indicada.
- Cada projeto é representado por um dicionário com exatamente quatro chaves:
  - `id`: identificador único do projeto.
  - `custo`: inteiro positivo correspondente ao custo de implantação.
  - `beneficio`: inteiro não negativo correspondente ao benefício estimado.
  - `dependencias`: lista de identificadores dos projetos necessários para sua execução.
- Cada identificador contém apenas letras maiúsculas e/ou dígitos.
- Todas as dependências apontam para projetos existentes e não existem ciclos de dependência.
- Quando um projeto for selecionado, todas as suas dependências diretas e indiretas também deverão integrar o conjunto, sem contabilização duplicada.
- O custo total não poderá ultrapassar o orçamento disponível, que será um inteiro não negativo.
- Não é obrigatório utilizar todo o orçamento.
- O primeiro critério de seleção é maximizar o benefício total.
- Em caso de empate de benefício, deverá ser escolhido o conjunto de menor custo.
- Persistindo o empate, deverá ser escolhida a lista ordenada de identificadores lexicograficamente menor.
- É permitido não selecionar nenhum projeto. Nesse caso, os totais deverão ser zero e a lista de projetos deverá estar vazia.
- O programa deverá suportar até 18 projetos.
- As entradas serão válidas conforme o formato especificado, sem necessidade de validação adicional.

## 4. Resultado esperado

O programa deverá retornar um dicionário contendo exatamente três chaves:

- `projetos`: lista de identificadores selecionados em ordem lexicográfica.
- `beneficio_total`: soma dos benefícios dos projetos selecionados.
- `custo_total`: soma dos custos dos projetos selecionados.

O conjunto retornado deverá respeitar todas as restrições e representar a seleção ótima conforme os critérios estabelecidos.

**Exemplo de entrada:**

```python
selecionar_projetos(
    [
        {
            'id': 'A',
            'custo': 4,
            'beneficio': 10,
            'dependencias': ['B']
        },
        {
            'id': 'B',
            'custo': 3,
            'beneficio': 2,
            'dependencias': []
        },
        {
            'id': 'C',
            'custo': 3,
            'beneficio': 6,
            'dependencias': []
        }
    ],
    7
)
```

**Saída esperada:**

```python
{
    'projetos': ['A', 'B'],
    'beneficio_total': 12,
    'custo_total': 7
}
```
