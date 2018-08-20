# простые задачи на графы
import networkx as nx
import matplotlib.pyplot as plt

color_list = ['red', 'green', 'blue', 'orange', 'magenta', 'pink', 'cyan']


def input_edges_list():
    """получает список рёбер в форме
    в первой строке N - число рёбер
    затем следует N строк из 2 слов и одного числа
    слова - названия вершин, концы ребра, а число - его вес
    return граф в форме словаря словарей смежности с весами
    """

    for i in range(N):
         N = int(input('Введите количество рёбер: '))
         vertex1, vertex2, weight = input().split()
         weight = float(weight)
         G[vertex1][vertex2] = weight
    return G

def edges_list_to_adjacency_list(E):
    """G - граф в форме словаря рёбер и соответствующих им весов
    :return граф в форме словаря словарей смежности с весами
    """
    G = {}
    for vertex1, vertex2 in E:
        weight = E[(vertex1, vertex2)]
        # добавляю ребро (vertex1, vertex2)
        if vertex1 not in G:
            G[vertex1] = {vertex2: weight}
        else:  # такая вершина уже встречалась
            G[vertex1][vertex2] = weight
        # граф не направленный, поэтому добавляем ещё и "обратный ход" по ребру
        # (vertex2, vertex1)
        if vertex2 not in G:
            G[vertex2] = {vertex1: weight}
        else:  # такая вершина уже встречалась
            G[vertex1][vertex2] = weight
    return G

#обход в глубину
def dfs(G, start, called = set(), ostov = set()):
    called.add(start)
    for neighbour in G[start]:
        if neighbour not in called:
            dfs(G, neighbour, called, ostov)
            ostov.add((start, neighbour))

s = """L B 1
B D 1
B C 2
G J 7
V W 2
N M 2
C L 2
O D 3
G R 1
R T 2
N S 2
Y W 5""".split('\n')
E = {}
for line in s:
    a, b, weight = line.split()
    E[(a, b)] = int(weight)

A = edges_list_to_adjacency_list(E)

called = set()
ostov = set()
G = nx.Graph(A)

position = nx.spring_layout(G) #для всех листов
nx.draw(G, position)
count_components = 0

for vertex in A:
    if vertex in called:
        continue
    else:
        # vertex ещё не встречалась ни в одной обойдённой компоненте связности
        skelet = set()
        dfs(A, vertex, called, ostov)
        nx.draw_networkx_edges(G, position, edgelist=ostov,
                                     width=5, alpha=0.5,
                                     edge_color=color_list[count_components])
        count_components += 1

print('Количество компонент связности ', count_components)
plt.show()

