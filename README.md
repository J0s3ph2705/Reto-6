# Reto-6

1. Dado la figura de la imagen, desarrolle:

<div align='center'>
<figure> <img src="https://i.postimg.cc/FRvCmpxx/image.png" alt="" width="400" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

+ Una función matemática para calcular el volumen y el área superficial.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r1`, `r2` y `h`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*

```python
import math
def volumen(r1:float,r2:float,h:float,pi:float) -> float:
  return (4/3*pi*r1**3)+(1/3*pi*r2**2*h)
def area(r1:float,r2:float,h:float,pi:float) -> float:
  return (4*pi*r1**2)+(pi*r2**2)+pi*r2*(r2**2+h**2)**(1/2)
if __name__ == "__main__":
    r1=float(input("Radio esfera? "))
    r2=float(input("Radio cono? "))
    h=float(input("Altura cono? "))
    pi=float(math.pi)
    volumen_total = volumen(r1,r2,h,pi)
    print("El volúmen total es "+str(volumen_total))
if __name__ == "__main__":
    area_total = area(r1,r2,h,pi)
    print("El área superficial total es "+str(area_total))
```


2. Dado la figura de la imagen, desarrolle:

<div align='center'>
<figure> <img src="https://i.postimg.cc/1t4MrzsL/image.png" alt="" width="400" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

+ Una función matemática para calcular el área y el perimetro.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r`, `a` y `b`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*

```python
import math
def perimetro(a:float,b:float,r:float,pi:float) -> float:
  return (2*a+2*b)+2*(2*pi*r)
def area(a:float,b:float,r:float,pi:float) -> float:
  return (a*b)+2*(pi*r**2)
if __name__ == "__main__":
    a=float(input("Alto del rectángulo? "))
    b=float(input("Ancho del rectángulo? "))
    r=float(input("Radio de los círculos? "))
    pi=float(math.pi)
    perimetro_total = perimetro(a,b,r,pi)
    print("El perímetro total es "+str(perimetro_total))
if __name__ == "__main__":
    area_total = area(a,b,r,pi)
    print("El área total es "+str(area_total))
```


3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```python
def masa(n:float,m:float,k:float) -> float:
  return n*6+m*7+k*1
if __name__ == "__main__":
    n=float(input("Cantidad de gallinas? "))
    m=float(input("Cantidad de gallos? "))
    k=float(input("Cantidad de pollitos? "))
    masa_total = masa(n,m,k)
    print("La masa total es "+str(masa_total)+" kilogramos")
```


4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a  3300 cada una y H huevos a  350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

```python
def valor(p:float,m:float,h:float,b:float) -> float:
  return b-(p*300+m*3300+h*350)
if __name__ == "__main__":
    p=float(input("Cantidad de panes? "))
    m=float(input("Cantidad de bolsas de leche? "))
    h=float(input("Cantidad de huevos? "))
    b=float(input("Valor del billete? "))
    vueltas = valor(p,m,h,b)
    if float(vueltas)>0:
        print("Te sobran "+str(vueltas)+" pesos")
    elif float(vueltas)==0:
        print("Llevas es dinero exacto")
    else:
        print("Quedas debiendo "+str(vueltas)+" pesos")
```

5. Haga un programa que utilice una función para calcular el valor de un préstamo `C` usando interés compuesto del `i` por `n` meses.

```python
def valor(c:float,i:float,n:float) -> float:
  return (c*i/1200*n)+c
if __name__ == "__main__":
    c=float(input("Valor del préstamo? "))
    i=float(input("Interés? "))
    n=float(input("Meses? "))
    total = valor(c,i,n)
    print("El costo total es de "+str(total)+" pesos")
```

6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

```python
def contagiados(c:float,d:float) -> float:
  return c*2**d
if __name__ == "__main__":
    c=float(input("Contagiados iniciales? "))
    d=float(input("Dias transcurridos? "))
    total_contagiados = contagiados(c,d)
    print("Los contagiados totales después de "+str(d)+" días es de "+str(total_contagiados))
```

7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
  + El promedio
  + La mediana 
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + Ordenar los números de forma ascendente
  + Ordenar los números de forma descendente
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número

```python
def promedio(a:float,b:float,c:float,d:float,e:float) -> float:
  return (a+b+c+d+e)/5
def media(a:float,b:float,c:float,d:float,e:float) -> float:
  return (a+b+c+d+e)//5
def promedio_multiplicativo(a:float,b:float,c:float,d:float,e:float) -> float:
  return (a*b*c*d*e)**(1/5)
def ascendente(a:float,b:float,c:float,d:float,e:float) -> float:
  return a,b,c,d,e
def descendente(a:float,b:float,c:float,d:float,e:float) -> float:
  return a,b,c,d,e
if __name__ == "__main__":
    a=float(input("Número 1? "))
    b=float(input("Número 2? "))
    c=float(input("Número 3? "))
    d=float(input("Número 4? "))
    e=float(input("Número 5? "))
    promedio_final=promedio(a,b,c,d,e)
    media_final=media(a,b,c,d,e)
    promedio_multiplicativo_final=promedio_multiplicativo(a,b,c,d,e)
    lista_ascendente=sorted(ascendente(a,b,c,d,e))
    lista_descendente=sorted(descendente(a,b,c,d,e),reverse=True)
    menor=float(lista_ascendente[0])
    mayor=float(lista_descendente[0])
    potencia=mayor**menor
    raiz=menor**(1/3)
    print("El promedio es "+str(promedio_final))
    print("La media es "+str(media_final))
    print("El promedio multiplicativo es "+str(promedio_multiplicativo_final))
    print("El orden ascendente es "+str(lista_ascendente))
    print("El orden descendente es "+str(lista_descendente))
    print("La potencia del número mayor a la de el menor es "+str(potencia))
    print("La raíz cúbica del número menor es "+str(raiz))
```

8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

Está arriba :)

9. Consultar qué es y cómo funciona *pip* en python.

Es un sistema que sirve para instalar y usar paquetes que hacen los usuarios a manera de código abierto.

11. Hacer un listado de módulos populares para python que se puedan instalar com *pip* y consultar cómo instalarlos.

Para instalar un programa pip, se debe tener python con una versión mayor a la 3.4, ya que en esta actualización se creo el pip e internet. En la sección de comandos se escribe:
  - pip install (Módulo o librería)
Si se tiene una versión menor, se debe instalar pip en python.

Entre los módulos más populares con pip están:
  - fibo (fibonacci)
  - math (matemáticas)
  - num.py (Números científicos)
  - Matplotlib (Gráficas)
  - Requests (HTTP)
  - BeautifulSoup (HTML)
