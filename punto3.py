def masa(n:float,m:float,k:float) -> float:
  return n*6+m*7+k*1
if __name__ == "__main__":
    n=float(input("Cantidad de gallinas? "))
    m=float(input("Cantidad de gallos? "))
    k=float(input("Cantidad de pollitos? "))
    masa_total = masa(n,m,k)
    print("La masa total es "+str(masa_total)+" kilogramos")
