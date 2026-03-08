# Uputstvo za Integraciju HTML Prototipa u WordPress (Custom-Code-First)

**Autor:** Manus AI
**Datum:** 08. Mart 2026.
**Verzija:** 2.0

## 1. Uvod i Filozofija

Ovaj dokument pruža uputstvo za integraciju statičkog HTML prototipa u WordPress, prateći **"Custom Code First"** filozofiju. Cilj je da se iskoristi naš postojeći, optimizovan kod za frontend (header, footer, search, mega meni), a da se pluginovi (Elementor, Crocoblock) koriste isključivo tamo gde su neophodni — za upravljanje dinamičkim podacima i kompleksnim backend funkcionalnostima (WooCommerce, CPT, AJAX filteri).

Ovim pristupom zadržavamo potpunu kontrolu nad performansama i izgledom ključnih delova sajta, dok istovremeno koristimo moćne alate za ono što oni najbolje rade.

## 2. Analiza postojećih pluginova i njihov opseg

Pluginovi se koriste samo za ono što je apsolutno neophodno.

| Plugin | Svrha | Opseg korišćenja |
| :--- | :--- | :--- |
| **Elementor Pro** | Page Builder za sadržaj | Koristi se za kreiranje tela (body) stranica, **ne za header/footer** |
| **WooCommerce** | E-commerce platforma | Osnova za proizvode, korpu, plaćanje |
| **JetEngine** | Dinamički podaci | **Neophodan** za CPT (Projekti), taksonomije (Brendovi) i meta polja |
| **JetSmartFilters** | AJAX Filteri | **Neophodan** za filtriranje proizvoda i projekata |
| **JetWooBuilder** | Templejti za WooCommerce | **Neophodan** za dinamičke stranice kategorija i proizvoda |
| **JetProductGallery** | Galerije za proizvode | Preporučeno za napredne galerije na PDP-u |
| **JetCompareWishlist** | Lista želja / Poređenje | Koristi se |
| **JetSearch** | Pretraga (backend) | **Neophodan** — naš custom frontend poziva JetSearch REST endpoint |
| ~~JetMenu~~ | ~~Meni~~ | **Ne koristi se.** Koristimo našu custom implementaciju. |

## 3. Strategija integracije

### 3.1. Header, Footer i Meni (100% Custom Code)

Naš postojeći kod za header, footer i mega meni je već napisan i optimizovan. Nema potrebe za JetMenu ili Elementor Header/Footer.

1.  **Kreiranje `header.php` i `footer.php`:** U vašem WordPress child theme-u, kreirajte fajlove `header.php` i `footer.php`.
2.  **Kopiranje koda:**
    *   Iz `index.html` prototipa, kopirajte sav kod od početka do `<main>` taga u `header.php`.
    *   Kopirajte sav kod od `</main>` taga do kraja u `footer.php`.
3.  **WordPress Funkcije:**
    *   U `header.php`, zamenite statički `<title>` tag sa `wp_head();`.
    *   U `footer.php`, pre `</body>` taga, dodajte `wp_footer();`.
4.  **Meni:** Statički meni u `header.php` zamenite sa `wp_nav_menu()`. Biće potrebno registrovati novu menu lokaciju u `functions.php` i potencijalno napisati custom Walker klasu da bi se HTML struktura mega menija poklopila 100% sa našim CSS-om.

### 3.2. Pretraga (Custom Frontend + JetSearch Backend)

Naš header ima potpuno custom search UI (mega dropdown, keyboard navigacija, highlight, loading state). JetSearch se koristi **isključivo kao data source** — naš JS poziva njegov REST endpoint i prikazuje rezultate u našem custom dropdownu.

1.  **Aktivacija:** U kodu headera, u `CONFIG` objektu, promenite `prototypeMode: true` u `prototypeMode: false` i dodajte `apiUrl` koji pokazuje na JetSearch REST endpoint.
2.  **JetSearch endpoint:** JetSearch izlaže REST API na adresi `/wp-json/jet-search/v1/search`. Naš `doSearch()` funkcija treba da šalje GET request na ovaj endpoint sa parametrima `search_query`, `post_type=product` i `posts_per_page=5`.
3.  **Mapiranje odgovora:** JetSearch vraća JSON sa listom postova. Potrebno je mapirati polja (`post_title`, `permalink`, `price`, `thumbnail`) na naše `MOCK_PRODUCTS` strukturu.
4.  **Rezultati pretrage (stranica):** Za stranicu sa svim rezultatima (kada korisnik pritisne Enter), koristite standardni WordPress `search.php` templejt u child theme-u, stilizovan prema prototipu.

### 3.3. Globalni stilovi (Elementor + Custom CSS)

1.  **Elementor Site Settings:** Unesite globalne boje i fontove iz prototipa da bi Elementor widgeti bili konzistentni.
2.  **Glavni CSS:** CSS za header, footer i ostale custom elemente treba da se učitava preko `functions.php` (`wp_enqueue_style`).

## 4. Integracija po stranicama (Ažurirani pristup)

Za sve stranice, koristite `get_header();` na početku i `get_footer();` na kraju templejta.

| Stranica | Implementacija | Pluginovi |
| :--- | :--- | :--- |
| **Homepage** | Elementor za body. | Elementor, JetEngine (za listinge) |
| **Kategorije** | JetWooBuilder Category Template. | JetWooBuilder, JetSmartFilters |
| **Proizvod (PDP)** | JetWooBuilder Single Product Template. | JetWooBuilder, JetProductGallery |
| **Brendovi** | Elementor + JetEngine Listing Grid za taksonomiju "Brendovi". | Elementor, JetEngine, JetSmartFilters |
| **Inspiracija** | Elementor + JetEngine Listing Grid za CPT "Projekti". | Elementor, JetEngine, JetSmartFilters |
| **Single Projekat** | JetThemeCore Single Post Template za CPT "Projekti". | JetThemeCore, JetEngine |

## 5. Zaključak (Revidirano)

Ovaj hibridni pristup je optimalan. Zadržavamo potpunu kontrolu i performanse nad ključnim delovima sajta (header, footer, search) koristeći naš postojeći, provereni kod. Istovremeno, delegiramo upravljanje kompleksnim, dinamičkim podacima (proizvodi, filteri, CPT) moćnim pluginovima koji su za to i napravljeni. Rezultat je sajt koji je brz, lak za održavanje i skalabilan.
