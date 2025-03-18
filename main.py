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



def optimizacion_global(Diccionario):
    lista_solucion = []
    posible_mejora = True
    lista_con_estaciones = list(Diccionario)
    
    lista_de_valor = []
    colecion = set()
    while posible_mejora:
        lista_de_valor,posible_mejora = calcular_valor_emisoras(colecion,list(Diccionario.values()))
        siguiente_estacion = 0

        if posible_mejora:
            posicion_lista = 0
            for i in range(len(lista_de_valor)):
                if lista_de_valor[i] > siguiente_estacion:
                    siguiente_estacion = lista_de_valor[i]
                    posicion_lista = i
                
            estacion_a_añadir = lista_con_estaciones[posicion_lista]        
            colecion = colecion | Diccionario[estacion_a_añadir]           
            lista_solucion.append(estacion_a_añadir)
    return lista_solucion    




def calcular_valor_emisoras(contratadas,potenciales):
    lista_de_valor = []
    potencial = False
    for i in potenciales:
       valor =  len(i - contratadas)
       if valor > 0:
           potencial = True
       lista_de_valor.append(valor)
    return lista_de_valor,potencial    






if "__main__"==__name__:

    lista_estaciones = {"kone":{"ID","NV","UT"},"ktwo":{"WA","ID","MT"},"kthree":{"OR","NV","CA"},"kfour":{"NV","UT"},"kfive":{"CA","AZ"},"ksix":{"NM","TX","OK"},"kseven":{"OK","KS","CO"},"keight":{"KS","CO","NE"},"knine":{"NE","SD","WY"},"kten":{"ND","IA"},"keleven":{"MN","MO","AR"},"ktwelve":{"LA"},"kthirteen":{"MO","AR"}}
    
    resultado_minimo_local = optimizacion_aleatoria(lista_estaciones)

    #print(f"Este seria el resultado aplicando un algoritmo que busca minimos locales : {resultado_minimo_local}")
    
    resultado_minimo_global = optimizacion_global(lista_estaciones)

    print(resultado_minimo_global)
    