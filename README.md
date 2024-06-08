# NUKS_2024

Izdelava projekta v sklopu predmeta NUKS (Načrtovanje in upravljanje komunikacijskih sistemov). Izdelali smo aplikacijo, ki uporabnikom omogoča pošiljanje različnih datotek (png, mp3, pdf, webms itd), podobno kot aplikacija WeTransfer.

Aplikacija komunicira z spletnim vmesnikom (Ang. SPA - single page application), ki je sestavljena iz HTML datotek (front end) in komunicira s Uvicorn strežnikom preko fastAPI (Ang. fast Application Programming Interface) vmesnika. API vmesnik oziroma "back-end" sprejema zahteve od HTML datotek (preko URL-ja) in je napisan v programskem jeziku Python. Za podatkovno bazo je uporabljena SQLite3, ki vsebuje 6 elementov.

Opis in delovanje:
Aplikacija potrebuje nekaj vhdonih parametrov,da lahko posreduje datoteko. Na prvi strani (index.html) imamo 3 vhodna polja, kamor vnesemo svoj gmail, gmail prejemnika in sporočilo k datoteki. Te podatke in generirano verifikacijsko kodo (server.py -> "random_number") python shrani v podatkovno bazo za kasnejšo obdelavo. Na drugi strani (authentication.html) potrdimo naš vnesen gmail (podobno kot varnsotni sistem captcha). Če je vnesena koda pravilna, nas spusti na tretjo stran ("upload_file.html"), kjer naložimo datoteko na strežnik (pod mapo "uploads"). Če je datoteka bila uspešno naložena, bo "back-end" psoredoval URL za prenos te datoteke na prejemnikov GMAIL skupaj z vsebino sporočila (Ang. message).



