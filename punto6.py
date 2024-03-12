def contagiados(c:float,d:float) -> float:
  return c*2**d
if __name__ == "__main__":
    c=float(input("Contagiados iniciales? "))
    d=float(input("Dias transcurridos? "))
    total_contagiados = contagiados(c,d)
    print("Los contagiados totales después de "+str(d)+" días es de "+str(total_contagiados))
