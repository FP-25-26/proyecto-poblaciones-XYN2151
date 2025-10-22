from collections import namedtuple
import matplotlib.pyplot as plt


RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero):
    with open(ruta_fichero, encoding='utf-8') as f:
        poblaciones = []
        for linea in f:
            pais, codigo, año, censo = linea.strip().split(',')
            registro = RegistroPoblacion(pais, codigo, int(año), int(censo))
            poblaciones.append(registro)
    return poblaciones

def calcula_paises(poblaciones):
    return sorted({registro.pais for registro in poblaciones})

def filtra_por_pais(poblaciones, nombre_o_codigo):
    filtrado = []
    for registro in poblaciones:
        if registro.pais == nombre_o_codigo or registro.codigo == nombre_o_codigo:
            filtrado.append((registro.año, registro.censo))
    return filtrado

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    filtrado = []
    for registro in poblaciones:
        if registro.año == anyo and (registro.pais in paises):
            filtrado.append((registro.pais, registro.censo))
    return filtrado

def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    datos = filtra_por_pais(poblaciones, nombre_o_codigo)
    lista_años, lista_censos = [], []
    for l in datos:
        lista_años.append(l[0])
        lista_censos.append(l[1])
    plt.title(f"Evolución de la población de {nombre_o_codigo}")
    plt.plot(lista_años, lista_censos)
    plt.show()

def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    datos = filtra_por_paises_y_anyo(poblaciones, anyo, paises)
    lista_paises, lista_censos = [], []
    for l in datos:
        lista_paises.append(l[0])
        lista_censos.append(l[1])
    plt.title(f"Comparativa de población en {anyo}")
    plt.bar(lista_paises, lista_censos)
    plt.show()




