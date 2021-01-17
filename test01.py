class __Lod:
    def __init__(self, barva, hmotnost, pohon):
        self.barva = barva
        self.hmotnost = hmotnost
        self.pohon = pohon

    def vypisvlastnosti(self):
        print("Barva plavidla je: " + self.barva)
        print("Hmotnost plavidla je: " + self.hmotnost)
        print("Pohon plavidla je: " + self.pohon + "\n")

class Ledoborec(__Lod):
    def koliklidi(self):
        print("Ledoborec má posádku 100 lidí.")

class Kanoe(__Lod):
    def koliklidi(self):
        print("Kanoe má posádku 2 lidí.")

class Katamaran(__Lod):
    def koliklidi(self):
        print("Katamarán má posádku 4 lidí.")

ledoborec = Ledoborec("červená", "30000 kg", "motor")
kanoe = Kanoe("žlutá", "35 kg", "člověk")
katamaran = Katamaran("bílá", "65 kg", "plachta")

ledoborec.koliklidi()
ledoborec.vypisvlastnosti()

kanoe.koliklidi()
kanoe.vypisvlastnosti()

katamaran.koliklidi()
katamaran.vypisvlastnosti()
