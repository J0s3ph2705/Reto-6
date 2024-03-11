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
