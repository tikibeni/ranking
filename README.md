# windsurf-ranking
Järjestelmä purjelautailun kilpailukausien ranking-pistelaskua varten.

Taustatietona: 
Lajissani, purjelautailussa on joka vuosi useita eri kilpailuja muutamassa eri lautaluokassa. Kaudessa on aina noin 4-5 "ranking"-kilpailua per luokka, joista muodostetaan kauden parhaat kilpailijat muutaman pistelaskusäännön pohjalta. Ongelmana on, että tällä hetkellä lajiliitolla ei ole mitään järjestelmää/ohjelmaa/taulukkoa, mihin he varastoisivat näitä pisteitä, vaan esimerkiksi tällä kaudella meikäläinen kaivoi kaikkien (oman lautaluokan) kilpailijoiden sijoitukset ja laskin pisteet manuaalisesti. Näinpä ideana olisi toteuttaa järjestelmä, jonka avulla voitaisiin laskea useiden kymmenien kilpailijoiden tuloksia läpi kauden syöttämällä kilpailu- ja kilpailijatiedot järjestelmään.

Lisätoiminnallisuuksia / hifistelyä:
	* Mahdollisuus laittaa korjauspyyntö säpöön / admin-tunnukselle
	* Mikäli taidot ja aika riittää, niin käyttäjätunnuksen luontimahdollisuus, jotta järjestelmän 	voisi saada toimimaan siltä pohjalta, että kilpailijat lähettävät itse tuloksia adminille, joka hyväksyy / hylkää ehdotukset.

Huomioita:
- Kilpailija voi olla useammassa kilpailuluokassa
- Eri kilpailuluokkien mukaiset pistelaskusäännöt
	* Discardit.

Tauluja voisivat olla:

- Tulokset
	* Tulokseen liittyvä kilpailu
	* Tulokseen liittyvät kilpailijat
	* Tulos:Double
- Kilpailu
	* Siihen liittyvä luokka
	* Siihen liittyvät kilpailijat
	* Kilpailun nimi
	* Päivämäärä 
- Luokka
	* Liittyvät kilpailijat
	* Luokkaan liittyvät kilpailut
	* Kilpailijoiden lukumäärä luokassa
- Kilpailija
	* Nimi
	* Pursiseura
	* Purjenumero
	* Kilpailijaan liittyvät kilpailuluokat
	* Kilpailijaan liittyvät tulokset
	* Kilpailijaan liittyvät välineet
