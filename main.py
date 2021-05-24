import muestraReduc

tablaSiguiente = [
    ["a", 1, [3,4,5]],
    ["b", 2, [3,4,5]],
    ["c", 3, [3,4,5]],
    ["a", 4, [1,2,6,8,10]],
    ["b", 5, [1,2,6,8,10]],
    ["a", 6, [7]],
    ["c", 7, [1,2,6,8,10]],
    ["a", 8, [9]],
    ["b", 9, [1,2,6,8,10]],
    ["#", 10, []]
]

inicio = [0, [1,2,6,8,10]]

muestraReduc.runReduce(tablaSiguiente, inicio)


# ----- ESTRUCTURA ~ EJEMPLO ---------------

# tablaSiguiente = [      
#     ["L", 1, [2,3,4,8]],
#      simbolo, numeroNodo, siguientes
#     [  "L",        2,      [2,3,4,8]   ],
#     ["D", 3, [2,3,4,8]],
#     ["_", 4, [2,3,4,8]],
#     ["D", 5, [5,6]],
#     [".", 6, [7]],
#     ["D", 7, [7,8]],
#     ["#", 8, []],
# ]

#           #Estado, Conjunto de la raíz
# inicio = [    0,         [1,5]          ]      Preferiblemente el estado siempre será 0
