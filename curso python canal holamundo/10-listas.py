lenguajes = ["Python", "Ruby", "PHP", "Javascript", "Java"] # lista
#              [0]      [1]     [2]        [3]        [4]   # las listas empiezan con
                                                            # un indice = 0

print(lenguajes) # ['Python', 'Ruby', 'PHP', 'Javascript', 'Java'] la lista se ve 
                 # asi en la terminal

lenguajes[1] = "Go" # cambio de uno de los elementos de la lista (segundo elemento en
                    # este caso)

print(lenguajes[-1]) # -1 selecciona el ultimo elemento de la lista, -2 el penultimo
                     # elemento, -3 el antepenultimo y asi sucesivamente (en este
                     # caso Java)

print(lenguajes[1:4]) # : entre los numeros de una lista seleciona todos los elementos
                      # empezando por el numero a la izquierda de los : y terminando
                      # por el que esta a la derecha de los : -1 (en este caso
                      # seleccionara Ruby (Go despues del cambio de elemento), PHP,
                      # Javascript y para antes de llegar
                      # al 4to elemento que es Java)