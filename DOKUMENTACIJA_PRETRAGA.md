# Dokumentacija: Stranica za Pretragu (`pretraga.html`)

Ovaj dokument detaljno opisuje arhitekturu, funkcionalnost i preporučeni način integracije stranice za pretragu u WordPress okruženje, sa fokusom na custom rešenja i minimalnu upotrebu pluginova.

## 1. Arhitektura i Funkcionalnost

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

## 2. Integracija u WordPress

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
