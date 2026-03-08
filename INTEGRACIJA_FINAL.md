# WordPress Integration Guide: Saya Group Prototype (v3.0)

**Autor:** Manus AI
**Datum:** 08. Mart 2026.
**Verzija:** 3.0 (Comprehensive)

## 1. Filozofija: Custom Code First, Plugins kao Utility

Ovaj dokument je finalni vodič za integraciju našeg HTML prototipa u WordPress. Pristup je jasan: **naš kod je osnova, a pluginovi su pomoćni alati**. Koristimo naš postojeći, optimizovan frontend za sve što korisnik vidi (header, footer, meniji, kartice, layout), a pluginove koristimo isključivo za ono što se dešava u pozadini (upravljanje podacima, AJAX, CPT).

**Zašto ovaj pristup?**
- **Performanse:** Zadržavamo potpunu kontrolu nad brzinom učitavanja i renderovanjem.
- **Fleksibilnost:** Nismo ograničeni opcijama nekog page buildera.
- **Održivost:** Lakše je održavati čist, semantički kod nego kompleksne strukture widgeta.

## 2. Globalna podešavanja: Teme i stilovi

### 2.1. Child Theme

Sve izmene se rade u **custom child theme-u**. Ovo osigurava da update-ovi parent teme (npr. Hello Elementor) ne prepišu naš kod.

### 2.2. `header.php` i `footer.php` (100% Custom Code)

Naš `index.html` je podeljen na `header.php` i `footer.php`.

- **`header.php`:** Sadrži sve od `<!DOCTYPE>` do početka `<main>` taga. Uključuje `<head>`, top bar, glavni header sa logom, i navigaciju sa mega menijem. Ključna izmena je zamena statičkog `<title>` sa `wp_head();`.
- **`footer.php`:** Sadrži sve od `</main>` do `</html>`. Uključuje footer widgete, dno footera i `wp_footer();` pre `</body>`.

### 2.3. Glavni CSS i JS fajlovi

- **CSS:** Svi naši stilovi iz `<style>` bloka u `index.html` se prebacuju u `style.css` child teme. Ovo uključuje CSS variable (`:root`), stilove za header, footer, grid, kartice, itd.
- **JS:** Sav naš JavaScript iz `<script>` bloka se prebacuje u `main.js` (ili sličan fajl) i učitava preko `functions.php` koristeći `wp_enqueue_script`.

## 3. Analiza i integracija po komponentama

### 3.1. Header i Mega Meni

- **Implementacija:** 100% custom kod u `header.php`.
- **Dinamika:** Meni se registruje u `functions.php` (`register_nav_menus`). Da bi se zadržala naša HTML struktura mega menija, potrebno je napisati **custom `Walker_Nav_Menu` klasu**. Ova klasa će iterirati kroz stavke menija i generisati tačno onaj HTML koji naš CSS očekuje, uključujući `mega-menu-grid`, `mega-menu-column`, `mega-menu-title` itd.
- **Plugin:** **Nijedan.** Ne koristimo JetMenu.

### 3.2. Pretraga

- **Implementacija:** Naš custom UI (search bar, mega dropdown) ostaje. JS logika se blago modifikuje.
- **Dinamika:** U `main.js`, `CONFIG.prototypeMode` se postavlja na `false`. `doSearch()` funkcija se modifikuje da šalje `fetch` request na **JetSearch REST API endpoint** (`/wp-json/jet-search/v1/search`). Odgovor (JSON) se parsira i prikazuje u našem postojećem `renderResults()` funkciji.
- **Plugin:** **JetSearch** (samo kao backend data provider).

### 3.3. Homepage

- **Implementacija:** Telo stranice se gradi u Elementoru. Međutim, umesto standardnih widgeta, koristimo **kratke kodove (shortcodes)** koji pozivaju naše custom templejte.
- **Napredni pristup (preporučeno):** Kreirati shortcode u `functions.php` za svaku sekciju (npr. `[saya_hero_slider]`, `[saya_bento_grid]`, `[saya_products_tabs]`). Svaki shortcode učitava odgovarajući `.php` fajl iz `template-parts` direktorijuma koji sadrži naš HTML i WordPress loop.
- **Alternativa (lakša):** Koristiti Elementor HTML widget i direktno ubaciti naš HTML. Ovo je brže, ali teže za održavanje.
- **Hero Slider:** Naš postojeći JS (`changeSlide`, `goToSlide`) se koristi. Slike i tekst se mogu učitavati dinamički iz JetEngine postova ili ACF repeater polja.

### 3.4. Stranice kategorija (PLP - Product Listing Page)

- **Implementacija:** Koristi se **JetWooBuilder Category Template**. Unutar templejta, umesto JetWooBuilder widgeta za proizvode, koristimo **JetEngine Listing Grid**.
- **Zašto?** JetEngine Listing Grid nam daje 100% kontrolu nad HTML-om svake kartice proizvoda. U Listing Item-u, prebacujemo naš HTML za `.product-card` i dinamički povezujemo polja (slika, ime, cena, SKU) sa WooCommerce podacima.
- **Filteri:** **JetSmartFilters** se povezuju sa našim Listing Gridom. Stilovi za filtere (checkbox, range slider) se pišu u `style.css` da se uklope u naš dizajn.

### 3.5. Stranica proizvoda (PDP - Product Detail Page)

- **Implementacija:** Koristi se **JetWooBuilder Single Product Template**.
- **Galerija:** **JetProductGallery** je dobar izbor za glavnu galeriju. Stilovi se mogu prilagoditi.
- **Tabovi:** Naši postojeći tabovi (`Opis`, `Specifikacije`, `Preuzimanja`) se integrišu. Sadržaj tabova se vuče iz WooCommerce polja (opis, atributi) ili custom meta polja (za B2B preuzimanja).
- **Kalkulator:** Naš JS za kalkulator (`calculateArea`) ostaje. Vrednosti (npr. `1.44` za m² po kutiji) se mogu prebaciti u `data-` atribute da budu dinamičke.

### 3.6. Brendovi i Inspiracija (CPT i Taksonomije)

- **Struktura podataka:** **JetEngine** je **neophodan**.
    1. Kreira se **Custom Post Type (CPT)** pod nazivom "Projekti".
    2. Kreira se **Custom Taxonomy** pod nazivom "Brendovi" i povezuje se sa WooCommerce proizvodima.
- **Arhivske stranice (`/brendovi/`, `/inspiracija/`):**
    - Kreiraju se kao standardne WordPress stranice.
    - Na njih se dodaje **JetEngine Listing Grid** koji prikazuje ili taksonomiju "Brendovi" ili CPT "Projekti".
    - Naš JS za filtriranje (`filterBrands`, `filterProjects`) se menja da koristi **JetSmartFilters AJAX mehanizam**.
- **Single Projekat (`/inspiracija/{projekat}/`):
    - Kreira se templejt za CPT "Projekti" koristeći **JetThemeCore**.
    - Naš HTML za hotspotove i listu proizvoda se koristi unutar templejta. Podaci se vuku iz meta polja tog projekta (npr. ACF repeater za povezane proizvode).

## 4. Zaključak i preporuke

| Komponenta | Preporučeni pristup | Zašto? |
| :--- | :--- | :--- |
| **Header/Footer/Meni** | Custom `header.php` + `footer.php` + `Walker_Nav_Menu` | Maksimalne performanse i kontrola. |
| **Statične stranice (O Nama, Kontakt)** | Standardni WordPress templejti (`page-o-nama.php`) | Jednostavno i efikasno. |
| **Listing stranice (Kategorije, Brendovi)** | JetEngine Listing Grid + JetSmartFilters | Potpuna kontrola nad HTML-om kartice + moćan AJAX. |
| **Single stranice (Proizvod, Projekat)** | JetWooBuilder / JetThemeCore + naši HTML delovi | Kombinacija dinamike i custom dizajna. |
| **Forme (Kontakt, Newsletter)** | Contact Form 7 ili WPForms + naši stilovi | Pouzdano i sigurno rešenje za forme. |

Ovaj pristup minimizuje zavisnost od page buildera za ključne strukturne elemente, čime se dobija brz, unikatan i profesionalan sajt koji je lak za buduće održavanje.


## 5. E-commerce Flow: Korpa, Plaćanje, Lista Želja

Ove stranice su srce e-commerce funkcionalnosti. Pristup je hibridni: koristimo WooCommerce za backend logiku, a naš kod za frontend prikaz.

### 5.1. Korpa (`/korpa/`)

- **Implementacija:** Kreira se standardna WordPress stranica i dodeljuje joj se uloga "Cart Page" u WooCommerce podešavanjima (`WooCommerce > Settings > Advanced`).
- **Templejt:** Kreira se custom templejt `woocommerce/cart/cart.php` u child theme-u. Unutar ovog fajla, preuzimamo HTML iz našeg `korpa.html` prototipa i integrišemo ga sa WooCommerce hook-ovima i funkcijama. Naš JS za quantity update (`changeQty`, `recalcSummary`) se modifikuje da koristi WooCommerce AJAX za ažuriranje korpe, umesto da samo menja vrednosti u DOM-u.
- **Plugin:** **WooCommerce** (osnovna funkcionalnost).

### 5.2. Plaćanje (`/placanje/`)

- **Implementacija:** Slično kao korpa, stranica se dodeljuje u `WooCommerce > Settings > Advanced`.
- **Templejt:** Kreira se custom templejt `woocommerce/checkout/form-checkout.php` u child theme-u. Naš HTML iz `placanje.html` se koristi kao osnova. Polja forme se povezuju sa WooCommerce checkout poljima. Naš JS za validaciju (`submitOrder`) se dopunjuje WooCommerce validacijom.
- **Načini plaćanja:** U `WooCommerce > Settings > Payments`, aktiviraju se samo "Cash on delivery" i "Local pickup". Nema potrebe za dodatnim pluginovima.
- **Plugin:** **WooCommerce** (osnovna funkcionalnost).

### 5.3. Lista Želja (`/lista-zelja/`)

- **Implementacija:** Koristi se **JetCompareWishlist** plugin, koji već imaš.
- **Stranica:** Kreira se stranica i u nju se dodaje shortcode `[jet_wishlist]`.
- **Templejt (napredni pristup):** Da bi se postigao naš custom dizajn, kreira se templejt za JetEngine Listing Grid koji prikazuje wishlist iteme. U Listing Item-u se koristi naš HTML za karticu proizvoda. Ovaj Listing Grid se onda prikazuje na stranici umesto default shortcode-a.
- **"Pretvori u ponudu" dugme:** Ovo je custom funkcionalnost. U templejtu za wishlist item, dodaje se dugme koje na klik:
    1. Skuplja sve proizvode iz liste želja (naziv, količina, SKU).
    2. Preusmerava korisnika na `/kontakt/` stranicu.
    3. Prosleđuje podatke kroz URL parametre, koje naš JS na kontakt stranici čita i automatski popunjava u poruci B2B forme.
- **Plugin:** **JetCompareWishlist** (za backend logiku) + **JetEngine** (za custom prikaz).
## 6. Dokumentacija: Stranica za Pretragu (`pretraga.html`)

Ovaj dokument detaljno opisuje arhitekturu, funkcionalnost i preporučeni način integracije stranice za pretragu u WordPress okruženje, sa fokusom na custom rešenja i minimalnu upotrebu pluginova.

### 1. Arhitektura i Funkcionalnost

Stranica je dizajnirana kao sveobuhvatno rešenje za pretragu, zasnovano na uvidima iz B2C i B2B istraživačkih dokumenata. Ključni cilj je bio da se korisniku pruži relevantan, brz i lak za navigaciju rezultat, bez obzira na tip upita.

### 1.1. Ključne Komponente

| Komponenta | Opis | Insight iz istraživanja |
| :--- | :--- | :--- |
| **URL-driven query** | Stranica dinamički čita upit iz URL parametra `?q=` i ažurira sve relevantne delove interfejsa (naslov, breadcrumb, input polje). | Standardna praksa za deljive i bookmark-abilne rezultate. |
| **Tabovi za tipove rezultata** | Rezultati su grupisani u 4 taba: **Sve**, **Proizvodi**, **Kategorije** i **Brendovi**. | B2B dokument: "više paralelnih sistema organizacije" omogućava korisniku da brzo pronađe ono što ga zanima. |
| **Napredni filteri (Sidebar)** | Bogat set filtera omogućava sužavanje rezultata po **kategoriji, brendu, dimenziji, završnoj obradi, ceni i primeni**. | B2B dokument: "napredna pretraga po više parametara odjednom" je ključna za profesionalce. |
| **Stanje bez rezultata** | Ako nema rezultata, prikazuje se korisna poruka sa **sugestijama popularnih upita** i linkovima ka kategorijama i kontaktu. | B2C dokument: "Nema rezultata" ne sme biti ćorsokak. |
| **Prikaz (Grid/List)** | Korisnik može da bira između grid i list prikaza proizvoda. | B2C dokument: Korisnici imaju različite preferencije za pregled proizvoda. |
| **Responzivnost** | Filteri se na mobilnim uređajima sklanjaju u **drawer** koji se otvara na dugme, čime se štedi prostor na ekranu. | Standardna praksa za moderan web. |

### 1.2. JavaScript Logika

Sav JavaScript je napisan u vanilla JS i nalazi se unutar `<script>` taga na samoj stranici. Sve funkcije su samostalne i ne zavise od eksternih biblioteka (npr. jQuery).

- `runSearch()`: Pokreće novu pretragu na osnovu unosa u input polje.
- `switchTab()`: Menja prikaz između tabova (Sve, Proizvodi, Kategorije, Brendovi).
- `applyFilters()`, `clearFilters()`, `removeFilter()`: Upravljaju stanjem filtera (u prototipu samo prikazuju toast poruku).
- `setView()`: Menja prikaz između grid i list view.
- `openMobileFilters()`, `closeMobileFilters()`: Upravljaju prikazom filtera na mobilnim uređajima.

### 2. Integracija u WordPress

Cilj je iskoristiti naš custom frontend, a WordPress i pluginove koristiti za ono što rade najbolje: upravljanje podacima i AJAX endpoint-e.

### 2.1. Kreiranje Templejta

1. **Kreirati `search.php` templejt:** U vašem child theme-u, kreirajte fajl `search.php`. Ovo je standardni WordPress templejt koji se automatski koristi za prikaz rezultata pretrage.
2. **Kopirati HTML:** Prekopirajte kompletan HTML iz `pretraga.html` (od `<body>` do `</body>`) u `search.php`.
3. **Uključiti Header i Footer:** Na početku `search.php` dodajte `get_header();`, a na kraju `get_footer();`.

### 2.2. Povezivanje sa Podacima (Hibridni Pristup)

Ovo je ključni deo. Koristićemo **JetEngine** i **JetSmartFilters** za backend, a naš HTML i JS za frontend.

#### Korak 1: Priprema JetEngine

- **Listing Item za Proizvode:** U JetEngine, kreirajte novi Listing Item za proizvode. Unutar Elementor editora, koristite naš HTML za `.product-card` i povežite dinamičke podatke (slika, naziv, cena, brend) sa WooCommerce poljima.
- **Listing Item za Kategorije i Brendove:** Slično, kreirajte Listing Item-e za kategorije i brendove, koristeći naš HTML iz `pretraga.html`.

#### Korak 2: Prikaz Rezultata

- **Glavni Query:** WordPress `search.php` već ima glavni query (`$wp_query`) koji sadrži rezultate pretrage. Njega ćemo koristiti za prikaz proizvoda.
- **Prikaz Proizvoda:** Unutar `search.php`, na mestu gde se nalazi naš `.product-grid`, umesto statičkog HTML-a, koristite PHP petlju (`if ( have_posts() ) : while ( have_posts() ) : the_post(); ...`) i unutar nje renderujte JetEngine Listing Item za proizvode.
- **Prikaz Kategorija i Brendova:** Ovo je malo kompleksnije. JetSearch (koji koristimo za search bar) nažalost ne vraća termine taksonomija (kategorije, brendove) u svom AJAX odgovoru. Zato ćemo ih dobiti posebnim query-jem unutar `search.php`:

```php
// Unutar search.php, pre glavne petlje
$search_query = get_search_query();

$category_args = [
    'taxonomy'   => 'product_cat',
    'name__like' => $search_query,
];
$categories = get_terms($category_args);

$brand_args = [
    'taxonomy'   => 'brand', // Pretpostavka da je taksonomija 'brand'
    'name__like' => $search_query,
];
$brands = get_terms($brand_args);

// Kasnije u HTML-u, prođete kroz $categories i $brands i renderujete ih
```

#### Korak 3: Povezivanje Filtera

- **JetSmartFilters:** Ovo je **neophodan** plugin za AJAX filtriranje. U Elementor editoru za `search.php` (ako ga editujete kroz Theme Builder) ili kroz shortcode-ove, dodajte JetSmartFilters widgete (Checkbox, Range, etc.).
- **Povezivanje sa Listing Gridom:** Povežite filtere sa JetEngine Listing Gridom koji prikazuje proizvode. U podešavanjima filtera, kao "This filter for" odaberite "JetEngine".
- **Naš UI:** Naš HTML za filtere ostaje, ali `input` polja i `button`-i se moraju povezati sa JetSmartFilters JS API-jem da bi pokretali AJAX request. Ovo zahteva custom JS kod koji će na promenu našeg inputa pozvati odgovarajuću JetSmartFilters funkciju.

### 2.3. Preporuke i Best Practices

- **Ne koristiti Elementor HTML widget:** Izbegavajte da ceo kod stranice ubacite u jedan Elementor HTML widget. To je loše za performanse i održavanje. Koristite PHP templejte.
- **Odvojiti JS:** Sav JavaScript sa stranice prebacite u poseban `.js` fajl i učitajte ga kroz `functions.php` samo na `search.php` stranici (`if (is_search()) { ... }`).
- **Koristiti `wp_localize_script`:** Za prosleđivanje podataka iz PHP-a u JS (npr. AJAX URL, nonce), koristite `wp_localize_script` funkciju. To je siguran i ispravan način.
- **Optimizacija:** Pošto će stranica imati više query-ja, razmislite o keširanju rezultata za kategorije i brendove pomoću WordPress Transients API-ja da se smanji opterećenje baze.

Ovaj pristup vam daje potpunu kontrolu nad izgledom i osećajem stranice, dok istovremeno koristite moćne backend alate za upravljanje podacima i AJAX-om, što je idealan balans između custom rešenja i efikasnosti.
