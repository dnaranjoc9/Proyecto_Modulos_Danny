# Proyecto: [Modulos y funciones Python]
# Estudiante: [Danny Josué Naranjo Campos]
# Fecha de Inicio: [22/08/2025]
# Fecha de Entrega: [28/10/2025]
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.
#from analisis_datos.carga_datos import generar_lista_compras
#from analisis_datos.estadisticas import media

from analisis_datos import *

def saludar():
    print("¡Hola! desde la Función")
    
if __name__ == "__main__":
    compras = generar_lista_compras()
    print(compras)
    media = media(list(compras.values()))
    print("Promedio de precios por articulo es: ", media)
    
    mediana = mediana(list(compras.values())) 
    print("Mediana de precios por articulo es: ", mediana)
    