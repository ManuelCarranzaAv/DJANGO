from django.shortcuts import render #libreria para reconocer el request(front del usuario)
from django.http import HttpResponse #permite morstar en pantalla el resultado


#EJERCICIO 1:
#Hallar la suma de los 10 primeros numeros
def ejerciciosfor(request,*cadena,**cadenaID):
    n=10
    a=0
    for  i in range(n+1):
        a=a+i
    print(a)

#ejercicio 2:
#Contar la cantidad de vocales en la palabra Murcielago
    texto = "murcielago"
    vocales = "aeiouAEIOU"
    ara=0
    for i in texto:
        if i in vocales:
            ara=ara+1
        print(ara)

#EJERCICIOS 3:
#Hallar los 30 numeros pares
    pares=[]
    for i in range(2,31):
        if i%2==0 :
            pares.append(i)

#EJERCICIO4:
#Hallar los multiplos de 3 entre el rango 3-50
    multiplo=[]
    for i in range (3,51):
        if i % 3 == 0:
            multiplo.append(i)

#ejercicio 5
#Imprimir los multiplicados por 12 en el rango 1-12
    tabla = 12
    e= []
    for i in range (1,13):
        e.append(i*tabla)

#font-wight: bolder
#font-wight: italic
#EJERCICIO 6
#Suma de números enteros hasta el 20 usando while
    numero = 20
    suma = 0
    i = 1
    while i <= 20:
        suma += i
        i += 1
        
#EJERCICIO 7
#Realizar una tabla de multiplicar hasta el numero 13 con while
    tabla = []
    numero = 13
    i = 1
    while i <= 13:
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
        tabla.append(str(numero) +" " +"x"+ " "+str(i)+ "=" +str(resultado))
        i += 1
        
#EJERCICIO 8
#Imprimir los 10 primeros numeros naturales con while
    acum_num = []
    i = 1
    while i <=10: 
        acum_num.append(i)
        i += 1  
        
#EJERCICIO 9
#Imprimir 10 numeros de la serie de Fibonacci 
    fibonacci = []
    n = 10
    a, b = 0, 1
    i = 0
    while i < n:
        print(a)
        a, b = b, a + b
        fibonacci.append(a)
        i += 1
        
#EJERCICIO 10
#Hallar la cantidad de "o" que hay en la palabra "hola mundo"
    cadena = "Hola mundo"
    letra = "o"
    contador = 0
    i = 0
    while i < len(cadena):
        if cadena[i] == letra:
            contador += 1
        i += 1
    print(contador)
    
#EJERCICIO 11
#Hallar la factorial de 5 usando el do while   
    fact = 1
    num = 5
    while num > 0:
        fact *= num
        num -= 1
        
    dowhile = fact
    
#EJERCICIO 12
#Hacer un tabla que multplique por 6 hasta que llegue al numero 5 usando dowhile
    tabla1 = []
    n = 6
    i = 1
    while i <= 10:
        resultado = n*i 
        print(f"{n} x {i} =  {resultado}")
        tabla1.append(str(n)+" "+"x"+" "+str(i) +"="+ str(resultado))
        if i >= 5:
            break
        i = i + 1
        
#EJERCICIO 13
#Imprimir los solo los numeros impares del 1 al 10 usando el do while
    impar=[]
    num = 0
    while num < 10:
        num += 1
        if (num % 2) == 0:
            continue
        impar.append(num)
        
#EJERCICIO 14
#Contar hacia atras desde 20 hasta que se detenga en 4
    cuenta =[]
    i = 21
    while i > 0:
            i -= 1
            if i == 4:
                break
            cuenta.append(i)

#EJERCICIO 15
#Contar hacia atras desde 10 hasta llegar al 0, saltando el 5
    cuenta2 =[]
    i = 11
    while i > 0:
            i -= 1
            if i == 5:
                continue
            cuenta2.append(i)
            
    return render(request,'ejercicio1.html',{'a':a,'be': ara,'par': pares,
    'tercia': multiplo,'tabla':e, 'while1':suma,'while2':tabla,'while3':acum_num,
    'while4':fibonacci,'while5':contador, 'dowhile1':dowhile, 'dowhile2':tabla1, 
    'dowhile3':impar, 'dowhile4':cuenta,'dowhile5':cuenta2}) 