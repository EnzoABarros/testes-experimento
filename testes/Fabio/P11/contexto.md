Estou precisando de um código em Python para guardar algumas informações temporariamente, como se fosse uma memória que tem espaço limitado.

A ideia é que eu consiga guardar informações usando um nome ou identificador e depois consultar essas informações quando precisar.

O espaço disponível será limitado. Por exemplo, se eu tiver espaço para guardar apenas 3 informações e tentar adicionar uma quarta, o sistema deve apagar automaticamente aquela que faz mais tempo que não é consultada, mantendo as outras.

Sempre que eu consultar uma informação, ela deve ser considerada como recentemente utilizada. Da mesma forma, se eu adicionar novamente uma informação que já existe, o conteúdo antigo deve ser substituído e ela deve passar a ser considerada uma das mais recentes.

Se eu tentar consultar algo que não foi guardado, o sistema simplesmente deve informar que não encontrou aquela informação.

Também preciso conseguir descobrir quantas informações estão guardadas no momento.

O espaço disponível deve ser definido quando o sistema for criado e precisa ser maior que zero. Caso alguém tente criar o sistema sem espaço disponível ou com um valor inválido, deve apresentar um erro.

Quero que isso funcione de maneira eficiente, mesmo quando houver muitas informações armazenadas.

Gere o código em Python para resolver esse problema. Não precisa criar interface gráfica, salvar informações em arquivos ou implementar interação pelo terminal.
