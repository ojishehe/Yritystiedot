Eli siis, tällä koodilla voi hakea yritysten tietoja jonkun avoindata phr rajapinnan kautta.
Tällä hetkellä se siis toimii niin, että syötät jonkun random yrityksen y-tunnuksen haku kenttään, ja se hakee sulle ne tiedot mitä se löytää rajapinnasta.
Seuraava step mitä en osaa siis itse koodata, olisi se että tähän pitäisi lisätä hieman toimintoja. Yritän selittää mahdollisimman selkeesti.
ELI haku kriteereihin pitäis tulla 2 uutta haku kenttää alkuperäisen y-tunnus haun lisäksi jotka on: toimiala koodi haku sekä rekisteröintipäivä haku
eli siis tarkoittaa sitä että pystyt hakea yrityksen tietoja joko y-tunnuksen perusteella, yrityksen rekisteröinti päivän perusteella tai yritysten yhteisesti käyttämien toimialakoodien perusteella.
Oli vähän vaikea selittää, mutta y-tunnus on aina 1234567-8 (esimerkki) eli jokin 8 numeroinen jono numeroita, toimialakoodi on 4 numeroinen koodi joka viittaa siihen millä toimialalla yritys toimii. Viimeiseksi rekisteröinti päivä yleensä näissä piireissä se kirjoitetaan vvvv-kk-pp, eli siis se päivä milloin yritys on ensi kertaa rekisteröity rajapintaan.
Tässä on kaikki kriteerit haku kenttään. Eli kuin esimerkiksi asiakas syöttää y-tunnuksen, rekisteröinti päivän tai toimialakoodin, alapuolelle ilmestyy tottakai tulokset.
Seuraavaksi kerron mitä tuloksissa pitäisi näkyä.
perus lista tyyppinen haku tulos on hyvä jos pysyis about saman näköisessä ulkonäössä (nettisivu) kun on nyt niin on hyvä.
Mutta hakutuloksissa pitäis olla tottakai: yrityksen nimi, yrityksen verkkosivu (linkki?), yrityksen y-tunnus, yrityksen rekisteröintipäivä, yrityksen tila (onko esim yritys lakkautettu vai toiminnassa), osoite tiedot (kaupunki, postinumero katuosoite), yrityksen päätoimiala (eli joku yks virke mikä lukee rajapinnassa jotenkin esim "viestintälaitteiden tukkukauppa"), ja sitten viimeisimpänä yritysten tietojen viimeisin muokkaus päivä (löytyy rajapinnasta jostain vvvv-kk-pp muodossa eli milloin yrityksen tietoja on viimeksi muokattu).
Tässä on kaikki mitä koodin pitäisi sisältää, ei mitään kummempaa ulkoasua mutta kunhan se toimis. Oon tässä nyt jonkin aikaa hakannut päätä seinään tän kans, niin osaisitko mahdollisesti auttaa?
En siis osaa ite koodata ollenkaan tiedän about mitä noi koodin osat tekee ja miten se toimii. Pääasia on että koodi toimii visual codessa! 

kiitos :) 
Sorge oli vaikeet ohjeistukset :D 
