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
