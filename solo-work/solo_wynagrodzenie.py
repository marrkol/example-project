import csv

class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = wynagrodzenie_brutto

    def oblicz_wynagrodzenie_netto(self):
        # Tu możesz umieścić swoje obliczenia dla wynagrodzenia netto
        # Przykładowo:
        wynagrodzenie_netto = self.wynagrodzenie_brutto * 0.7  # Zakładamy stawkę podatku 30%
        return wynagrodzenie_netto

    def oblicz_calkowity_koszt(self):
        wynagrodzenie_netto = self.oblicz_wynagrodzenie_netto()
        koszt_pracodawcy = wynagrodzenie_netto + (0.2 * wynagrodzenie_netto)  # Dodajemy 20% na ZUS i inne składki
        return koszt_pracodawcy

# Odczyt danych z pliku CSV
pracownicy = []
with open('pracownicy.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Pomijamy nagłówek
    for row in reader:
        imie = row[0]
        nazwisko = row[1]
        wynagrodzenie_brutto = float(row[2])
        pracownik = Pracownik(imie, nazwisko, wynagrodzenie_brutto)
        pracownicy.append(pracownik)

# Obliczanie całkowitego kosztu pracodawcy
calkowity_koszt = 0
for pracownik in pracownicy:
    calkowity_koszt += pracownik.oblicz_calkowity_koszt()

print("Całkowity koszt pracodawcy:", calkowity_koszt)

