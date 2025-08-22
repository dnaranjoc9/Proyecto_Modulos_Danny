# estadisticas.py
def media(datos):
   media_arimetica = sum(datos) / len(datos)
   return media_arimetica

def mediana(datos):
   #mediana
   #Paso #1 Ordenar
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    mitad = n // 2
    if n % 2 == 0:
        mediana = (datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2 
    else:
        mediana = datos_ordenados[mitad]
    return mediana

if __name__ == "__main__":
   notas = [100,50,100,78,100]
   print(media(notas))