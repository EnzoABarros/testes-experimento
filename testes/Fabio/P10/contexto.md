# P1 — Agendamento de tarefas com dependências

Implemente, em Python, uma função:

    agendar_tarefas(tarefas: dict[str, list[str]]) -> list[str]

O parâmetro `tarefas` representa um conjunto de tarefas e suas dependências.
A chave é o identificador de uma tarefa e o valor é a lista de tarefas que
precisam ser concluídas antes dela.

Requisitos:

1. Todas as tarefas mencionadas como chaves ou como dependências devem fazer
   parte do conjunto de tarefas considerado.
2. A função deve retornar uma lista contendo todas as tarefas em uma ordem
   válida de execução, de forma que nenhuma tarefa apareça antes de uma de
   suas dependências.
3. Quando houver mais de uma ordem válida, use como critério de desempate a
   ordem lexicográfica dos identificadores disponíveis naquele momento.
4. Se houver dependências circulares, a função deve lançar `ValueError`.
5. Uma tarefa pode aparecer como dependência de várias outras tarefas.
6. Não modifique o dicionário recebido pela função.
7. A função deve funcionar também quando `tarefas` estiver vazio, retornando
   uma lista vazia.
8. A implementação deve ser determinística.

Exemplo:

    {
        "compilar": ["testar"],
        "testar": ["implementar"],
        "implementar": []
    }

deve produzir:

    ["implementar", "testar", "compilar"]

Outro exemplo:

    {
        "B": [],
        "A": [],
        "C": ["A", "B"]
    }

deve produzir:

    ["A", "B", "C"]

Não é necessário criar interface gráfica, ler arquivos ou receber entrada
pelo terminal. Implemente somente a função solicitada.
