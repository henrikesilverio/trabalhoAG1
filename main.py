arquivo = open("palavras.txt")

linhas = arquivo.readlines()
palavras = linhas[0].split()
listaDeAdjacencia = {}


def diferemEmUmaPosicao(primeiro, segundo):
    diferenca = 0
    for caractere in primeiro:
        if caractere in segundo:
            continue
        diferenca += 1

    return diferenca <= 1

# Construindo o grafo


for palavra in palavras:
    listaDeAdjacencia[palavra] = []
for chave in listaDeAdjacencia:
    for palavra in palavras:
        if chave != palavra and diferemEmUmaPosicao(chave, palavra):
            listaDeAdjacencia[chave].append({
                palavra: {"cor": "branco",
                          "pred": {},
                          "inicio": 0,
                          "termino": 0}
            })

# Busca em profundidade

def DFSVisit(vertice, tempo):
    chave in vertice
    tempo += 1
    vertice.cor = "cinza"
    vertice.inicio = tempo
    for adjacente in listaDeAdjacencia[chave]:
        if adjacente.cor == "branco":
            adjacente.pred = vertice
            DFSVisit(adjacente)
    vertice.cor = "Preto"
    tempo += 1
    vertice.termino = tempo

def DFS(grafo, verticeInicial):
    tempo = 0
    for chave in listaDeAdjacencia:
        for vertice in listaDeAdjacencia[chave]
        if listaDeAdjacencia[chave]
