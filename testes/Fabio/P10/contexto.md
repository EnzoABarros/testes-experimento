Tô precisando de uma função em Python pra organizar uma lista de tarefas de um projeto.

Eu tenho várias tarefas e algumas dependem de outras. Por exemplo, pra fazer o deploy eu preciso primeiro terminar o build, e pra fazer o build preciso terminar a compilação. Queria passar essas informações pra função e receber de volta a ordem em que as tarefas devem ser feitas.

Pode fazer uma função chamada `agendar_tarefas(tarefas)`.

O `tarefas` vai ser um dicionário, onde cada chave é o nome de uma tarefa e o valor é uma lista com as tarefas que precisam ser feitas antes dela. Nem toda tarefa precisa necessariamente aparecer como chave, porque ela pode aparecer só como dependência de outra.

A função precisa devolver uma lista com todas as tarefas na ordem correta, sem colocar uma tarefa antes de alguma coisa que ela depende.

Tem uma coisa importante: se tiver mais de uma tarefa disponível pra fazer ao mesmo tempo, quero que você escolha primeiro a que vem antes em ordem alfabética. Isso precisa deixar o resultado sempre previsível.

Também preciso que a função perceba quando existe um ciclo de dependências. Por exemplo, se A depende de B, B depende de C e C depende de A, não existe uma ordem possível. Nesse caso, pode lançar um `ValueError`.

Se não tiver nenhuma tarefa, deve retornar uma lista vazia.

Também não quero que a função altere o dicionário original que eu passei pra ela.

Por enquanto não precisa criar interface, ler arquivo ou nada disso. Só preciso da função em Python mesmo.
