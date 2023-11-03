
# Proyecto Integrador parte 2

#Investigrar cómo leer un caracter del teclado
#Si queremos leer un solo carácter desde teclado podemos hacerlo de dos formas: 
#Utilizando el método next() o nextLine()  de Scanner. 
#Ulilizando el método System.in.read(); Este método no pertenece a la clase Scanner.


#Escribir un programa que corra un bucle infinito leyendo e imprimiento las teclas 
#y sólo terminará cuando se presione la tecla ↑ indicada como UP


from readchar import readkey, key

print("Hola, está apunto de comenzar tú aventura!!!")
print("Presiona ↑ (UP) para terminar el juego")
while True:
    tecla = readkey()
    if tecla == key.UP:
        print("Acabó el juego, oprimiste la tecla UP")
        break
    print(tecla)