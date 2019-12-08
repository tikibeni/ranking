# windsurf-ranking
Järjestelmä purjelautailun kilpailukausien ranking-pistelaskua varten.

# Herokuun:
- [Tästä](https://windsurf-ranking.herokuapp.com)
- Testitunnukset:
	* Käyttäjätunnus (admin-oikeuksilla): admin
	    - Salasana: admin
	* Käyttäjätunnus (spectator-oikeuksilla): testi
	    - Salasana: testi
- Mahdollisuutena myös rekisteröityä spectator-oikeus-käyttäjäksi.

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
- account
	* Käyttäjätunnukset
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
![alt text](https://github.com/tikibeni/windsurf-ranking/blob/master/documentation/tsohakaavio.png "Tietokantakaavio")

# Ohjelman lataaminen?
- Voit ladata ohjelman omalle koneellesi GitHubin "Clone or download"-painikkeesta, josta saat ladattua .zip-tiedoston "Download ZIP"-painikkeesta.
- Ohjelman suorittamiseen tarvitset tuen Python-kielisten ohjelmien suorittamiseen. Pythonin asentamiseen tarvittavat tiedostot löydät osoitteesta: (https://www.python.org/downloads/). 
- Lisäksi tarvitset tuen Python-kirjastojen lataamiseen, eli Pythonin pipin. Pip asentuu edellä mainitun linkin mukana.
- Tarvitset myös tuen Python-virtuaaliympäristön luomiseen, Pythonin venv-kirjaston. Tulee mahdollisesti em. linkin mukana, mutta täältä voi lukea lisää: (https://docs.python.org/3/tutorial/venv.html)
- Myös PostgreSQL:n. (https://www.postgresql.org/)
- Suositeltavaa on myös Visual Studio Code, jossa lähdekoodia voi tarkastella ja muokata helposti: (https://code.visualstudio.com/)
- Mikäli sovelluksen haluaa Herokuun, tarvitset työvälineet Herokun käyttöön: (https://devcenter.heroku.com/articles/heroku-cli)
- Kattavat ohjeet toimintoihin löydät täältä: (https://materiaalit.github.io/tsoha-19/tyovalineet/)