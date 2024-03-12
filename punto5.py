def valor(c:float,i:float,n:float) -> float:
  return (c*i/1200*n)+c
if __name__ == "__main__":
    c=float(input("Valor del préstamo? "))
    i=float(input("Interés? "))
    n=float(input("Meses? "))
    total = valor(c,i,n)
    print("El costo total es de "+str(total)+" pesos")
