
#Funcion que abre y lee y retorna el texto de un archivo
def readFile(path):
    file1 = open(path,"r")
    return file1.read()


text = readFile("C:/University/Recuperacion de informacion textual/Tarea 1/University-SemesterVI-WordProcessor/pruebas/test.txt")
print(text)
