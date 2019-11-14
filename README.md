# windsurf-ranking
Järjestelmä purjelautailun kilpailukausien ranking-pistelaskua varten.

# Herokuun:
-[Tästä](https://windsurf-ranking.herokuapp.com)
-Testitunnukset:
	* Käyttäjätunnus: admin
	* Salasana: admin

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


## Tauluja voisivat olla:

- Kilpailu
	* ID
	* Nimi
	* Päivämäärä
	* Paikka
	* Kilpailuun liittyvä luokka
	* Kilpailuun liittyvät tulokset
- Kilpailija
	* ID
	* Nimi
	* Purjenumero
	* Pursiseura
	* Kilpailijaan liittyvät tulokset
- Luokka
	* ID
	* Nimi
	* Luokkaan liittyvät kilpailut
- Tulos
	* Taulu, joka toimii samalla sekä liitostauluna taulujen Kilpailu ja Kilpailija välillä, että tulostauluna
	* ID
	* Tulokseen liittyvä kilpailu 
	* Tulokseen liittyvä kilpailija
	* Sijoitus

## Tietokantakaavio:
![alt text](https://github.com/tikibeni/windsurf-ranking/blob/master/kaavio.PNG?raw=true1 "Tietokantakaavio")
