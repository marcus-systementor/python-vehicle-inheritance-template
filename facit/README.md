# Facit – en möjlig lösning

Det här är **en möjlig lösning** till grundlabben. Försök själv först. Jämför sedan både din struktur och programmets beteende med lösningen; kopiera inte bara koden. Försök förklara varför varje class och method fungerar.

`Vehicle` äger gemensamma attributes och methods. `Car`, `Motorcycle` och `Boat` har varsin egen `move()` och en egen särskild method. [main.py](main.py) visar både att `start()`/`stop()` påverkar rätt object och att samma anrop till `move()` ger olika resultat i en loop. Statusformuleringen är ändrad som i steg 12. Den egna subclassen i steg 11 och bonusdelen med extra subclass-state får du utforma själv; de ingår inte i detta kärnfacit.

Kör från repositoryts rot med `python facit/main.py` (eller `py`/`python3` på din dator). Filerna i `facit/` ska följa med i Git när templaten publiceras; välj själv när du vill jämföra med dem.
