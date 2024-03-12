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
