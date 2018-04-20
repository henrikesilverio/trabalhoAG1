arquivo = open("palavras.txt")

palavras = arquivo.read().split("\n")
grafo = []
tempo = 0

# Construindo o grafo


def diferemEmUmaPosicao(primeiro, segundo):
    diferenca = 0
    for i in range(0, len(primeiro)):
        if primeiro[i] == segundo[i]:
            continue
        diferenca += 1

    return diferenca <= 1


for palavra in palavras:
    grafo.append({
        "nome": palavra,
        "cor": "branco",
        "pred": {},
        "inicio": 0,
        "termino": 0,
        "adjacentes": []
    })

for i in range(0, len(grafo)):
    for j in range(0, len(grafo)):
        if grafo[i]["nome"] != grafo[j]["nome"] and diferemEmUmaPosicao(grafo[i]["nome"], grafo[j]["nome"]):
            grafo[i]["adjacentes"].append(grafo[j])

# Busca em profundidade


def DFSVisit(vertice):
    global tempo
    tempo += + 1
    vertice["cor"] = "cinza"
    vertice["inicio"] = tempo
    for adjacente in vertice["adjacentes"]:
        if adjacente["cor"] == "branco":
            adjacente["pred"] = vertice
            DFSVisit(adjacente)
    vertice["cor"] = "Preto"
    tempo += 1
    vertice["termino"] = tempo


def DFS(grafo, verticeInicial):
    for vertice in grafo:
        if vertice["cor"] == "branco":
            DFSVisit(vertice)

DFS(grafo, grafo[0])
