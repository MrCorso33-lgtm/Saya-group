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
