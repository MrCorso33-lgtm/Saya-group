# Uputstvo za Integraciju HTML Prototipa u WordPress

**Autor:** Manus AI
**Datum:** 08. Mart 2026.

## 1. Uvod

Ovaj dokument pruža detaljno uputstvo za integraciju statičkog HTML/CSS/JS prototipa u postojeću WordPress instalaciju sa **Elementor Pro** i **Crocoblock (JetEngine)** pluginovima. Cilj je da se iskoristi maksimalan potencijal postojećih alata za kreiranje dinamičkog sajta koji je lak za održavanje, uz zadržavanje dizajna i funkcionalnosti prototipa.

## 2. Analiza postojećih pluginova

Na osnovu pregleda `plugins.php` stranice, identifikovan je sledeći ključni set alata:

| Plugin | Svrha | Status |
| :--- | :--- | :--- |
| **Elementor Pro** | Glavni page builder | Aktivan |
| **WooCommerce** | E-commerce platforma | Aktivan |
| **JetEngine** | Kreiranje Custom Post Types (CPT), taksonomija, meta polja | Aktivan |
| **JetSmartFilters** | Napredno filtriranje (AJAX) | Aktivan |
| **JetWooBuilder** | Template-i za WooCommerce stranice | Aktivan |
| **JetProductGallery** | Galerije za proizvode | Aktivan |
| **JetCompareWishlist** | Funkcionalnost poređenja i liste želja | Aktivan |
| **JetSearch** | Napredna pretraga (AJAX) | Aktivan |
| **JetMenu** | Kreiranje mega menija | Aktivan |

Ovaj set alata je **idealan** za implementaciju svih funkcionalnosti iz prototipa bez potrebe za dodatnim pluginovima.

## 3. Strategija integracije: Od statike do dinamike

Osnovna strategija je da se statički HTML elementi zamene dinamičkim Elementor widgetima i JetEngine listingima. Globalni stilovi (fontovi, boje) će biti definisani u Elementor Site Settings, a specifični stilovi će biti dodati kao Custom CSS gde je potrebno.

### 3.1. Globalni stilovi (Elementor Site Settings)

Prvi korak je definisanje globalnih stilova u Elementor-u kako bi se osigurala konzistentnost. Idite na **WordPress Dashboard → Elementor → Settings → Site Settings**.

- **Global Colors:** Unesite sve boje iz `:root` CSS varijabli prototipa (`--primary`, `--secondary`, `--background` itd.).
- **Global Fonts:** Definišite globalne fontove (Playfair Display za naslove, Montserrat za tekst).
- **Typography:** Podesite osnovnu tipografiju za Body, H1, H2, H3 itd.
- **Buttons:** Stilizuhte globalni izgled dugmadi.

### 3.2. Kreiranje Header-a i Footer-a (JetThemeCore)

Prototip namerno nema header i footer. Potrebno ih je kreirati kao globalne templejte.

1. Idite na **Crocoblock → JetThemeCore → Theme Builder**.
2. Kreirajte novi **Header** templejt i dodelite ga na **Entire Site**.
3. Koristite **JetMenu** widget da rekreirate navigaciju iz prototipa, uključujući mega meni za brendove.
4. Kreirajte novi **Footer** templejt i dodelite ga na **Entire Site**.

## 4. Integracija po stranicama

### 4.1. Homepage (`index.html`)

1. Kreirajte novu stranicu u WordPressu i otvorite je sa Elementorom.
2. **Hero sekcija:** Koristite Elementor-ov **Slides** widget.
3. **Featured Categories:** Koristite JetEngine **Listing Grid** widget. Kreirajte Listing Item templejt koji prikazuje WooCommerce kategorije (slika, naziv).
4. **Novi Proizvodi / Popularni Proizvodi:** Koristite JetWooBuilder **Products Grid** widget.
5. **Inspirišite Se Našim Projektima:** Koristite JetEngine **Listing Grid**. Biće potrebno kreirati CPT "Projekti" (vidi sekciju 5.1).
6. **Brendovi:** Koristite **Image Carousel** widget sa logoima brendova.

### 4.2. Stranica Pretrage (`pretraga.html`)

**JetSearch** je ključan za ovu funkcionalnost.

1. U header-u, zamenite statičku search ikonu sa **JetSearch AJAX Search** widgetom.
2. U podešavanjima widgeta, definišite koje sve post type-ove želite da pretražuje (Products, Posts, Pages, Projekti, Brendovi).
3. Stilizuhte rezultate koji se pojavljuju uživo (live search) da se poklapaju sa dizajnom prototipa.
4. Nije potrebno kreirati posebnu `pretraga.html` stranicu — JetSearch sve radi kroz AJAX overlay.

### 4.3. Stranice Kategorija (`plocice.html`, `sanitarije.html`...)

Ovo su WooCommerce arhivske stranice.

1. Idite na **Crocoblock → JetWooBuilder** i kreirajte novi **Category Template**.
2. Dodelite templejt svim željenim kategorijama proizvoda.
3. Unutar templejta, koristite **Products Loop** widget iz JetWooBuilder-a da prikažete proizvode.
4. **Filteri:** Sa leve strane, dodajte **JetSmartFilters** widgete (Sorting, Rating, Price Range, Checkboxes za atribute kao što su dimenzije, boja, završna obrada).

### 4.4. Stranica Proizvoda (PDP - `product-carrara-white.html`)

1. Idite na **Crocoblock → JetWooBuilder** i kreirajte novi **Single Product Template**.
2. Koristite **JetProductGallery** widget za glavnu sliku i thumbnail-e.
3. Koristite standardne WooCommerce widgete iz JetWooBuilder-a za naziv, cenu, opis, Add to Cart dugme.
4. Za tabove (Opis, Specifikacije, Recenzije), koristite **Tabs** widget i u njega ubacite dinamičke podatke.

### 4.5. Stranica Brendova (`brendovi.html`)

1. Kreirajte novu taksonomiju "Brendovi" preko **JetEngine → Taxonomies** i povežite je sa **Products**.
2. Svakom proizvodu dodelite odgovarajući brend.
3. Kreirajte novu stranicu "Brendovi" i otvorite je sa Elementorom.
4. Koristite **JetEngine Listing Grid** da prikažete sve termine iz taksonomije "Brendovi".
5. Kreirajte **Listing Item** templejt za jedan brend (logo, naziv, opis, link ka arhivi).
6. **Filter po kategoriji:** Dodajte **JetSmartFilters Checkboxes** widget koji filtrira brendove na osnovu WooCommerce kategorije proizvoda sa kojima su povezani.

### 4.6. Stranice Inspiracije (`inspiracija.html`, `inspiracija-projekat.html`)

Ovo zahteva kreiranje Custom Post Type-a.

1. **Kreiranje CPT:** Idite na **JetEngine → Post Types** i kreirajte novi CPT pod nazivom "Projekti".
2. **Meta Polja:** Dodajte meta polja za projekat: `prostor` (Kupatilo, Kuhinja...), `stil` (Moderno, Klasično...), `povrsina`, `lokacija`.
3. **Povezivanje sa proizvodima:** Najvažniji korak. Dodajte **Related Posts** meta polje koje će vam omogućiti da za svaki projekat odaberete više proizvoda iz WooCommerce-a.
4. **Arhiva (`inspiracija.html`):** Kreirajte novu stranicu i koristite **JetEngine Listing Grid** da prikažete sve "Projekti" postove. Dodajte **JetSmartFilters** za prostor i stil.
5. **Single Projekat (`inspiracija-projekat.html`):** Kreirajte **Single Post Template** u JetThemeCore za CPT "Projekti".
   - **Galerija:** Koristite standardni gallery widget.
   - **Hotspots:** Elementor Pro ima **Image Hotspot** widget. Možete ga koristiti, ali za dinamičko povezivanje sa proizvodima, biće potrebno malo Custom JS-a ili alternativni pristup.
   - **"Proizvodi iz ovog projekta":** Koristite **JetEngine Listing Grid** koji prikazuje povezane proizvode (iz koraka 3).

## 5. Zaključak

Kombinacija Elementor Pro i Crocoblock paketa pruža sve potrebne alate za vernu i funkcionalnu implementaciju HTML prototipa. Ključ uspeha leži u pravilnom postavljanju dinamičkih relacija kroz JetEngine (CPT, taksonomije, meta polja) i korišćenju JetWooBuilder-a za templejte WooCommerce stranica. Ovim pristupom, sajt će biti ne samo vizuelno identičan prototipu, već i potpuno dinamičan i lak za buduće ažuriranje od strane klijenta.
