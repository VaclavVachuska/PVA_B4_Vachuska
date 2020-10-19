polozka = []
cena = []

def printTable(vec,penize):
    max=tag = 0
    polozka.append(vec)
    cena.append(penize)

    for i in range(0,len(polozka)):
        if max < len(polozka[i]):
            max = len(polozka[i]) + 5

        if tag < len(cena[i]):
            tag = len(cena[i])

    hash = "═"*(max+tag)
    print(f"\n╔{hash}╗")

    for q in range(0,len(polozka)):
        delka = max - len(polozka[q])
        text = "║{polozka}{nic:<{max}}{cena:>{tag}}".format(polozka = polozka[q],max=str(delka),cena = cena[q], nic = "", tag = tag)
        print(text+"║")

    print(f"╚{hash}╝\n")

while True:
  a = input("Zadejte položku: ")
  b = input("Zadejte cenu: ")
  printTable(a,b)
