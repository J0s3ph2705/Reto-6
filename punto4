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
