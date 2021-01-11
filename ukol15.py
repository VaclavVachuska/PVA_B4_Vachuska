from turtle import *
class Zelva:
    def __init__(self, col, posx, posy):
        self.zelva=Turtle()
        self.color=col

        self.zelva.color(self.color)
        self.zelva.hideturtle()
        self.zelva.penup()
        self.zelva.speed(0)
        self.zelva.setposition(posx, posy)
        self.platno=Screen()
        self.platno.setup(width=700, height=700)

    def posun(self,x,y):
        self.zelva.penup()
        self.zelva.setposition(self.zelva.position()[0]+x,self.zelva.position()[1]+y)
        self.zelva.pendown()
    def pozice(self):
        a={self.zelva.position()[0],self.zelva.position()[1]}
        return a
    def pozicex(self):
        return self.zelva.position()[0]
    def pozicey(self):
        return self.zelva.position()[1]

cervena = Zelva("red", 0, 0)
cervena.zelva.shape("turtle")
cervena.zelva.showturtle()
cervena.zelva.pendown()

while True:
    try:
        print("Program ukončtíte stiskem CTRL+Z, nebo CTRL+C.")
        x, y = input("Zadej x,y: ").split(",")
        print(x)
        print(y)
        x = int(x)
        y = int(y)
        if x <= 340 and x >= -340 and y <= 340 and y >= -340:
            cervena.posun(x,y)
        else:
            print("Zadejte souřadnice od -340 do 340!")
    except ValueError as err:
        print("Prosím zadej dvě čísla oddělená čárkou.")
        continue
    except EOFError:
        print("Ukončení pomocí CTRL + Z.")
        break
    except KeyboardInterrupt:
        print("Ukončení pomocí CTRL + C.")
        break
