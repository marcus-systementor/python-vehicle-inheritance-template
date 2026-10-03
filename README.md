# Fordon – inheritance och polymorphism i praktiken

Du har redan arbetat med bilar och med `Animal`, `Dog`, `Cat` och `Horse`. Efter lärarens genomgång av inheritance, method overriding och polymorphism ska du nu använda samma idéer i ett bekant område: fordon.

Du börjar **utan inheritance**. Tre fordons-classes får medvetet liknande kod. När upprepningen syns bygger du en gemensam `Vehicle`. Målet är att kunna förklara sambandet:

```text
gemensamt state + gemensamt beteende → Vehicle
specialiserat beteende             → child classes
samma method-namn, olika resultat  → overriding
samma anrop på olika objects       → polymorphism
```

Arbeta i ordning och kör efter varje liten ändring. Det här är en övning, inte en examination. Ett fungerande checkpoint är framsteg även om du inte hinner allt. Grundlabben är steg 1–12; bonusen längst ned är frivillig.

## Kom igång

Om läraren delar detta som en publik GitHub-template: välj **Use this template → Create a new repository**, skapa ett eget **Private** repository och klona ditt nya repository. Öppna mappen med `README.md` i VS Code. Du behöver bara vanlig Python.

Redigera [vehicle.py](vehicle.py) för classes och [main.py](main.py) för objects, anrop och utskrifter. Kör från repositoryts rot:

```text
python main.py
```

På Windows kan `py main.py` fungera bättre; på vissa datorer används `python3 main.py`. Startfilen skriver bara `Fordon: börja med Car` och avslutas. Den färdiga lösningen finns inte i studentfilerna. Använd [HJALP.md](HJALP.md) vid fel och skriv egna svar i [REFLECTION.md](REFLECTION.md). Efter ett fungerande steg: spara, kör och gör gärna en `commit` med det engelska förslaget. Om du får en `traceback`, läs sista raden och hitta fil/rad före nästa ändring.

För att jämföra resultaten väljer vi en enkel gemensam regel: `start()` sätter `is_running` till `True`, `stop()` sätter den till `False`, och `show_status()` **returnerar** exempelvis `Volvo V60 is running` eller `Volvo V60 is stopped`. `main.py` skriver ut returvärdet. Alla objects börjar med `is_running = False`.

## Steg 1 – en välbekant Car

**Mål:** En `Car` kan hålla eget state och ändra det.

**Gör:** Skapa `class Car` i `vehicle.py` med `__init__(self, brand, model)` som sparar `self.brand`, `self.model` och `self.is_running = False`. Ge den `start(self)`, `stop(self)` och `show_status(self)` enligt regeln ovan. Använd ett vanligt `if`/`else` i `show_status()` för att välja `running` eller `stopped`, och returnera texten. Lägg också till `move(self)` som returnerar `f"{self.brand} {self.model} is driving on the road"` och `honk(self)` som returnerar `"Beep beep!"`. Importera Car i `main.py`. Skapa `car = Car("Volvo", "V60")` och skriv ut status före start, efter `car.start()` och efter `car.stop()`. Skriv även ut `car.move()` och `car.honk()`.

**Checkpoint:** Kör `python main.py`. Status går `stopped → running → stopped`; `move()` säger att Volvo V60 kör på vägen, och `honk()` ger `Beep beep!`. Prova ett annat model-namn och se att texterna följer det. Vilka tre attributes beskriver objectets state? Vilka methods ändrar state? Vilket object är `self` vid `car.start()`?

**Commit:** `Create Car class`

## Steg 2 – en liknande Motorcycle

**Mål:** Märka upprepningen innan vi försöker ta bort den.

**Gör:** Lägg till `class Motorcycle` **utan inheritance**. Upprepa samma `__init__`, `start()`, `stop()` och `show_status()` som i Car. Skriv en egen `move()` som returnerar `f"{self.brand} {self.model} is riding on the road"` och `rev_engine()` som returnerar `"Vroom!"`. Importera Motorcycle, skapa `motorcycle = Motorcycle("Honda", "CB650R")` och kontrollera alla methods som du kontrollerade för Car.

**Checkpoint:** Kör: Honda CB650R börjar stoppad, kan startas och stoppas, rör sig på vägen och ger `Vroom!`. Prova en annan brand på Motorcycle; Car:s texter ska inte ändras. Jämför de två class-definitionerna: vilka delar är nästan lika?

**Commit:** `Add Motorcycle class`

## Steg 3 – en Boat också

**Mål:** Göra problemet med duplicerad kod tydligt.

**Gör:** Lägg till `class Boat` **utan inheritance**. Upprepa samma tre attributes och samma `start()`, `stop()` och `show_status()`. Dess `move()` returnerar `f"{self.brand} {self.model} is sailing on the water"`; dess `drop_anchor()` returnerar `"Anchor dropped"`. Importera Boat, skapa `boat = Boat("Yamaha", "242X")` och kontrollera status, start, stopp och de två egna method-resultaten.

**Checkpoint:** Kör: båten börjar stoppad, växlar status vid start/stopp, seglar på vattnet och kan ge `Anchor dropped`. Prova en annan model för bara Boat. Alla tre fordons-objects ska fortfarande fungera.

**Commit:** `Add Boat class`

## Steg 4 – vad upprepas?

Pausa kodningen. Jämför de tre classes i [vehicle.py](vehicle.py). Vilka attributes upprepas? Vilka methods upprepas? Vilka methods skiljer sig? Om `show_status()` ska få en ny formulering, hur många ställen måste du ändra nu? Vad riskerar att hända om du glömmer ett av dem? Skriv ett kort svar i [REFLECTION.md](REFLECTION.md).

**Checkpoint:** Kör igen utan kodändring; alla tre ska ge samma resultat som i steg 3. Du ska kunna peka ut de upprepade raderna innan du fortsätter. Ingen `commit` krävs för denna reflektionspaus.

## Steg 5 – skapa en gemensam Vehicle

Nu har du ett konkret skäl att använda inheritance. Den gemensamma delen kan bo i en **base class** (eller **parent class**). `Car`, `Motorcycle` och `Boat` blir senare **subclasses** (eller **child classes**):

```text
Vehicle
├── Car
├── Motorcycle
└── Boat
```

**Mål:** Se att Vehicle fungerar själv innan du ändrar de tre andra classes.

**Gör:** Sätt `class Vehicle` **ovanför** Car, Motorcycle och Boat i `vehicle.py`. Flytta ännu inte bort deras kod. Ge Vehicle `__init__(self, brand, model)`, `start()`, `stop()` och `show_status()` med samma enkla beteende som du redan skrivit. Lägg också till en generell `move()` som returnerar `"The vehicle is moving"`. Importera Vehicle i `main.py`, skapa `base_vehicle = Vehicle("Generic", "Vehicle")` och skriv ut dess status, starta det, skriv status igen och skriv ut dess `move()`.

**Checkpoint:** Kör: Generic Vehicle går från stopped till running, och dess `move()` ger `The vehicle is moving`. Car, Motorcycle och Boat fungerar fortfarande. Prova `base_vehicle.stop()` och kontrollera stopped igen. Koden har tillfälligt **mer** upprepning; nästa steg tar bort den.

**Commit:** `Add Vehicle base class`

## Steg 6 – låt Car ärva från Vehicle

**Mål:** Ta bort upprepning från en class utan att förlora funktionen.

**Gör:** Ändra `class Car:` till `class Car(Vehicle):`. Ta bort Car:s egna `__init__`, `start()`, `stop()` och `show_status()`. Lämna kvar bara `move()` och `honk()` i Car. Ändra inte sättet att skapa `car = Car("Volvo", "V60")` i `main.py`.

**Checkpoint:** Kör samma kontroll som i steg 1: Car börjar stoppad, `car.start()` ger running, `car.stop()` ger stopped, `car.move()` ger körtexten och `car.honk()` ger signalen. Prova en ny Car med annan brand och model. Varifrån kommer nu `brand`, `start()` och `show_status()`? Vilka methods är definierade direkt i Car?

**Commit:** `Make Car inherit from Vehicle`

## Steg 7 – refaktorera Motorcycle och Boat

**Mål:** Låta alla tre dela samma kod för state och status.

**Gör:** Ändra deras class-rubriker till `class Motorcycle(Vehicle):` och `class Boat(Vehicle):`. Ta bort de egna kopiorna av `__init__`, `start()`, `stop()` och `show_status()` i båda. Behåll Motorcycle:s `move()` och `rev_engine()` samt Boat:s `move()` och `drop_anchor()`. Ändra inte object-anropen i `main.py`.

**Checkpoint:** Kör: alla tre börjar stoppade, kan starta och stoppa oberoende av varandra, och deras egna `move()` och särskilda methods fungerar. Starta bara Boat: dess status blir running medan Car och Motorcycle fortfarande är stopped. Jämför antalet kopior av `show_status()` före och efter refaktoreringen.

**Commit:** `Refactor vehicle subclasses`

## Steg 8 – förstå method overriding

En subclass kan definiera en method med **samma namn** som i base class. Det kallas **method overriding**. Vehicle har en generell `move()`, men varje child class har sin egen version. Python utgår från objectets class: finns `move()` där används den; annars används den ärvda versionen från Vehicle. För ett Car-object används alltså Car:s `move()`; för ett Vehicle-object används Vehicle:s.

**Förutsäg före körning:** Vad ger `base_vehicle.move()`, `car.move()`, `motorcycle.move()` och `boat.move()`? Skriv gärna din gissning i [REFLECTION.md](REFLECTION.md). Skriv sedan ut de fyra return-värdena i `main.py` om de inte redan syns.

**Checkpoint:** Kör och jämför: `The vehicle is moving`, Volvo V60 kör på vägen, Honda CB650R rör sig på vägen och Yamaha 242X seglar på vattnet. Prova en annan model för båten; bara båtens specialiserade text ska följa ändringen. Var hittar Python rätt `move()` för varje object? Detta steg behöver ingen ny `commit` om du bara återanvänder befintliga utskrifter; gör en liten `commit` om du lade till kontrollutskrifter du vill behålla.

## Steg 9 – samma loop, olika rörelser

**Mål:** Se polymorphism i en loop utan specialregler för olika fordon.

**Gör:** I `main.py`, skapa `vehicles = [car, motorcycle, boat]` med de objects du redan har. Lägg till en `for`-loop som skriver ut varje objects `move()`-resultat:

```python
for vehicle in vehicles:
    print(vehicle.move())
```

**Förutsäg före körning:** Skriv ner de tre raderna i rätt ordning och kör först därefter. Samma kodrad, `vehicle.move()`, fungerar för flera object-typer, men resultatet blir olika. Det är kärnan i **polymorphism** här. Loopen behöver inte veta om objectet är Car, Motorcycle eller Boat, och den behöver inga `if`/`elif`-grenar för typerna.

**Checkpoint:** Kör: utskrifterna gäller väg, väg och vatten i listans ordning. Byt tillfälligt plats på Car och Boat i listan: loopen ändras inte, men utskriftsordningen gör det. Återställ ordningen. Varför kan samma anrop ge olika resultat, och hur bestäms vilken `move()` som används?

**Commit:** `Use polymorphism with vehicles`

## Steg 10 – ärvt och override i samma loop

**Mål:** Koppla ihop delat state, ärvda methods och specialiserad rörelse.

**Gör:** Utöka loopen: anropa `vehicle.start()` före utskrifterna, skriv sedan `vehicle.show_status()` och `vehicle.move()`. Om du har gamla tillfälliga `start()`-anrop före loopen, ta bort dem eller se till att du vet vilken status varje object har när loopen börjar. Efter loopen, stoppa bara Car och skriv status för Car, Motorcycle och Boat igen.

**Checkpoint:** Kör: under loopen blir alla tre running och ger varsin rörelsetext. Efter att bara Car stoppats är Car stopped medan Motorcycle och Boat fortfarande är running. Prova att stoppa Boat i stället i en tillfällig körning; bara Boat ska ändra state. Vilken method är ärvd, vilken är override, och vilket state ändras?

**Commit:** `Combine inherited and overridden methods`

## Steg 11 – skapa en egen subclass

**Mål:** Pröva själv att utöka programmet utan nya specialfall i loopen.

**Gör:** Välj `Train`, `Scooter`, `Airplane` eller `Bus`. Skapa en ny class som ärver från Vehicle. Den ska använda ärvda `brand`, `model`, `is_running`, `start()`, `stop()` och `show_status()`. Skriv en egen `move()` med en kort text som passar fordonet och en enkel method som bara detta fordon behöver. Importera den, skapa ett object och lägg det sist i `vehicles`-listan. Behåll loopens body från steg 10 oförändrad. Använd inga typkontroller i loopen.

**Checkpoint:** Kör: det nya objectet får status running och sin egen rörelsetext i samma loop. Anropa också dess särskilda method separat så du ser att den fungerar. Prova ett annat brand-värde: både status och rörelsetext ska följa objectet. De gamla tre fordonen ska fortsätta fungera.

**Commit:** `Add custom vehicle subclass`

## Steg 12 – ändra gemensam kod på ett ställe

**Mål:** Känna den praktiska nyttan av inheritance.

**Gör:** Ändra bara texten som `Vehicle.show_status()` returnerar, till exempel från `Volvo V60 is running` till `Volvo V60 is currently running`. Behåll samma beslut mellan running och stopped. Ändra inte subclass-definitionerna eller loopen.

**Checkpoint:** Kör: Car, Motorcycle, Boat och ditt nya fordon om du gjorde steg 11 får den nya statusformuleringen. Kontrollera både ett running och ett stopped object. Hur många classes behövde du redigera? Hur många hade du behövt ändra i versionen från steg 3?

**Commit:** `Update shared vehicle status`

## Frivillig bonus – ett eget attribute i Car

**Bara efter grundlabben.** Vill du ge Car ett extra `number_of_doors` kan dess constructor använda `super()` för att låta Vehicle sköta den gemensamma initieringen:

```python
class Car(Vehicle):
    def __init__(self, brand, model, number_of_doors):
        super().__init__(brand, model)
        self.number_of_doors = number_of_doors
```

`super().__init__()` anropar Vehicle:s initializer, så du slipper skriva om `brand`, `model` och `is_running`. Om du provar detta måste du uppdatera dina Car-anrop med antalet dörrar. Bonusen krävs inte för att labben ska vara klar, och du behöver inte använda den i andra subclasses.

## Avsluta

Svara på [REFLECTION.md](REFLECTION.md) med egna ord. Du kan jämföra med [ett möjligt facit](facit/README.md) **efter** att du försökt själv; förklara hellre varför raderna fungerar än att kopiera dem. Om du fastnat, skriv vilket steg som fungerar, vad du förväntade dig och vad du faktiskt såg. Det är bra underlag för samtal med läraren.
