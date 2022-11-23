
<p style="font-size:120%;" align="center">
    <a href="#introducao">Introdução</a> -
    <a href="#desenvolvimento">Desenvolvimento</a> -
    <a href="#codigo">Código</a> -
    <a href="#resultados">Resultados</a> -
    <a href="#executar">Executar</a> -
    <a href="#contatos">Contatos</a>
</p>
<p align="center">
<a href="https://gabrielmesquita7.github.io/Mesh-Network-Dijkstra/html/index.html">gabrielmesquita7.github.io/Mesh-Network-Dijkstra</a>
</p>

# Introducao

<p align="justify">Uma rede mesh é composta de vários nós/roteadores, que passam a se comportar como uma única e grande rede, possibilitando que o cliente se conecte em qualquer um destes nós. Os nós têm a função de repetidores e cada nó está conectado a um ou mais dos outros nós. Desta maneira é possível transmitir mensagens de um nó a outro por diferentes caminhos. Já existem redes com cerca de 500 nós e mais de 400.000 usuários operando. </p>

<p align="center">
    <img src="https://cdn.ttgtmedia.com/rms/onlineImages/networking-wireless_mesh_mobile.jpg">
</p>

<p align="justify">Em uma rede Wi-Fi tradicional, seu telefone ou laptop é conectado a um único roteador e toda a comunicação passa por esse único roteador. Quanto mais longe você estiver do roteador, mais fraco será o sinal. Itens como paredes, móveis e outras obstruções podem afetar a distribuição de sinais sem fio em sua casa. Já na rede mesh, você tem vários pontos de conectividade em sua casa para nunca estar longe de um.</p>

<p align="center">
    <img src="/imgs/mesh.png">
</p>

<p align="justify"> Em uma rede mesh, se um ponto cair, a comunicação é simplesmente redirecionada para outro ponto. Porém, se o seu roteador ou ponto principal ficar offline (aquele conectado ao seu modem), toda a sua rede também ficará. Como todos os pontos estão conectados entre si, os dados podem seguir vários caminhos até seu destino⁠ e sempre escolherão a melhor rota do ponto A ao ponto B.</p>


<p align="center">
    <img src="https://silvernet.com/wp-content/uploads/2021/03/solutions-wireless-mesh-networks-2.gif">
</p>

<p align="justify"> Como dito anteriormente, a rede mesh procura automaticamente a melhor rota de um nó até a internet, podemos relacionar esse problema com a utilização de um grafo simples com suas arestas tendo seus pesos relacionados com a transmissão wireless entre os nós/roteadores. </p>
 

# Desenvolvimento

<p align="justify"> Já decidido o tipo de grafo a se utilizar, é necessário pensar sobre qual será o algoritmo utilizado para encontrar a melhor rota entre um nó A até o B. Com isso foi escolhido o Algoritmo de Dijkstra. </p>

## Dijkstra

<p align="justify">O Algoritmo de Dijkstra basicamente começa no nó que você escolhe (o nó de origem) e analisa o grafo para encontrar o caminho de menor custo entre esse nó e todos os outros nós do grafo. Uma vez que o algoritmo encontrou o caminho de menor custo entre o nó de origem e outro nó, esse nó é marcado como "visitado" e adicionado ao caminho.</p>

<p align="justify"> O processo continua até que todos os nós do grafo tenham sido adicionados ao caminho. Desta forma, temos um caminho que conecta o nó de origem a todos os outros nós seguindo o caminho de menor custo possível para chegar a cada nó.</p>

<p align="center">
    <img src="/imgs/Dijkstra.gif">
</p>


# Codigo 

**Afim de deixar o código devidamente documentado, foi utilizado o Sphinx que é um gerador automático de documentação escrito e usado pela comunidade Python.**
Veja em [Github Pages](https://gabrielmesquita7.github.io/Mesh-Network-Dijkstra/html/index.html)
* [gabrielmesquita7.github.io/Mesh-Network-Dijkstra](https://gabrielmesquita7.github.io/Mesh-Network-Dijkstra/html/index.html)

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

<p align="center">
    <img src="/imgs/equation.png">
</p>


```py
def edge_weight(max_fluxo, uso, potencia_sinal):
```

# Resultados

<p align="justify"> Para simular a efetividade do programa em encontrar o melhor caminho para a rede mesh, será testado um ambiente onde haverá 8 roteadores/nós onde um deles será o Gateway(Sink), ou seja, estará conectado diretamente na internet via cabo.</p>

<p align="justify"> Na seguinte representação foi escolhido os seguintes nós da rede mesh: A, B, C, D, E, F, G (Gateway/Sink) e H. Será testado diferentes situações para determinar a escolha do melhor caminho.</p>

<p align="center">
    <img src="/imgs/planta.jpg">
</p>

### Primeira Situação: Arvore Geradora Mínima

<p align="justify"> Primeiramente é testado com o mesmo peso para todas as arestas, ou seja, é imaginado que em condições iguais para todos os roteadores seria seguido o(s) seguinte(s) caminho(s) em uma situação onde o cliente esteja mais perto do roteador A.</p>

<p align="center">
    <img src="/imgs/planta01.jpg">
</p>

**Resultado:**
```terminal
A -> B -> G
```

<p align="justify"> Agora se o cliente estivesse mais perto do roteador C haveria o(s) seguinte(s) caminho(s):</p>

**Resultado:**
```terminal
C -> B -> G
    ou
C -> H -> G
```

### Segunda Situação: Potencia do Sinal

<p align="justify"> Agora é levado em consideração a potencia de sinal de cada roteador baseado em suas distancias de um ao outro, ou seja, se o roteador A está longe ou tem bastante paredes bloqueando o sinal em relação ao roteador D, a potencia de sinal tende a ser menor, logo sua largura de banda terá uma velocidade menor.</p>

<p align="justify"> Na seguinte situação, o cliente está perto do roteador D e cada potencia de sinal esta numerada.</p>

<p align="center">
    <img src="/imgs/planta02.jpg">
</p>

> Obs: Como nesse exemplo somente será observado a influência da potência do sinal no calculo do melhor caminho, todos terão a mesmo trafego de rede.

**Resultado:**
```terminal
Foi encontrado o seguinte melhor caminho com valor de 16.0
D -> E -> F -> G
```

### Terceira Situação: Trafego de rede

<p align="justify"> Na ultimo ambiente, será levado em consideração tanto a potencia do sinal como o trafego de rede, sendo assim como queremos evidenciar o impacto do trafego será utilizado o exemplo anterior de forma a aumentar o trafego no caminho menor encontrado anteriormente e seus adjacentes para verificar seu novo comportamento.</p>

<p align="center">
    <img src="/imgs/planta03.jpg">
</p>

**Resultado:**
```terminal
Foi encontrado o seguinte melhor caminho com valor de 40.0.
D -> B -> C -> H -> G
```

### Saida Esperada
Utilizando como exemplo a ultima situação a saida esperada do programa é a seguinte: 

<p align="center">
    <img src="/imgs/result.png">
</p>

### Conclusão 

<p align="justify"> Levando em consideração os experimentos anteriores, podemos concluir que em uma primeira situação onde no local não haver nenhum trafego significativo oque irá definir o caminho mínimo será a potência do sinal, já em uma situação onde as linhas de trafego tiverem sendo bastante utilizadas seja pela quantidade de usuarios nela ou pela quantidade de dados sendo trafegados, o programa opta pelas redes com menos tráfego já que tanto na equação quanto no ambiente das redes mesh é mais vantajoso percorrer uma maior distancia para evitar as redes de alto tráfego, sendo assim o Tráfego de rede tem um peso maior na escolha do caminho.</p>

>Obs: A variavel "Trafego de rede" é calculada pela multiplicação entre o máximo de trafego (Ex: 1000 Mb) e sua porcentagem de uso (Ex: 50% ou 0,5)



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
