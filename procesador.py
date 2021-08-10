
#Funcion que abre y lee y retorna el texto de un archivo
def readFile(path):
    file1 = open(path,"r")
    return file1.read()

def takePath():
    path = input("Indique el path donde se encuentra su archivo: ")
    return path

path = takePath()
text = readFile(path)

print(text)
