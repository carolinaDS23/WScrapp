
from urllib.request import urlopen 
from bs4 import BeautifulSoup


#Ciudades:
#Taskent; Mar_del_Plata; Las_Vegas
#Descubrir en que posición se encuentra la tabla de clima para algun ciudad de la lista
#¿Cualés con las filas de temperatura máx media y temperatura min media?
#Realizar un diccionario para para cada ciudad con Nombre, PosiciónTabla, Temperatura Máxima Media, Temperatura Mínima Media 
# Esto baja todo de la pagina
def bajar(laDir): 
   laPag = urlopen(laDir) 
   return BeautifulSoup(laPag.read(),features="html.parser") 
   
def leeLinea(linea):
   lista = []
   for dato in linea.find_all('td'):
      lista.append(dato.get_text())
   return lista
   
def leeTabla(tabla):
    filas = []
    for fila in tabla.find_all('tr'):
       filas.append(leeLinea(fila))
    return filas
    

def EncontrarTemperaturaMaxima(temperaturas=[]):
   maxima= float(temperaturas[0])
   for temp in temperaturas:
      if float(temp)>maxima:
         maxima=float(temp)
   return maxima

def EncontrarTemperaturaMinima(temperaturas=[]):
   minima= float(temperaturas[0])
   for temp in temperaturas:
      if float(temp)<minima:
         minima=float(temp)
   return minima



def Calcular_Diferencia_Temperatura(ciudad:any):
    miDir = f"https://es.wikipedia.org/wiki/{ciudad['nom']}"
    laSopa = bajar(miDir)
    todasLasTablas = laSopa.find_all("table")
    tablaClima = todasLasTablas[ciudad['ptabla']]
    temperaturas = leeTabla(tablaClima)
    maximaMedia=EncontrarTemperaturaMaxima(temperaturas[ciudad['tmax']])
    minimaMedia=EncontrarTemperaturaMinima(temperaturas[ciudad['tmin']])
    diferencia= maximaMedia-minimaMedia
    print(f"La diferencia de temperaturas medias en {ciudad['nom']} es de {round(diferencia,1)}")


lista_de_ciudades = [
    {'nom': 'Taskent', 'ptabla': 1, 'tmax': 3, 'tmin':5},
    {'nom': 'Mar_del_Plata', 'ptabla': 8, 'tmax': 3, 'tmin':5},
    {'nom': 'Las_Vegas', 'ptabla': 3, 'tmax': 3, 'tmin':5},
    {'nom': 'San_Juan_(Puerto_Rico)', 'ptabla': 3, 'tmax': 3, 'tmin':5},
    {'nom': 'Neuquen_(ciudad)', 'ptabla': 5, 'tmax': 3, 'tmin':5},
    {'nom': 'Alma_Ata', 'ptabla': 4, 'tmax': 3, 'tmin':5},
   #  {'nom': 'Salta', 'ptabla': 1, 'tmax': 2, 'tmin':4},
    {'nom': 'Kasgar', 'ptabla': 1, 'tmax': 1, 'tmin':2},    
]
# Esto itera por ciudades del arreglo
for ciudad in lista_de_ciudades:
   Calcular_Diferencia_Temperatura(ciudad)


   



def Calcular_Diferencia_Temperatura(ciudad):
   miDir = f"https://es.wikipedia.org/wiki/{ciudad['nom']}"
   laSopa = bajar(miDir)
   todasLasTablas = laSopa.find_all("table")
   try:
       tablaClima = todasLasTablas[ciudad['ptabla']]
       temperaturas = leeTabla(tablaClima)
       maximaMedia = EncontrarTemperaturaMaxima(temperaturas[ciudad['tmax']])
       minimaMedia = EncontrarTemperaturaMinima(temperaturas[ciudad['tmin']])
       diferencia = maximaMedia - minimaMedia
       print(f"La diferencia de temperaturas medias en {ciudad['nom']} es de {round(diferencia, 1)}")
   except (IndexError, KeyError) as e:
       raise ValueError(f"No se pudo encontrar información climática para {ciudad['nom']}") from e


def funcion(listaCiudades):  
    for ciudad in listaCiudades:         
        try:
            Calcular_Diferencia_Temperatura(ciudad)
        except ValueError as ve:
            print("Ocurrió un error:", ve)

funcion(lista_de_ciudades)
