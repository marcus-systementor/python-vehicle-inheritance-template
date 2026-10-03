# Hjälp – när fordonen inte gör som du väntat dig

Arbeta från aktuellt steg i [README.md](README.md), inte från en senare bild av den färdiga koden. Kör `python main.py` efter små ändringar. Om Python visar en `traceback`:

1. Läs sista raden: vilket fel nämns?
2. Leta upp filen och radnumret i raderna ovanför.
3. Läs just den raden och några rader före den. Vilket object och vilket värde borde finnas där?
4. Ändra en sak som prövar din gissning.
5. Spara och kör igen. Använd en tillfällig `print()` för att inspektera ett värde om det hjälper.

Vanliga saker att kontrollera:

- **`NameError: Vehicle is not defined`:** finns `Vehicle` i `vehicle.py` **ovanför** de subclasses som använder den? Stavades class-namnet likadant i rubriken?
- **En child class verkar inte ärva:** jämför rubriken med `class Car(Vehicle):`. Har du glömt parenteserna med Vehicle? Kontrollera samma sak för Motorcycle och Boat när du når dem.
- **`IndentationError`:** methods ska ligga indragna inne i sin class; methodens rader ska ha ett indrag till. Ett nytt `class`-block börjar utan föregående class-indrag.
- **Saknat `self` eller fel antal argument:** varje instance-method har `self` först i definitionen. När du anropar `car.start()` skriver du inte `self` i parentesen. Ett object måste också ha skapats med brand och model innan du anropar dess methods.
- **Class eller object?** `Car` är en class; `car = Car("Volvo", "V60")` skapar ett object. En lista med `Car` i stället för `car` innehåller inte det object du nyss skapade.
- **Felstavat attribute:** jämför `self.brand`, `self.model` och `self.is_running` i definitionen med namnen där de används. `brand` utan `self.` inne i en annan method är inte automatiskt samma sparade värde.
- **Ärvd ändring syns inte:** kontrollera att du verkligen tog bort de gamla kopiorna av `start()`, `stop()` och `show_status()` från varje subclass. En egen method med samma namn används där i stället för Vehicle:s version. Kontrollera också att du sparat filen du kör.
- **`vehicle.move` visar inte rörelsetexten:** parenteserna behövs. `vehicle.move()` anropar methoden; `print(vehicle.move())` visar dess return-värde.
- **Car:s rörelse ändrar inte Boat:** det är väntat. Varje subclass har sin egen `move()`. Jämför vilket object du anropar och var dess method är definierad.
- **Ett nytt fordon saknas i loopen:** du behöver skapa ett object, importera classen i `main.py` och lägga objectet i `vehicles`-listan. Class-definitionen ensam lägger inte till ett element.
- **Programmet ser oförändrat ut:** kör du `main.py` i samma mapp som din ändrade `vehicle.py`? Kontrollera att importen pekar på rätt fil och att ändringen är sparad. Prova en liten tillfällig utskrift och ta bort den när du hittat felet.

Om du fortfarande fastnar: dela stegnummer, ditt körkommando, vad du förutsåg, vad som faktiskt skrevs ut och den sista relevanta raden i `traceback`. Det räcker ofta för att komma vidare tillsammans.
