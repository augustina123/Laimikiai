from dataclasses import dataclass 
@dataclass 
class Laimikis: 
  pav: str 
  kg: int 
  gylis: float 
  val: int 
def skaityti ():  
  l=[] 
  with open("laimikiai.csv", encoding-"utf-8") as fd: 
    fd.readline()
    for eil in fd: 
      if eil.strip() == "" 
        continue 
      d=eil.strip().split(",") 
      gylis=float(d[2]) if d[2] != "" else –1.0 
      l.append.(Laimikis(d[0], int(d[1]), gylis, int(d[3]))) 
  return l 
l= skaityti() 
print(f"irasu: {len(1)}, 3 iraso gylis: {1[2].gylis;g}) 
