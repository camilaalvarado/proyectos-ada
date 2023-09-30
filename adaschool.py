#Define una variable de cada tipo de primitivo
numero = 5
flotante = 4.5
maestro = True
cadena = "str"
#Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable
concatena = cadena + " "+ str(numero) + " "+  str(flotante) +" "+ str(maestro)
print (concatena)
#el limite de un entero es:  ,
#Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable
n = 20
resultado = 0
for i in range (2,n+1,2):
    resultado += i
print(resultado)