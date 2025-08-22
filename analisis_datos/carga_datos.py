import random

def generar_lista_compras():
    compras={}
    canasta_basica = {
        'Arroz': 2000,
        'Frijoles': 1500,
        'Huevos':1300,
        'Aceite':2500,
        'Cerveza':1200,
        'Leche':1100,
        'Café':2100,
        'Chocolate':1400,
        'Atún': 500,
        'Sal':480,
        'Azucar':1250,
        'Numar': 198,
        'Pescado':6375,
        'Posta Cerdo': 3800,
        'Cereal':1200,
        'Galletas':995,
        'Pollo':2000,
        'Harina': 1050,
        'Masa':1480,
        'Coca Cola': 1400  
    }
    lista_seleccionada = random.sample(list(canasta_basica.keys()), k=5)
   
    for key in lista_seleccionada:
        compras[key] = canasta_basica[key]
    
    #print(compras)
    return compras
    
    
if __name__ == "__main__":
    generar_lista_compras()