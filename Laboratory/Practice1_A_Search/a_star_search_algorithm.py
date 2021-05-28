'''
TAREFA 1 - A*

Diego Santos Gonçalves - 20183012537
Mariana Bulgarelli Alves dos Santos - 20183000330
'''

import networkx as nx
import time

def cria_grafo():
    #Inicialmente, cria-se o grafo com as cidades e adicionam-se arestas de acordo com o enunciado da atividade 
    grafo_cidades = nx.Graph()
    grafo_cidades.add_edge("Arad","Zerind", weight=75, visitado= False)
    grafo_cidades.add_edge("Arad","Sibiu", weight=140, visitado= False)
    grafo_cidades.add_edge("Arad","Timisoara", weight=118, visitado= False)
    grafo_cidades.add_edge("Timisoara","Lugoj", weight=111, visitado= False)
    grafo_cidades.add_edge("Sibiu","Oradea", weight=151, visitado= False)
    grafo_cidades.add_edge("Oradea","Zerind", weight=71, visitado= False)
    grafo_cidades.add_edge("Sibiu","Fagaras", weight=99, visitado= False)
    grafo_cidades.add_edge("Sibiu","Rimnicu Vilcea", weight=80, visitado= False)
    grafo_cidades.add_edge("Lugoj","Mehadia", weight=70, visitado= False)
    grafo_cidades.add_edge("Rimnicu Vilcea","Craiova", weight=146, visitado= False)
    grafo_cidades.add_edge("Rimnicu Vilcea","Pitesti", weight=97, visitado= False)
    grafo_cidades.add_edge("Fagaras","Bucareste", weight=211, visitado= False)
    grafo_cidades.add_edge("Pitesti","Bucareste", weight=101, visitado= False)
    grafo_cidades.add_edge("Pitesti","Craiova", weight=138, visitado= False)
    grafo_cidades.add_edge("Mehadia","Drobeta", weight=75, visitado= False)
    grafo_cidades.add_edge("Drobeta","Craiova", weight=120, visitado= False)
    grafo_cidades.add_edge("Bucareste","Giurgiu", weight=90, visitado= False)
    grafo_cidades.add_edge("Bucareste","Urziceni", weight=85, visitado= False)
    grafo_cidades.add_edge("Urziceni","Hirsova", weight=98, visitado= False)
    grafo_cidades.add_edge("Urziceni","Vaslui", weight=142, visitado= False)
    grafo_cidades.add_edge("Hirsova","Eforie", weight=86, visitado= False)
    grafo_cidades.add_edge("Vaslui","Iasi", weight=92, visitado= False)
    grafo_cidades.add_edge("Iasi","Neamt", weight=87)
    return grafo_cidades


def define_heuristica():
    # Criacao de um dicionario para armazenar as distancias em linha reta ate Bucareste - heuristica
    dist_bucareste = dict()
    dist_bucareste["Arad"] = 366
    dist_bucareste["Bucareste"] = 0
    dist_bucareste["Craiova"] = 160
    dist_bucareste["Drobeta"] = 242
    dist_bucareste["Eforie"] = 161
    dist_bucareste["Fagaras"] = 176
    dist_bucareste["Giurgiu"] = 77
    dist_bucareste["Hirsova"] = 151
    dist_bucareste["Iasi"] = 226
    dist_bucareste["Lugoj"] = 244
    dist_bucareste["Mehadia"] = 241
    dist_bucareste["Neamt"] = 234
    dist_bucareste["Oradea"] = 380
    dist_bucareste["Pitesti"] = 100
    dist_bucareste["Rimnicu Vilcea"] = 193
    dist_bucareste["Sibiu"] = 253
    dist_bucareste["Timisoara"] = 329
    dist_bucareste["Urziceni"] = 80
    dist_bucareste["Vaslui"] = 199
    dist_bucareste["Zerind"] = 374
    return dist_bucareste

'''
O algoritmo inicia no no correspondente a cidade de Arad. Busca-se chegar a Bucareste considerando a seguinte funcao de avaliacao a cada abertura de caminho:
f(n) = g(n) + h(n)
Onde g(n) eh o custo ate alcancar o no n ate o momento e h(n) eh a heuristica de distancia em linha reta.
A partir de f, escolhe-se o caminho no qual f eh menor. Para isso, sao abertos todos os caminhos existentes a partir do no atual e realizada a comparacao do valor de f entre eles.
Apos a escolha do menor, outros caminhos sao abertos e, novamente, o f eh comparado. Importante dizer que os caminhos anteriores nao sao descartados, sendo avaliados a cada nova abertura com relacao ao valor de f.
'''
def main():
    grafo_cidades = nx.Graph()
    dist_bucareste = dict()
    grafo_cidades = cria_grafo()
    dist_bucareste = define_heuristica()
    sorted(dist_bucareste.items(),key=lambda x: x[1])
    no_atual = "Arad"
    no_final = "Bucareste"
    list_cidades = [no_atual]
    distancia = 0
    lista_caminhos = []
    caminho_escolhido = ([no_atual],0)

    while True:
        f = caminho_escolhido[1] + dist_bucareste[no_atual]
        print("No atual: ",no_atual)
        print("f: ",f)
        print("g: ",caminho_escolhido[1])
        print("h: ",dist_bucareste[no_atual])
        print()

        # verifica se o nó atual eh o final. Se sim, sai do while
        if (no_atual == no_final):
            break
        
        for n in grafo_cidades.neighbors(no_atual):
            caminho = caminho_escolhido[0].copy()
            caminho.append(n)
            lista_caminhos.append((caminho, caminho_escolhido[1] + grafo_cidades.get_edge_data(no_atual,n)['weight']))

        lista_caminhos = sorted(lista_caminhos ,key=lambda x: x[1] + dist_bucareste[x[0][-1]])
        caminho_escolhido = lista_caminhos[0]
        del(lista_caminhos[0])

        print(f'Nó escolhido: {caminho_escolhido[0][-1]} - f: {caminho_escolhido[1]+dist_bucareste[caminho_escolhido[0][-1]]}, g: {caminho_escolhido[1]}, h: {dist_bucareste[caminho_escolhido[0][-1]]}')
        print()
        print('Demais opções:')
        for n in lista_caminhos:
            print(f'{n[0][-1]} - f: {n[1]+dist_bucareste[n[0][-1]]}, g: {n[1]}, h: {dist_bucareste[n[0][-1]]}')
        print("======================================\n")
        list_cidades.append(caminho_escolhido[0][-1])
        no_atual = list_cidades[-1]

    print('\n*********')
    print(f"Caminho escolhido: {'  ->  '.join(caminho_escolhido[0])} - {caminho_escolhido[1]}")   


if __name__ == '__main__':
    inicio = time.time()
    main()
    fim = time.time()
    print(f'\nTempo de execução: {fim - inicio}')