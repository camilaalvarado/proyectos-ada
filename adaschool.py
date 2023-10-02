#Define una variable de cada tipo de primitivo
numero = 5
flotante = 4.5
maestro = True
cadena = "str"
#Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable
concatena = cadena + " "+ str(numero) + " "+  str(flotante) +" "+ str(maestro)
print (concatena)
#Investigación
#Los enteros en Python no tienen un límite fijo. El límite es la memoria disponible, Para conocer el límite en tu sistema, puedes utilizar sys.maxsize o sys.maxint.
#Los flotantes en Python siguen el estándar IEEE 754 y tienen límites definidos. El límite superior es aproximadamente 1.8 x 10^308, y el límite inferior es aproximadamente -1.8 x 10^308
#Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable
n = 20
resultado = 0
for i in range (2,n+1,2):
    resultado += i
print(resultado)