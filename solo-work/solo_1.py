# zadanie 1.1

hello = "Hello"
student = "Ola"

print("{} {}".format(hello, student))

# zadanie 1.2

student = input("Wpisz swoje imie: ")

print("Hello " + student)

# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Jan"]

liczba_studentow = str(len(studenci))
print("Liczba studentow wynosi: " + liczba_studentow)

# zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]
for student in studenci:
    print("Hello " + student)

# zadanie 1.5

liczba = 3
potega = 4

wynik = str(liczba**potega)

print("Wynik wynosi: " + wynik)

# zadanie 1.6

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count("(")

print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

# zadanie 1.7

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

sorted_list = sorted(studenci)
print("Alfabetyczna lista studentow wynosi: ")
for student in sorted_list:
    print(student)

# zadanie 1.8

# posortuj alfabetycznie (od nazwiska) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

def get_last_name(student):
    return student.split()[-1]

sorted= sorted(studenci, key=get_last_name)

print("Alfabetyczna lista studentow wynosi: ")
for student in sorted:
    print(student)

