from urllib.request import urlopen 
from bs4 import BeautifulSoup


def bajar(laDir): 
   laPag = urlopen(laDir) 
   return BeautifulSoup(laPag.read()) 
   
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
   máximo=temperaturas[0]
   for temp in temperaturas:
      if temp>máximo:
         máximo=temp
   return máximo

def EncontrarTemperaturaMinima(temperaturas=[]):
   minima=temperaturas[0]
   for temp in temperaturas:
      if temp<minima:
         minima=temp
   return minima
#Ciudades:
#Taskent; Mar_del_Plata; Las_Vegas
#Descubrir en que posición se encuentra la tabla de clima para algun ciudad de la lista
#¿Cualés con las filas de temperatura máx media y temperatura min media?
#Realizar un diccionario para para cada ciudad con Nombre, PosiciónTabla, Temperatura Máxima Media, Temperatura Mínima Media 

# lista [{nom:"Taskent"; ptabla : 1; tmax: 3; tmin : 5},{nom:"Mar_del_Plata"; ptabla : 8; tmax: 3; tmin : 5},{nom:"Las_Vegas"; ptabla : 3; tmax: 3; tmin : 5}].
#

miDir = "https://es.wikipedia.org/wiki/Las_Vegas"
laSopa = bajar(miDir)
todasLasTablas = laSopa.find_all("table")
tablaClima = todasLasTablas[3]
temperaturas = leeTabla(tablaClima)

maximaMedia=EncontrarTemperaturaMaxima(temperaturas[3])
minimaMedia=EncontrarTemperaturaMinima(temperaturas[5])
print(minimaMedia,maximaMedia)
diferencia= round(float(maximaMedia)-float(minimaMedia))
print(f"La diferencia de temperaturas es de {diferencia}")

   




