def procesar_grupos(archivo):
    grupos = []
    arc = open(archivo, "r")
    for linea in arc:
        grupo = linea.strip().split(";")[0]
        if linea:
            grupos.append(grupo)
    arc.close()

    elementos = {}
    for grupo in grupos:
        arc = open(f"./datos/{grupo}.csv", 'r')
        for linea in arc:
            linea = linea.strip().split(";")
            informacion_elemento = linea[1:]
            informacion_elemento.insert(1, grupo)
            elementos[linea[0]] = informacion_elemento
    return elementos

def procesar_compuestos(grupos, compuestos):
    elementos = procesar_grupos(grupos)
    elementos_presentes = {}
    arc = open(f"./datos/compuestos.csv", 'r')
    for linea in arc:
        linea = linea.strip().split(";")
        compuesto = linea[1].split("-")
        for molecula in compuesto:
            elemento = ""
            i = 0
            while i < len(molecula):
                if molecula[i].isalpha():
                    elemento += molecula[i]
                    i += 1
                else:
                    i = len(molecula)
            if elemento not in elementos_presentes:
                informacion_elemento = elementos[elemento]
                informacion_elemento.insert(0, 1)
                elementos_presentes[elemento] = informacion_elemento
            else:
                elementos_presentes[elemento][0] += 1
    arc.close()
    return elementos_presentes

arc = open("./datos/resumen.txt", "w")
elementos = procesar_compuestos("./datos/grupos.csv", "./datos/compuestos.csv")
grupos = {}
for key in elementos:
    if elementos[key][2] not in grupos:
        grupos[elementos[key][2]] = [key]
    else:
        grupos[elementos[key][2]].append(key)

for key in grupos:
    arc.write(f"{key}: {len(grupos[key])}\n")
    arc.write(f"{', '.join(grupos[key])}\n")