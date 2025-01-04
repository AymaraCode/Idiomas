import copy

# BLOQUE DE LECTURA DEL ARCHIVO
a = input("Leccion a practicar(sin extension): ")
with open(a + ".txt", "r", encoding="utf-8") as l:
    lista = l.readlines()
d = dict()
for i in range(0, len(lista), 2):
    d[lista[i].strip()] = lista[i+1].strip()


#BLOQUE DE PREGUNTAR LAS PREGUNTAS 
def preguntar():
    aux = copy.deepcopy(d)
    for esp in aux.keys():
        res = input(esp + ":\n")
        if res.strip() == d[esp]:
            print("Correcto!\n")
            d.pop(esp)
        else:
            print("Incorrecto :(\nRespuesta correcta:\n" + d[esp]+ "\n\n")
    if len(d) > 0:
        print("Otro round!!")
        preguntar()
    pass

preguntar()