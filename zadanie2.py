class Ksiazka:
    def __init__(self, tytul, autor):
        self.tytul=tytul
        self.autor=autor
        self.egzemplarze=[]

class Egzemplarz:
    def __init__(self, rok_wydania, ksiazka):
        self.rok_wydania=rok_wydania
        self.ksiazka=ksiazka
        self.wypozyczony=False

class Czytelnik:
    limit = 3
    def __init__(self, nazwisko):
        self.nazwisko=nazwisko
        self.wypozyczone={}
    def wypozycz(self, egzemplarz):
       
        if Czytelnik.limit > len(self.wypozyczone) and egzemplarz.ksiazka.tytul
not in self.wypozyczone.keys()
            self.wypozyczone[egzemplarz.ksiazka.tytul]=egzemplarz
            egzemplarz.wypozyczony=True
            return True
        else:
            return False
    def oddaj(self, tytul):
        try:
            egzemplarz=self.wypozyczone[tytul]
            egzemplarz.wypozyczony=False
            del self.wypozyczone[tytul]
            return True
        except:
            return False
        
        
class Biblioteka:
    def __init__(self):
        self._ksiazki={}
        self._czytelnicy={}
    def dodaj_egzemplarz_ksiazki(self, tytul, autor, rok_wydania):
        try:
            ksiazka=self._ksiazki[tytul]
        except:
            ksiazka=Ksiazka(tytul, autor)
            self._ksiazki[tytul]=ksiazka
        ksiazka.egzemplarze.append(Egzemplarz(rok_wydania, ksiazka))
        return True
    def dostepne_egz(self, tytul):
        try:
            for egz in self._ksiazki[tytul].egzemplarze:
                if egz.wypozyczony == False:
                   return [egz]
                else
                   return []
        except:
            return 
    def __pobierz_czytelnika(self, nazwisko):
        try:
            czytelnik=self._czytelnicy[nazwisko]
        except:
            czytelnik=Czytelnik(nazwisko)
            self._czytelnicy[nazwisko]=czytelnik
        return czytelnik
    def wypozycz(self, nazwisko, tytul):
        try:
            self.dostepne_egz(tytul)[0]
            czytelnik=self._pobierz_czytelnika(nazwisko)
            return czytelnik.wypozycz(egzemplarz)
        except:
            return False
    def oddaj(self, nazwisko, tytul):
        try:
            Czytelnik=self._pobierz_czytelnika(nazwisko)
            return czytelnik.oddaj(tytul)
        except:
            return False 
    def raport_ksiazek(self):
        lista=[]
        for el in sorted(self._ksiazki.items()):
            lista.append((el[0],el[1].autor,len(el[1].egzemplarze)))
        return lista


biblioteka = Biblioteka()
for i in range(int(input())):
    t = eval(input())
    if t[0] == "dodaj":
        print(biblioteka.dodaj_egzemplarz_ksiazki(t[1], t[2], t[3]))
    elif t[0] == "wypozycz":
        print(biblioteka.wypozycz(t[1], t[2]))
    elif t[0] == "oddaj":
        print(biblioteka.oddaj(t[1], t[2]))
print("Koniec")
