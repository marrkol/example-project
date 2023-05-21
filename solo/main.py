class Student:
    def __init__(self, imie, nazwisko, numer_indeksu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.oceny = []

    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.numer_indeksu}"

    def __int__(self):
        return 5

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def zwroc_srednia(self):
        return sum(self.oceny)/len(self.oceny)

student_ola = Student("Aleksandra", "Wojewoda", 123123)
print(int(student_ola))
print(student_ola.zwroc_srednia)
student_ola.dodaj_ocene(5)
print(student_ola.oceny)