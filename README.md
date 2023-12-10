<h1 align="center">
  Kmeans
</h1>

![Resultado final do projeto](.github/kmeans.png)

## 📚 Projeto

Algoritmo desenvolvido para a disciplina de Inteligência Artificial da Uni7. O algoritmo receberá coordenadas como pontos do grafo, e vai selecionar 2 pontos aleatoriamente dos pontos criados anteriormente para serem os centroides. O objetivo é separar os pontos em dois grupos, onde cada pontos pertencerá ao seu centroid mais proximo.

## 💼 Tecnologias utilizadas

Para o desenvolvimento deste site utilizei as seguintes tecnologias:

- Python;
- Random Lib;

## 🔧 Arquitetura

Para criar o grafo, utilizei uma classe (Grafo) que implementa um dicionário, onde nele é armazenado o vértice e os vértices para qual ele possui arestas. A classe Grafo possui uma função (getVizinhos) para pegar os vértices para qual determinado vértice possui arestas, e outra função (excluiRep) que utiliza o resultado da função getVizinhos como parâmetro, para excluir os vértices que já estão em LE, LNE e BSS. A lógica segue como a vista em sala de aula.

Também utilizei duas bibliotecas do python, o matplotlib e networkx, para exibir o grafo em tela e mostrar o algoritmo percorrendo pelos vértices durante sua execução.

Para o desenvolvimento do algoritmo utilizei 3 classes como estrutura de dados, a classe Pontos, a classe Cluster (centroide), e a classe Kmeans. A classe Pontos armazena os pontos fornecidos pelo usuario, o Cluster tem seu Id, suas coordenadas e uma lista de pontos que ele armazena.
