import random


def optimizacion_aleatoria(Diccionario):
    lista_solucion = []
    random_list = list(Diccionario)
    random.shuffle(random_list)
    colecion = set([])
    for i in random_list:
        last_action = colecion
        colecion = colecion | Diccionario[i]
        if  colecion == last_action:
            return lista_solucion
        else:
            lista_solucion.append(i) 












if "__main__"==__name__:

    lista_estaciones = {"kone":{"ID","NV","UT"},"ktwo":{"WA","ID","MT"},"kthree":{"OR","NV","CA"},"kfour":{"NV","UT"},"kfive":{"CA","AZ"},"ksix":{"NM","TX","OK"},"kseven":{"OK","KS","CO"},"keight":{"KS","CO","NE"},"knine":{"NE","SD","WY"},"kten":{"ND","IA"},"keleven":{"MN","MO","AR"},"ktwelve":{"LA"},"kthirteen":{"MO","AR"}}
    
    resultado_minimo_local = optimizacion_aleatoria(lista_estaciones)

    print(f"Este seria el resultado aplicando un algoritmo que busca minimos locales : {resultado_minimo_local}")
    
    