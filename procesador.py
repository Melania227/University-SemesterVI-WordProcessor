from collections import Counter
import re
import unicodedata

#Funcion que abre y lee y retorna el texto de un archivo
def readFile(path):
    try:
        with open(path, encoding='utf-8') as file:
            content=file.read()
            file.close()
    except:
        with open(path,"r") as file:
            content=file.read()
            file.close()
    return content

#Funcion que solicita y toma el path digitado por el usuario
def takePath():
    path = input("Indique el path donde se encuentra su archivo y el nombre del mismo: ")
    return path

#Funcion que elimina los signos de puntuacion del texto y los cambia por un espacio en blanco
def deletePunctuation(text):
    return re.sub(r'[^\w\s]',' ',text)

#Funcion que elimina los caracteres especiales, por ejemplo, las tildes
def deleteSpecialCharacters(text):
    text = text.replace('ñ','-&-')
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    text = text.replace('-&-','ñ')
    return str(text)

#Funcion para volver todas las palabras a minuscula
def lowerCaseText(text):
    return text.lower()

#Funcion que toma un texto y lo separa en palabras
def splitText(text):
    return text.split()

#Funcion la lista de palabras y quita duplicados
def wordsInTextList(wordList):
	return list(set(wordList))

#Funcion que toma la lista de palabras y la ordena alfabeticamente
def alphabeticOrder(list):
	list.sort()

#Funcion que toma una lista de palabras y nos devuelve otra lista que contiene cada palabra y la cantidad de veces que aparece
def wordAppearances(list):
    return Counter(list).most_common()

#Funcion que toma todas las frecuencias y las suma
def sumFrequencies(list):
    result = 0
    for i in list: 
        result+=i[1]
    return result

#Funcion que imprime y coloca en un archivo toda la informacion de manera correcta
def printResults(list, n, f):
    result = ""
    for i in list: 
        result += i[0] + "\t \t" + str(i[1]) + "\n"
    result += "Número de palabras: " + str(n) + "\n"
    result += "Frecuencia total: " + str(f) + "\n"
    print (result)
    path = input("Indique el path y el nombre donde desea que se guarde su archivo con los resultados: ")
    file = open(path, "w")
    file.write(result)
    file.close()


#Funcion principal
def wordCount(path):
    text = readFile(path)
    text = lowerCaseText(text)
    textWithoutPunctuation = deletePunctuation(text)
    textWithoutSpecialCharacters = deleteSpecialCharacters(textWithoutPunctuation)
    wordList = splitText(textWithoutSpecialCharacters)
    wordListWithoutDuplicades = wordsInTextList(wordList)
    numberOfDistincticWordsInText = len(wordListWithoutDuplicades)
    alphabeticOrder(wordList)
    alphabeticOrder(wordListWithoutDuplicades)
    wordAppearancesInText = wordAppearances(wordList)
    alphabeticOrder(wordAppearancesInText)
    frequencies = sumFrequencies(wordAppearancesInText)

    printResults(wordAppearancesInText, numberOfDistincticWordsInText, frequencies)

path = takePath()
wordCount(path)