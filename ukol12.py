slova = input("zadejte 3 slova: ")
pole = slova.split()
pole2 = pole
if len(pole) == 3:
    for prvky1 in pole:
        print(pole)
        pole.insert(0, pole[-1])
        pole.pop(-1)
    if len(pole2) == 3:
        pole2.insert(2, pole2[0])
        pole2.pop(0)
        print(pole2)
        pole2.insert(0, pole2[-1])
        pole2.pop(-1)
        print(pole2)
        pole2.insert(0, pole2[-1])
        pole2.pop(-1)
        print(pole2)
else:
    print("zadejte prosím 3 slova")

# Omlouvám se za toto řešení ale nic jiného jsem nevymyslel.
