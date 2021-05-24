from os import system
from os import path
import time

def getsource():
    ruta = path.dirname(path.abspath(__file__)) #Obtiene la ruta del script en ejecución
    #print("lo que obtengo ",ruta)
    return ruta

def mimetodo(di):
    try:
        time.sleep(2)
        system (di)
        print(" >>> Grafo generado exitosamente...")
    except:
        print("Error al generar png")
    
def grafo(estados, enlaces):
    ruta = getsource()
    nombre = ruta + "\\afdMinimo"
    file = open(nombre + ".dot", "w")
    file.close()
    
    escrituranorm("digraph d{", nombre)
    escrituranorm("\trankdir = LR", nombre)
    escrituranorm("\tgraph [dpi = 300];", nombre)
    
    for n in estados:
        if n[1] == True:
            log = "\tS" + str(n[0]) + "[shape=\"doublecircle\"];"
        else:
            log = "\tS" + str(n[0]) + "[shape=\"circle\"];"
        escrituranorm(log, nombre)

    for en in enlaces:
        log = "\tS" + str(en[0]) + " -> S" + str(en[1]) + " [label=\"" + str(en[2]) + "\"];"
        escrituranorm(log, nombre)

    
    log = "}"
    escrituranorm(log, nombre)
    
    generagraf(nombre)
    
def generagraf(nombre):
    di = "dot -Tpng " +  nombre + ".dot -o " + nombre + "-grafo.png"
    #print(di)
    mimetodo(di)
    openGraf(nombre)

    
def escrituranorm(log, nombre):
    file = open(nombre + ".dot", "a")
    file. write(log + "\n")
    file. close()

def openGraf(name):
    di = "start " + name + "-grafo.png"
    try:
        time.sleep(2)
        system (di)
    except:
        print("Error al abrir grafo")