reduccion = []  # S, [], [S#]                 s# = [simb, [union], S#]

estadosNuevos = [] # S#, []

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
    ["#", 10, []],
]

inicio = [0, [1,2,6,8,10]]

def reduceTS():
    contadorEstados = 0
    init = True
    while True:
        if init:
            init = False
            listaEtiqueta = [generaPar(x) for x in inicio[1] ] # nodo, simbolo
            union = [] #  S#
            estadosSig = [] #  S#
            simboloActual = "" # ----
            siguientes = []    # ----
            contadorSig = 0    # ----
            while len(listaEtiqueta) > 0:
                if simboloActual:
                    if contadorSig < len(listaEtiqueta):
                        evaluando = listaEtiqueta[contadorSig]
                        if simboloActual == evaluando[1]:
                            union.append(evaluando[0])
                            temp = dameSimbolos(evaluando[0])
                            for s in temp:
                                if not s in siguientes:
                                    siguientes.append(s)
                            listaEtiqueta.pop(contadorSig)
                        else:
                            contadorSig += 1
                    else:
                        siguientes.sort()
                        if siguientes == inicio[1]:
                            estadosSig.append([simboloActual, union.copy(), inicio[0]]) # --------------------------------
                        else:
                            contadorEstados += 1
                            estadosNuevos.append([contadorEstados, siguientes.copy()])
                            estadosSig.append([simboloActual, union.copy(), contadorEstados]) # --------------------------------
                        simboloActual = "" # ----
                        union.clear()    # ----
                        siguientes.clear()    # ----
                        contadorSig = 0    # ----
                else:
                    evaluando = listaEtiqueta[contadorSig]
                    if evaluando[1] != "#":
                        simboloActual = evaluando[1]
                        union.append(evaluando[0])
                        siguientes = dameSimbolos(evaluando[0])
                    listaEtiqueta.pop(contadorSig)
            if simboloActual:
                siguientes.sort()
                if siguientes == inicio[1]:
                    estadosSig.append([simboloActual, union.copy(), inicio[0]]) # --------------------------------
                else:
                    contadorEstados += 1
                    estadosNuevos.append([contadorEstados, siguientes.copy()])
                    estadosSig.append([simboloActual, union.copy(), contadorEstados]) # --------------------------------
            # Almacenar
            reduccion.append([inicio[0], inicio[1], estadosSig])
        else:
            while estadosNuevos:
                listaEtiqueta = [generaPar(x) for x in estadosNuevos[0][1] ] # nodo, simbolo
                union = [] #  S#
                estadosSig = [] #  S#
                simboloActual = "" # ----
                siguientes = []    # ----
                contadorSig = 0    # ----
                while len(listaEtiqueta) > 0:
                    if simboloActual:
                        if contadorSig < len(listaEtiqueta):
                            evaluando = listaEtiqueta[contadorSig]
                            if simboloActual == evaluando[1]:
                                union.append(evaluando[0])
                                temp = dameSimbolos(evaluando[0])
                                for s in temp:
                                    if not s in siguientes:
                                        siguientes.append(s)
                                listaEtiqueta.pop(contadorSig)
                            else:
                                contadorSig += 1
                        else:
                            siguientes.sort()
                            if siguientes == estadosNuevos[0][1]:
                                estadosSig.append([simboloActual, union.copy(), estadosNuevos[0][0]]) # --------------------------------
                                # estadosSig.append(estadosNuevos[0][0])
                            else:
                                find = False
                                for r in reduccion:
                                    if siguientes == r[1]:
                                        estadosSig.append([simboloActual, union.copy(), r[0]]) # --------------------------------
                                        # estadosSig.append(r[0])
                                        find = True
                                if not find:
                                    find = False
                                    contadorEstados += 1
                                    # if contadorEstados == 4:
                                        # print(estadosNuevos[0], "---------------------", siguientes)
                                    estadosNuevos.append([contadorEstados, siguientes.copy()])
                                    estadosSig.append([simboloActual, union.copy(), contadorEstados]) # --------------------------------
                            simboloActual = "" # ----
                            union.clear()    # ----
                            siguientes.clear()    # ----
                            contadorSig = 0    # ----
                    else:
                        evaluando = listaEtiqueta[contadorSig]
                        if evaluando[1] != "#":
                            simboloActual = evaluando[1]
                            union.append(evaluando[0])
                            # print(simboloActual)
                            siguientes = dameSimbolos(evaluando[0])
                        listaEtiqueta.pop(contadorSig)
                if simboloActual:
                    siguientes.sort()
                    if siguientes == estadosNuevos[0][1]:
                        estadosSig.append([simboloActual, union.copy(), estadosNuevos[0][0]]) # --------------------------------
                    else:
                        find = False
                        for r in reduccion:
                            if siguientes == r[1]:
                                estadosSig.append([simboloActual, union.copy(), r[0]]) # --------------------------------
                                find = True
                        if not find:
                            contadorEstados += 1
                            estadosNuevos.append([contadorEstados, siguientes.copy()])
                            estadosSig.append([simboloActual, union.copy(), contadorEstados]) # --------------------------------
                # Almacenar
                reduccion.append([estadosNuevos[0][0], estadosNuevos[0][1].copy(), estadosSig])
                estadosNuevos.pop(0)
            break
    muestraFormato()

def generaPar(n):
    for node in tablaSiguiente:
        if n == node[1]:
            return [n, node[0]]
def dameSimbolos(n):
    for node in tablaSiguiente:
        if n == node[1]:
            return node[2].copy()   
def findSet(n):
    for r in reduccion:
        if n == r[0]:
            return ", ".join([str(x) for x in r[1]])

def muestraFormato():
    for r in reduccion:
        print("S"+str(r[0]) + " = {" + ", ".join([str(x) for x in r[1]]) + "}")
        for sig in r[2]:
            print(sig[0] + ": " + "sig(" + ") U sig(".join([str(x) for x in sig[1]]) + ") = {" + findSet(sig[2]) + "}    //  S" + str(sig[2]) )
        print()

def runReduce(tS, i):
    global tablaSiguiente, inicio
    tablaSiguiente = tS
    inicio = i
    reduceTS()