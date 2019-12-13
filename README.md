# windsurf-ranking
Järjestelmä purjelautailun kilpailukausien ranking-pistelaskua varten.

# Herokuun:
- [Tästä](https://windsurf-ranking.herokuapp.com)
- Testitunnukset:
	* Admin-oikeuksilla: 
		- Tunnus: admin
	    - Salasana: admin
	* Kilpailija-oikeuksilla: 
		- Tunnus: testi
	    - Salasana: testi
- Mahdollisuutena myös rekisteröityä spectator-oikeus-käyttäjäksi.

## Taustatietona: 
Lajissani, purjelautailussa on joka vuosi useita eri kilpailuja muutamassa eri lautaluokassa. Kaudessa on aina noin 4-5 "ranking"-kilpailua per luokka, joista muodostetaan kauden parhaat kilpailijat muutaman pistelaskusäännön pohjalta. Ongelmana on, että tällä hetkellä lajiliitolla ei ole mitään järjestelmää/ohjelmaa/taulukkoa, mihin he varastoisivat näitä pisteitä, vaan esimerkiksi tällä kaudella meikäläinen kaivoi kaikkien (oman lautaluokan) kilpailijoiden sijoitukset ja laskin pisteet manuaalisesti. Näinpä ideana olisi toteuttaa järjestelmä, jonka avulla voitaisiin laskea useiden kymmenien kilpailijoiden luokkakohtaisia tuloksia läpi kauden syöttämällä kilpailu- ja kilpailijatiedot järjestelmään.

## Päivityksistä, pohtimisia, ideoita, tehtävää:
https://github.com/tikibeni/windsurf-ranking/blob/master/documentation/LITodo

## Käyttäjätarinat:
https://github.com/tikibeni/windsurf-ranking/blob/master/documentation/K%C3%A4ytt%C3%A4j%C3%A4tarinat

## Tietokantakaavio:
![alt text](https://github.com/tikibeni/windsurf-ranking/blob/master/documentation/tsohakaavio.png "Tietokantakaavio")

# Ohjelman lataaminen?

## Asennus ja työkalut
- Voit ladata ohjelman omalle koneellesi GitHubin "Clone or download"-painikkeesta, josta saat ladattua .zip-tiedoston "Download ZIP"-painikkeesta.
- Pura zip-tiedosto haluamaasi kansioon
- Pääset siihen käsiksi konsolilla, johon tarvitset muutaman työkalun
- Ohjelman suorittamiseen tarvitset tuen Python-kielisten ohjelmien suorittamiseen. Pythonin asentamiseen tarvittavat tiedostot löydät osoitteesta: (https://www.python.org/downloads/). 
- Lisäksi tarvitset tuen Python-kirjastojen lataamiseen, eli Pythonin pipin. Pip asentuu edellä mainitun linkin mukana.
- Tarvitset myös tuen Python-virtuaaliympäristön luomiseen, Pythonin venv-kirjaston. Tulee mahdollisesti em. linkin mukana, mutta täältä voi lukea lisää: (https://docs.python.org/3/tutorial/venv.html)
- Myös PostgreSQL:n. (https://www.postgresql.org/)
- Suositeltavaa on myös Visual Studio Code, jossa lähdekoodia voi tarkastella ja muokata helposti: (https://code.visualstudio.com/)
- Mikäli sovelluksen haluaa Herokuun, tarvitset työvälineet Herokun käyttöön: (https://devcenter.heroku.com/articles/heroku-cli)
- Kattavat ohjeet toimintoihin löydät täältä: (https://materiaalit.github.io/tsoha-19/tyovalineet/)

## Käytön aloittaminen
- Jotta ohjelma toimii, joudut syöttämään tietokannanhallintaohjelmalla muutaman arvon kantaan tässä järjestyksessä:
	* INSERT INTO Rooli (name) VALUES ('admin');
	* INSERT INTO Rooli (name) VALUES ('kilpailija');
	* INSERT INTO Rooli (name) VALUES ('spectator');
	* INSERT INTO account (name, username, password, rooli_id) VALUES ('Valvoja', 'admin', 'admin', 1);
	* INSERT INTO account (name, username, password, rooli_id) VALUES ('Kilpailija', 'testi', 'testi', 2);
