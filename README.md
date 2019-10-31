# windsurf-ranking
Järjestelmä purjelautailun kilpailukausien ranking-pistelaskua varten.

- Pointtina, että admin syöttää kilpailujen tuloksia järjestelmään, jonka myötä ohjelma automaattisesti laskee tuloksia ‘taulukkoon’
- Lisätoiminnallisuuksia / hifistelyä:
	* Mahdollisuus laittaa korjauspyyntö säpöön / admin-tunnukselle
	* Mikäli taidot ja aika riittää, niin käyttäjätunnuksen luontimahdollisuus, jotta järjestelmän 	voisi saada toimimaan siltä pohjalta, että kilpailijat lähettävät itse tuloksia adminille, joka 	hyväksyy / hylkää ehdotukset.

Huomioita:
- Kilpailija voi olla useammassa kilpailuluokassa
- Eri kilpailuluokkien mukaiset pistelaskusäännöt
	* Discardit.

Tauluja voisivat olla:

- Tulokset
	* Tulokseen liittyvä kilpailu
	* Tulokseen liittyvät kilpailijat
	* Tulos:Integer TAI HUOM! Double: Slalom- ja formula-luokat!!
- Kilpailu
	* Siihen liittyvä luokka
	* Siihen liittyvät kilpailijat
	* Kilpailun nimi
	* Päivämäärä 
- Luokka
	* Liittyvät kilpailijat
	* Luokkaan liittyvät kilpailut
	* Denormalisointihuomio: Kilpailijoiden lukumäärä attribuuttina, sillä lukumäärä vaihtelee 	harvoin
- Kilpailija
	* Nimi
	* Kilpailijaan liittyvät kilpailuluokat
	* Kilpailijaan liittyvät tulokset
	* Kilpailijaan liittyvät välineet
	* Purjenumero
- Väline
	* Nimi:String
	* Paino:Double
