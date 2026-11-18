# P2 — Cache LRU com capacidade e estatísticas

Implemente, em Python, uma classe:

    LRUCache

Ela representa um cache com política Least Recently Used (LRU).

A classe deve possuir:

    LRUCache(capacidade: int)

e os métodos:

    get(chave)
    put(chave, valor)
    __len__()

Requisitos:

1. `capacidade` deve ser um inteiro positivo. Caso contrário, o construtor
   deve lançar `ValueError`.
2. `get(chave)` deve retornar o valor associado à chave quando ela estiver
   presente.
3. Um `get` de uma chave existente torna essa chave a mais recentemente usada.
4. Quando a chave não existir, `get` deve retornar `None` e não deve alterar
   a ordem das demais chaves.
5. `put(chave, valor)` deve inserir uma nova chave ou atualizar uma chave
   existente.
6. Um `put` de uma chave existente deve substituir seu valor e tornar essa
   chave a mais recentemente usada.
7. Se a inserção fizer o número de itens ultrapassar a capacidade, remova
   exatamente a chave menos recentemente usada.
8. A classe deve manter a ordem de uso corretamente após qualquer combinação
   de `get` e `put`.
9. `len(cache)` deve retornar o número atual de itens armazenados.
10. A capacidade deve permanecer fixa durante toda a vida do objeto.
11. A implementação deve aceitar qualquer objeto hashable como chave e
    qualquer objeto como valor.
12. Não utilize uma biblioteca externa para implementar a política LRU.
13. A complexidade de `get` e `put` deve ser O(1) amortizado.
14. A classe deve funcionar corretamente com capacidade igual a 1.

Não é necessário criar interface gráfica, ler arquivos ou receber entrada
pelo terminal. Implemente somente a classe solicitada.
