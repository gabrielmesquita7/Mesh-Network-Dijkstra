import sys


class Graph(object):
    """Um grafo representado como objeto"""

    def __init__(self, nodes, init_graph):
        """Inicia a classe graph com os nós

        :param init_graph: dict contendo as arestas do nó que conectam a outros nós
        :param nodes: lista de nós(vertices) do grafo
        """
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        """Gera o grafo final

        :return: class Graph(k,v): grafo final
        k = list[str], v = dict
        """
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value

        return graph

    def get_nodes(self):
        """Retorna os nos de um grafo

        :return: list[str]
        """
        return self.nodes

    def get_outgoing_edges(self, node):
        """Retorna os vizinhos de um no, ou seja os nós adjacentes

        :param nodes: list[str]
        :return: list[str] nós adjacentes
        """
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        """Retorna o valor de uma aresta que liga dois nos

        :param node1: (str)
        :param node2: (str)
        :return: (float) valor da aresta que liga os dois nós
        """
        return self.graph[node1][node2]


def dijkstra_algorithm(graph, start_node):
    """Implementação do Dijkstra. Primeiro o algoritmo começa visitar os nós, o codigo abaixo instrui 
    o algoritmo a encontrar o nó com o valor mais baixo. Feito isso, o algoritmo visita todos os 
    vizinhos do nó que ainda não foram visitados. Se o novo caminho para o vizinho for melhor que o melhor 
    caminho atual, o algoritmo faz ajustes nos dicionários shortest_path e previous_nodes. 

    :param graph: (Graph)
    :param start_node: (str)
    :return: (dict) previous_nodes = armazenará a trajetória do caminho atual mais conhecido para cada nó
    :return: (dict) shortest_path = armazenará o custo conhecido de visitar cada vértice a partir do start_node, o custo vai acumulando a medida que avança no grafo. 
    """
    unvisited_nodes = list(graph.get_nodes())

    shortest_path = {}

    previous_nodes = {}

    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value

    shortest_path[start_node] = 0

    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + \
                graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value

                previous_nodes[neighbor] = current_min_node

        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


def print_result(previous_nodes, shortest_path, start_node, target_node):
    """Receberá dois dicts retornados pela função dijkstra, bem como os nomes dos nós inicial e destino. \
        A função usará os dois dicts para encontrar o melhor caminho e calcular a pontuação total do caminho.

    :param previous_nodes: (dict)
    :param shortest_path: (dict)
    :param start_node: (str)
    :param target_node: (str)
    """
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    path.append(start_node)

    print("Foi encontrado o seguinte melhor caminho com valor de {}.".format(
        shortest_path[target_node]))
    print(" -> ".join(reversed(path)))


def print_graph():
    """Imprimi o grafo indicando cada nó com sua respectiva dict com suas ligações a outros nós \

    Exemplo: Nó::H {'G': 8.0, 'B': 32.0, 'C': 8.0}
    """
    for node in nodes:
        print("Nó" + "::" + node)
        print(init_graph[node])


def edge_weight(max_fluxo, uso, potencia_sinal):
    """Função para definir a equação que irá definir o peso da aresta, tal equação irá levar \
    em consideração o trafego da rede e sua porcentagem de uso como também a potencia do sinal que \
    influenciará na largura de banda (Mbps).

    :param max_fluxo: (float)
    :param uso: (float)
    :param potencia_sinal: (float)
    :return: (float) peso final = ((max_fluxo * uso) / bandwidth)
    """
    match potencia_sinal:
        case 1:
            bandwidth = 10
            return ((max_fluxo * uso) / bandwidth)
        case 2:
            bandwidth = 25
            return ((max_fluxo * uso) / bandwidth)
        case 3:
            bandwidth = 50
            return ((max_fluxo * uso) / bandwidth)


# Criando o grafo
nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]

init_graph = {}
for node in nodes:
    init_graph[node] = {}

# 1000mb trafego ; 20% sendo usado; 2 de pontencia de sinal
init_graph["A"]["B"] = edge_weight(1000, 0.2, 2)
init_graph["A"]["C"] = edge_weight(1000, 0.2, 2)
init_graph["A"]["D"] = edge_weight(1000, 0.2, 1)

init_graph["D"]["B"] = edge_weight(1000, 0.2, 1)
init_graph["D"]["E"] = edge_weight(1000, 0.8, 3)

init_graph["C"]["B"] = edge_weight(1000, 0.2, 3)
init_graph["C"]["H"] = edge_weight(1000, 0.2, 2)

init_graph["E"]["B"] = edge_weight(1000, 0.2, 1)
init_graph["E"]["F"] = edge_weight(1000, 0.8, 2)

init_graph["F"]["G"] = edge_weight(1000, 0.8, 3)
init_graph["F"]["B"] = edge_weight(1000, 0.2, 2)

init_graph["H"]["G"] = edge_weight(1000, 0.2, 2)
init_graph["H"]["B"] = edge_weight(1000, 0.8, 2)

init_graph["B"]["G"] = edge_weight(1000, 0.8, 2)

graph = Graph(nodes, init_graph)
print_graph()

previous_nodes, shortest_path = dijkstra_algorithm(
    graph=graph, start_node="D")
print("\n")
print_result(previous_nodes, shortest_path,
             start_node="D", target_node="G")
