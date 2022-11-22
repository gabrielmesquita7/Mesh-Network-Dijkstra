
<p style="font-size:120%;" align="center">
    <a href="#problema">Introdução</a> -
    <a href="#desenvolvimento">Desenvolvimento</a> -
    <a href="#resultados">Resultados</a> -
    <a href="#aplicabilidade">Aplicabilidade</a> -
    <a href="#executar">Executar</a> -
    <a href="#contatos">Contatos</a>
</p>

# Introdução

<p align="justify">Uma rede mesh é composta de vários nós/roteadores, que passam a se comportar como uma única e grande rede, possibilitando que o cliente se conecte em qualquer um destes nós. Os nós têm a função de repetidores e cada nó está conectado a um ou mais dos outros nós. Desta maneira é possível transmitir mensagens de um nó a outro por diferentes caminhos. Já existem redes com cerca de 500 nós e mais de 400.000 usuários operando. </p>

<p align="justify">Em uma rede Wi-Fi tradicional, seu telefone ou laptop é conectado a um único roteador e toda a comunicação passa por esse único roteador. Quanto mais longe você estiver do roteador, mais fraco será o sinal. Itens como paredes, móveis e outras obstruções podem afetar a distribuição de sinais sem fio em sua casa. Já na rede mesh, você tem vários pontos de conectividade em sua casa para nunca estar longe de um.</p>

<p align="justify"> Em uma rede mesh, se um ponto cair, a comunicação é simplesmente redirecionada para outro ponto. Porém, se o seu roteador ou ponto principal ficar offline (aquele conectado ao seu modem), toda a sua rede também ficará. Como todos os pontos estão conectados entre si, os dados podem seguir vários caminhos até seu destino⁠ e sempre escolherão a melhor rota do ponto A ao ponto B.</p>

<p align="justify"> Como dito anteriormente, a rede mesh procura automaticamente a melhor rota de um nó até a internet, podemos relacionar esse problema com a utilização de um grafo simples com suas arestas tendo seus pesos relacionados com a transmissão wireless entre os nós/roteadores. </p>
 

# Desenvolvimento

<p align="justify"> Já decidido o tipo de grafo a se utilizar, é necessário pensar sobre qual será o algoritmo utilizado para encontrar a melhor rota entre um nó A até o B. Com isso foi escolhido o Algoritmo de Dijkstra. </p>

## Dijkstra

<p align="justify">O Algoritmo de Dijkstra basicamente começa no nó que você escolhe (o nó de origem) e analisa o grafo para encontrar o caminho de menor custo entre esse nó e todos os outros nós do grafo. Uma vez que o algoritmo encontrou o caminho de menor custo entre o nó de origem e outro nó, esse nó é marcado como "visitado" e adicionado ao caminho.</p>

<p align="justify"> O processo continua até que todos os nós do grafo tenham sido adicionados ao caminho. Desta forma, temos um caminho que conecta o nó de origem a todos os outros nós seguindo o caminho de menor custo possível para chegar a cada nó.</p>

## Código 
<p align="justify">
A construção do grafo foi feita por meio da classe Graph, onde é utilizado um dictionary para a implementaçao do grafo, onde as chaves do dictionary correspondem aos nós e seus valores correspondem aos dictionarys que registram os pesos a outros nós no gráfico.</p>

>Exemplo: Nó = C ;
>Valor = {'E': 0.04, 'D': 0.04, 'A': 0.5, 'B': 0.2}

<p align="justify">Ou seja, o nó C está conectado com o nó E com uma aresta de peso 0.04,também com o nó D com uma aresta de peso 0.04 e assim por diante...</p>

<p align="justify">A sua construção no main é bastante simples, primeiro é definido uma lista de nós que serão atribuidos para cada chave do dict, por fim é definido o peso das arestas atribuindo o valor entre duas chaves(nós) em um dict e depois criando o objeto da classe.</p>

```py
class Graph(object):
def print_graph():

#main()
nodes = ["A", "B", "C", "D", "E", "Sink"]

init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph["A"]["B"] = "edge_weight"
graph = Graph(nodes, init_graph)
```
<p align="justify"> Para o Dijkstra foi implementado uma função seguindo a teoria anteriormente mencionada, e tendo como retorno da função dois dictionarys, um com os nós anteriores e o outro com o melhor caminho com os valores das arestas somado. Por fim é executado a função para printar o resultado onde vai ser mostrado ao usuario o valor da soma das arestas percorridas e o caminho com os nós em sequencia. </p>

>Exemplo: 

>Foi encontrado o seguinte melhor caminho com valor de 0.4  (A -> B -> C -> D -> Sink)

```py
def dijkstra_algorithm(graph, start_node):
def print_result(previous_nodes, shortest_path, start_node, target_node):

#main()

previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="A")
print_result(previous_nodes, shortest_path,start_node="A", target_node="Sink")
```

## Equação para definir o peso da aresta

<p align="justify"> Por fim é utilizado uma função para definir a equação que irá definir o peso da aresta, tal equação irá levar em consideração o trafego da rede e sua porcentagem de uso como também a potencia do sinal que influenciará na largura de banda (Mbps).</p>

O valor da potencia do sinal é classificado de 1 a 3:
+ **1** = Sinal Ruim :: *Larg.Banda* = 10 Mbps
+ **2** = Sinal Bom :: *Larg.Banda* = 25 Mbps
+ **3** = Sinal Otimo :: *Larg.Banda* = 50 Mbps


img da equacao

```py
def edge_weight(max_fluxo, uso, potencia_sinal):
```

# Resultados
### Primeira Situação: Arvore Geradora Mínima

### Segunda Situação: Potencia do Sinal

### Terceira Situação: Trafego de rede


# Aplicabilidade
como aplicar o mesmo codigo para diferentes problemas

# Executar
* Como executar:

| Comando                |  Função                                                                                           |                     
| -----------------------| ------------------------------------------------------------------------------------------------- |
|  `python3 main.py`          | Executa o arquivo python       |


# Contatos

<div style="display: inline-block;">
<a href="https://t.me/mesquita776">
<img align="center" height="20px" width="90px" src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/> 
</a>

<a href="https://www.linkedin.com/in/gabriel-mesquita-pereira-675946229/">
<img align="center" height="20px" width="90px" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>

</div>

<a style="color:black" href="mailto:michel@cefetmg.br?subject=[GitHub]%20Source%20Dynamic%20Lists">
✉️ <i>mesquitagabriel30@gmail.com</i>
</a>

<p> </p>