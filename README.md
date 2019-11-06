# windsurf-ranking
Järjestelmä purjelautailun kilpailukausien ranking-pistelaskua varten.

## Taustatietona: 
Lajissani, purjelautailussa on joka vuosi useita eri kilpailuja muutamassa eri lautaluokassa. Kaudessa on aina noin 4-5 "ranking"-kilpailua per luokka, joista muodostetaan kauden parhaat kilpailijat muutaman pistelaskusäännön pohjalta. Ongelmana on, että tällä hetkellä lajiliitolla ei ole mitään järjestelmää/ohjelmaa/taulukkoa, mihin he varastoisivat näitä pisteitä, vaan esimerkiksi tällä kaudella meikäläinen kaivoi kaikkien (oman lautaluokan) kilpailijoiden sijoitukset ja laskin pisteet manuaalisesti. Näinpä ideana olisi toteuttaa järjestelmä, jonka avulla voitaisiin laskea useiden kymmenien kilpailijoiden luokkakohtaisia tuloksia läpi kauden syöttämällä kilpailu- ja kilpailijatiedot järjestelmään.

## Halutut toiminnallisuudet:
- Kausi- ja luokkakohtaiset pistetaulukot kilpailijoista
- Admin pystyy muokkaamaan kaikkien taulujen sisältöä
	* Kilpailujen, tulosten, kilpailijoiden ja luokkien lisääminen, muokkaaminen ja poistaminen
- Pystyy hakea halutun kauden tulokset yhteenvetokyselyiden avulla
- Pystyy hakemaan kaikki kilpailijat luokkaa kohden
	* Kilpailija liittyy luokkaan mikäli tämä on osallistunut kyseisen luokan kilpailuun haetulla kaudella.


## Lisätoiminnallisuuksia, idealista:
- Mahdollisuus laittaa korjauspyyntö säpöön / admin-tunnukselle
- Kilpailijan oma kirjautuminen, jonka myötä näkee omat tulokset
- Kilpailijoiden välineet

## Huomioita:
- Luokkaan liittyy useampi kilpailu
- Kilpailuun liittyy yksi luokka
- Kilpailuun liittyy useampi, kilpailijakohtainen tulos
- Kilpailuun liittyy useampi kilpailija
- Kilpailijaan voi liittyä useampi kilpailu
- Tulokseen liittyy yksi kilpailija
- Kilpailijaan voi liittyä useampi tulos

- Muista eri kilpailuluokkien mukaiset pistelaskusäännöt!


## Tauluja voisivat alustavasti olla:

- Tulos
	* Sijoitus
	* Tulokseen liittyvä kilpailu
	* Tulokseen liittyvä kilpailija
- Kilpailu
	* Nimi
	* Päivämäärä
	* Paikka
	* Kilpailuun liittyvä luokka
	* Kilpailuun liittyvät kilpailijat
	* Kilpailuun liittyvät tulokset
- Kilpailija
	* Nimi
	* Purjenumero
	* Pursiseura
	* Kilpailijaan liittyvät kilpailut
- Luokka
	* Nimi
	* Luokkaan liittyvät kilpailut
- KilpailuKilpailija
	* Liitostaulu, jossa viiteavaimet tauluista Kilpailu ja Kilpailija

## Tietokantakaavio:
![alt text][logo]
[logo]: https://github.com/tikibeni/windsurf-ranking/blob/master/kaavio.PNG "Tietokantakaavio"
