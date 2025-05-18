import csv
import os
from datetime import datetime
from collections import defaultdict

class Izdevums:
    def __init__(self, summa, kategorija, apraksts=""):
        self.summa = float(summa)
        self.kategorija = kategorija
        self.apraksts = apraksts
        self.datums = datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_list(self):
        return [self.datums, self.summa, self.kategorija, self.apraksts]

def pievienot_izdevumu(izdevums, fails="budzets.csv"):
    fails_neeksiste = not os.path.exists(fails)
    with open(fails, mode="a", newline="", encoding="utf-8") as f:
        rakstitajs = csv.writer(f)
        if fails_neeksiste:
            rakstitajs.writerow(["Datums", "Summa", "Kategorija", "Apraksts"])
        rakstitajs.writerow(izdevums.to_list())

def radit_kopsavilkumu(fails="budzets.csv"):
    kategorijas_summa = defaultdict(float)
    total = 0.0

    try:
        with open(fails, mode="r", encoding="utf-8") as f:
            lasitajs = csv.reader(f)
            next(lasitajs, None)
            for rinda in lasitajs:
                if len(rinda) >= 3:
                    try:
                        summa = float(rinda[1])
                        kategorija = rinda[2]
                        kategorijas_summa[kategorija] += summa
                        total += summa
                    except ValueError:
                        continue
    except FileNotFoundError:
        print("Kļūda: fails nav atrasts.")
        return

    print("\nTēriņu kopsavilkums pēc kategorijām:")
    for kat, summa in kategorijas_summa.items():
        print(f"  - {kat}: {summa:.2f} €")

    print(f"\nKopējās izmaksas: {total:.2f} €")

def dzest_izdevumu(fails="budzets.csv"):
    try:
        with open(fails, mode="r", encoding="utf-8") as f:
            rindas = list(csv.reader(f))

        if len(rindas) <= 1:
            print("Failā nav neviena izdevuma.")
            return

        print("\nEsošie izdevumi:")
        for i, rinda in enumerate(rindas[1:]):
            datums, summa, kategorija, apraksts = rinda
            print(f"{i + 1}. [{datums}] {summa}€ – {kategorija} – {apraksts}")

        izvele = input("\nIevadi izdevuma kārtas numuru, kuru vēlies dzēst (vai '0', lai atceltu): ")
        if not izvele.isdigit():
            print("Kļūda: jāievada cipars.")
            return

        izvele = int(izvele)
        if izvele == 0:
            print("Dzēšana atcelta.")
            return
        elif 1 <= izvele <= len(rindas) - 1:
            dzestais = rindas.pop(izvele)
            with open(fails, mode="w", newline="", encoding="utf-8") as f:
                rakstitajs = csv.writer(f)
                rakstitajs.writerows(rindas)
            print(f"Izdevums \"{dzestais[1]}€ – {dzestais[2]}\" ir izdzēsts.")
        else:
            print("Kļūda: šāds kārtas numurs neeksistē.")

    except FileNotFoundError:
        print("Kļūda: fails nav atrasts.")

def radit_visus_izdevumus(fails="budzets.csv"):
    try:
        with open(fails, mode="r", encoding="utf-8") as f:
            rindas = list(csv.reader(f))
            if len(rindas) <= 1:
                print("Nav neviena izdevuma.")
                return
            print("\nVisi izdevumi:")
            for r in rindas[1:]:
                print(f"[{r[0]}] {r[1]}€ – {r[2]} – {r[3]}")
    except FileNotFoundError:
        print("Kļūda: fails nav atrasts.")

def izvelne():
    while True:
        print("\n=== Virtuālais budžeta plānotājs ===")
        print("1. Pievienot izdevumu")
        print("2. Rādīt tēriņu kopsavilkumu un kopējās izmaksas")
        print("3. Dzēst izdevumu")
        print("4. Rādīt visus izdevumus")
        print("5. Iziet")
        izvele = input("Izvēlies darbību: ")

        if izvele == "1":
            summa = input("Ievadi summu (€): ")
            try:
                summa = float(summa)
            except ValueError:
                print("Kļūda: lūdzu, ievadi derīgu skaitli!")
                continue
            kategorija = input("Ievadi kategoriju (ēdiens, transports, izklaide utt.): ")
            apraksts = input("Papildu apraksts (nav obligāts): ")
            izd = Izdevums(summa, kategorija, apraksts)
            pievienot_izdevumu(izd)
            print("Izdevums pievienots.")
        elif izvele == "2":
            radit_kopsavilkumu()
        elif izvele == "3":
            dzest_izdevumu()
        elif izvele == "4":
            radit_visus_izdevumus()
        elif izvele == "5":
            print("Programma tiek pārtraukta.")
            break
        else:
            print("Kļūda: nepareiza izvēle. Mēģini vēlreiz.")

if __name__ == "__main__":
    izvelne()
