from io import open_code
from os import error
import re
import unicodedata

#Funcion que abre y lee y retorna el texto de un archivo
def readFile(path):
    try:
        file1 = open(path,encoding="UTF-8")
    except IOError:
        file1 = open(path,"r")
    return file1.read()

#Funcion que solicita y toma el path digitado por el usuario
def takePath():
    path = input("Indique el path donde se encuentra su archivo: ")
    return path

#Funcion que elimina los signos de puntuacion del texto y los cambia por un espacio en blanco
def deletePunctuation(text):
    return re.sub(r'[^\w\s]',' ',text)

#Funcion que elimina los caracteres especiales, por ejemplo, las tildes
def deleteSpecialCharacters(text):
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)

#Funcion para volver todas las palabras a minuscula
def lowerCaseText(text):
    return text.lower()

#path = takePath()
path = "C:/University/Recuperacion de informacion textual/Tarea 1/University-SemesterVI-WordProcessor/pruebas/test.txt"
text = readFile(path)
text = lowerCaseText(text)
textWithoutPunctuation = deletePunctuation(text)
textWithoutSpecialCharacters = deleteSpecialCharacters(textWithoutPunctuation)

print (textWithoutSpecialCharacters)

