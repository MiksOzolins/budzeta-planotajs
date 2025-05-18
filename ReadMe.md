# Virtuālais ikdienas budžeta plānotājs

## Projekta apraksts

Šis projekts ir izstrādāts kā gala darbs datu struktūru kursam. Tā mērķis ir automatizēt personīgo budžeta pārvaldību, ļaujot lietotājam:

- Pievienot savus ikdienas izdevumus,
- Skatīt tēriņu kopsavilkumu pēc kategorijām,
- Aprēķināt kopējo izdevumu summu,
- Rādīt visus reģistrētos tēriņus,
- Dzēst konkrētus ierakstus no saraksta.

Programma darbojas komandrindas režīmā, izmantojot vienkāršu izvēlni un saglabā visus datus failā `budzets.csv`, kas padara izdevumus noturīgus starp palaišanām.

## Izmantotās Python bibliotēkas

Projektā izmantotas tikai **standarta Python bibliotēkas** (nav nepieciešama ārēja instalācija):

- `csv` – izdevumu saglabāšanai un nolasīšanai no CSV faila;
- `datetime` – lai automātiski reģistrētu precīzu izdevuma pievienošanas laiku;
- `collections.defaultdict` – ērtai tēriņu grupēšanai pēc kategorijām;
- `os` – lai pārbaudītu, vai fails eksistē (CSV galvenes pievienošanai).

Šo izvēli nosaka vienkāršība, savietojamība un mērķis strādāt ar strukturētiem datiem efektīvā veidā.

## Paša definēta datu struktūra

Galveno datu vienību apraksta klase `Izdevums`, kurā tiek glabāta:

- **summa** (float),
- **kategorija** (str),
- **papildu apraksts** (str),
- **izveides datums** (automātisks ar `datetime.now()`).

```python
class Izdevums:
    def __init__(self, summa, kategorija, apraksts=""):
        self.summa = float(summa)
        self.kategorija = kategorija
        self.apraksts = apraksts
        self.datums = datetime.now().strftime("%Y-%m-%d %H:%M")
```

Šī struktūra tiek izmantota gan datu ievadē, gan eksportā uz CSV.

## Programmas izmantošana

Lietotājs, palaižot programmu (`python main.py`), redz izvēlni ar sekojošām iespējām:

```
=== Virtuālais budžeta plānotājs ===
1. Pievienot izdevumu
2. Rādīt tēriņu kopsavilkumu un kopējās izmaksas
3. Dzēst izdevumu
4. Rādīt visus izdevumus
5. Iziet
```

### 1. Pievienot izdevumu
- Lietotājs ievada summu, kategoriju un (neobligāti) aprakstu.
- Izdevums tiek ierakstīts `budzets.csv`.

### 2. Kopsavilkums un kopējās izmaksas
- Rāda tēriņu sadalījumu pa kategorijām.
- Aprēķina un izvada kopējo tēriņu summu.

### 3. Dzēst izdevumu
- Lietotājam tiek parādīts saraksts ar visiem ierakstiem un kārtas numuriem.
- Pēc numura ievades konkrētais izdevums tiek izņemts no faila.

### 4. Rādīt visus izdevumus
- Tiek izdrukāti visi esošie ieraksti hronoloģiskā secībā.

## Papildu informācija

- Programma automātiski izveido CSV failu, ja tas neeksistē, un pievieno galveni.
- Katra darbība ir interaktīva, ar kļūdu apstrādi un lietotājam draudzīgu ziņojumu sistēmu.
- Visi dati tiek glabāti UTF-8 kodējumā.

## Autors

**Miks Kristaps Ozoliņš**  

