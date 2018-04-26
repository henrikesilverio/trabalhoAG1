arquivo = open("palavras.txt")

palavras = arquivo.read().split("\n")
grafo = {}
tempo = 0
componentes_conexos = 0

# Construindo o grafo


def diferemEmUmaPosicao(primeiro, segundo):
    diferenca = 0
    for i in range(0, len(primeiro)):
        if primeiro[i] == segundo[i]:
            continue
        diferenca += 1

    return diferenca <= 1


for palavra in palavras:
    grafo[palavra] = {
        "nome": palavra,
        "cor": "branco",
        "distancia": 999999999,
        "tempo_inicio": 0,
        "tempo_termino": 0,
        "predecessor": {},
        "adjacentes": []
    }

for vertice_i in grafo.values():
    for vertice_j in grafo.values():
        if vertice_i["nome"] != vertice_j["nome"] and diferemEmUmaPosicao(vertice_i["nome"], vertice_j["nome"]):
            vertice_i["adjacentes"].append(vertice_j)

# Busca em largura
# Calcular a distancia entre duas palavras quaisquer e
# Imprimir o caminho entre elas


def WFS(grafo, verticeInicial):
    verticeInicial["cor"] = "cinza"
    verticeInicial["distancia"] = 0
    fila = []
    fila.append(verticeInicial)
    while(len(fila) != 0):
        vertice = fila.pop(0)
        for adjacente in vertice["adjacentes"]:
            if adjacente["cor"] == "branco":
                adjacente["cor"] = "cinza"
                adjacente["distancia"] = vertice["distancia"] + 1
                adjacente["predecessor"] = vertice
                fila.append(adjacente)
        vertice["cor"] = "preto"

# Imprimir o caminho do vertice inical até o vertice final


def ImprimirCaminho(verticeInicial, verticeFinal):
    if verticeFinal["nome"] == verticeInicial["nome"]:
        print(verticeInicial["nome"])
    elif not verticeFinal["predecessor"]:
        print("não existe caminho de {0} a {1}".format(
            verticeInicial["nome"], verticeFinal["nome"]))
    else:
        ImprimirCaminho(verticeInicial, verticeFinal["predecessor"])
        print(verticeFinal["nome"])


WFS(grafo, grafo[palavras[0]])
ImprimirCaminho(grafo[palavras[0]], grafo[palavras[1]])
print("a distância entre {0} a {1} e de {2}".format(grafo[palavras[0]]["nome"],
                                                    grafo[palavras[1]]["nome"],
                                                    grafo[palavras[1]]["distancia"]))

# Busca em profundidade


def DFSVisit(vertice):
    global tempo
    tempo += + 1
    vertice["cor"] = "cinza"
    vertice["tempo_inicio"] = tempo
    for adjacente in vertice["adjacentes"]:
        if adjacente["cor"] == "branco":
            adjacente["predecessor"] = vertice
            DFSVisit(adjacente)
    vertice["cor"] = "preto"
    tempo += 1
    vertice["tempo_termino"] = tempo


def DFS(grafo, verticeInicial):
    global componentes_conexos
    for vertice in grafo.values():
        vertice["cor"] = "branco"

    for vertice in grafo.values():
        if vertice["cor"] == "branco":
            componentes_conexos += 1 
            DFSVisit(vertice)


DFS(grafo, grafo[palavras[0]])
print("Numero de componentes conexos é {0}".format(componentes_conexos))
