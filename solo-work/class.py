class Mieszkanie:
    def __init__(self, miasto, ulica, numer, kod_pocztowy, pietro, powierzchnia, liczba_pokoi, balkon):
        self.miasto = miasto
        self.ulica = ulica
        self.numer = numer
        self.kod_pocztowy = kod_pocztowy
        self.pietro = pietro
        self.powierzchnia = powierzchnia
        self.liczba_pokoi = liczba_pokoi
        self.balkon = balkon

    def __str__(self):
        return f"Mieszkanie znajduje się w mieście {self.miasto}, na ulicy {self.ulica}, a jego powierzchnia wynosi: {self.powierzchnia} m2"

    def dodaj_pokoj(self):
        self.liczba_pokoi += 1

    def oblicz_sr_powierzchnie_pokoi(self):
        return self.powierzchnia / self.liczba_pokoi

    def dodaj_balkon(self):
        self.balkon = True

mieszkanie_1 = Mieszkanie("Poznań", "Roosevelta", "15", 60-829, 3, 47, 3, False)
print(mieszkanie_1)
mieszkanie_1.dodaj_pokoj()
print(mieszkanie_1.liczba_pokoi)
print(mieszkanie_1.oblicz_sr_powierzchnie_pokoi())
mieszkanie_1.dodaj_balkon()
print(mieszkanie_1.balkon)