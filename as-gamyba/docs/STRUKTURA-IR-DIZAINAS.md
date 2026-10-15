# MB „AS gamyba“ · kryptis 01

Tai pirmos versijos dizaino ir UX prototipas, ne produkcinė svetainė. Integruotas vartotojo pateiktas originalus SVG logotipas; paletė priderinta prie jo raudonos ir grafito spalvų. Tikrų projektų, partnerių, atestatų, sertifikatų ir nepagrįstų skaičių nėra.

## Sitemap

```text
Pradžia /
├── Paslaugos /paslaugos/
│   ├── #automatikos-skydai
│   ├── #elektra-pva
│   ├── #bms
│   ├── #integracijos
│   ├── #paleidimas
│   ├── #cctv
│   ├── #duomenu-tinklai
│   └── #modernizacija
├── Projektai /projektai/
│   └── Krypčių filtrai ir 3 aiškiai pažymėtos būsimo turinio vietos
├── Kompetencijos /kompetencijos/
│   ├── Apie įmonę
│   ├── Tikslinės auditorijos
│   ├── Patvirtinamų kompetencijų / dokumentų vieta
│   └── Darbo eiga
└── Kontaktai /kontaktai/
    ├── Kontaktai ir rekvizitai
    └── Vietinis užklausos ruošinio kopijavimas
```

Šiame etape atskirų projektų puslapių, dokumentų bibliotekos, naujienų ir backend nėra.

## Homepage wireframe

```text
DESKTOP
┌────────────────────────────────────────────────────────────┐
│ Tekstinis ženklas    Navigacija             Aptarkime       │
├─────────────────────────────┬──────────────────────────────┤
│ Veiklos kryptis             │ Abstrakti techninė           │
│ H1 / vertės pasiūlymas      │ automatikos skydo iliustracija│
│ Trumpas pristatymas         │                              │
│ CTA + paslaugų nuoroda      │                              │
├─────────────────────────────┴──────────────────────────────┤
│ Sprendimų krypčių juosta                                    │
├────────────────────────────────────────────────────────────┤
│ Paslaugos · 8 kortelės, 4 × 2                               │
├─────────────────────────────┬──────────────────────────────┤
│ Kompetencijos / protokolai  │ Principinė sistemų schema    │
├─────────────────────────────┴──────────────────────────────┤
│ Projektų preview · 3 placeholderiai, aiškūs TODO             │
├─────────────────────────────┬──────────────────────────────┤
│ Požiūrio pristatymas        │ 3 kompetencijų argumentai    │
├─────────────────────────────┴──────────────────────────────┤
│ Projekto aptarimo CTA                                      │
├────────────────────────────────────────────────────────────┤
│ Įmonė / navigacija / paslaugos / kontaktai                   │
└────────────────────────────────────────────────────────────┘

MOBILE
[Ženklas] [Meniu]
[Hero tekstas → CTA → techninė iliustracija]
[Sprendimų krypčių juosta]
[Paslaugų kortelės viena po kitos]
[Kompetencijos → principinė schema]
[Projektų placeholderiai viena po kitos]
[Požiūris → argumentai]
[CTA]
[Footer ir kontaktai]
```

## Dizaino principai

- Šviesus, šiek tiek šiltas fonas; kontrastinga tipografija; santūrus techninis charakteris.
- Pagrindinis akcentas — originalaus logotipo raudona `#DC0000`, teksto ir tamsių blokų pagrindas — grafitas `#2B2A29`. Šviesūs neutralūs paviršiai išlaiko erdvę ir techninį charakterį.
- Scheminis tinklelis, įrangos kontūrai ir ryšių linijos vietoje fiktyvių objektų fotografijų.
- Įmonės kompetencijos pristatomos per veiklos apimtį ir darbo principus, ne per išgalvotą stažą ar skaičius.
- Pirminis veiksmas — „Aptarkime jūsų projektą“, antrinis — „Mūsų paslaugos“.
- Toks pats header, footer, CTA ir kortelių charakteris visose skiltyse.
- Judesys apsiriboja trumpais hover pokyčiais; palaikoma `prefers-reduced-motion`.

## Dizaino sistema

| Elementas | Reikšmė |
|---|---|
| Puslapio fonas `--paper` | `#F5F5F5` |
| Pagrindinis tekstas `--ink` | `#2B2A29` |
| Antrinis tekstas `--muted` | `#6E6E6E` |
| Pagrindinis akcentas `--green` | `#DC0000` |
| Šviesus akcentas `--lime` | `#F5D9D5` |
| Linijos `--line` | `#DEDEDE` |
| Antrinis fonas `--soft` | `#ECECEC` |
| Šriftas | Arial / Helvetica / sans-serif; vietinis, be išorinių užklausų |
| H1 | 42–78 px; vidinių puslapių 40–66 px |
| H2 | 31–49 px |
| Pagrindinis tekstas | 14–16 px; antrinis kortelių tekstas 12 px |
| Mygtukai | Raudonas pilnas; alternatyvus kontūrinis; teksto nuoroda su rodykle |
| Kampai | Mygtukai 5 px; kortelės / panelės 6–8 px |
| Tinklelis | Iki 1240 px turinio plotis; 24–76 px šoninės paraštės |
| Spacing | 8 / 12 / 16 / 24 / 32 / 48 / 60 / 83 px |
| Breakpoints | 1100 / 800 / 480 px |
| Mobile meniu | Mygtukas su aria-expanded, Escape uždarymas, aiškios nuorodos |

Kortelėse naudojamas antraštės, piktogramos, paaiškinimo ir kryptinės nuorodos derinys. Nėra karuselių, automatinio video, sunkios animacijos ar trečiųjų šalių sekimo.

## Turinio sąžiningumas ir neužbaigtos vietos

- Kontaktai ir rekvizitai įvesti pagal įmonės pateiktus duomenis; el. pašto ir telefono nuorodos veikia.
- Originalus logotipas pateiktas vartotojo ir naudojamas nekeičiant jo formos bei proporcijų.
- Projektų kortelės nevaizduoja tikrų projektų. Filtrai leidžia išbandyti būsimos struktūros UX.
- Įmonės įkūrimo data ir veiklos pristatymas įrašyti. Komandos nariai neviešinami. SSVA / VERT dokumentų numeriai, apimtis ir galiojimas lieka `TODO` iki registrų patikros.
- Kontaktų forma nesiunčia duomenų: vietoje jos yra naudingas užklausos ruošinio kopijavimas.
- Svetainė neindeksuojama: `noindex, nofollow` ir `robots.txt`. Prieš publikavimą reikia patvirtinti turinį, domeną ir pakeisti indeksavimo nustatymus.

## SEO ir našumo pagrindas

Kiekvienas puslapis turi atskirą statinį HTML, lietuvių kalbos žymą, vieną H1, savo title / description ir Open Graph tekstus. Tik įvedus tikrą `siteUrl` generuojami canonical URL ir sitemap.xml. Nėra išgalvoto domeno ar LocalBusiness duomenų su netikrais kontaktais. Nėra framework runtime, išorinių šriftų ar JS bibliotekų. Puslapių turinys veikia be JavaScript; meniu, filtrai ir kopijavimas yra nedideli JS pagerinimai. Tai nėra atlikto SEO audito ar Lighthouse rezultato teiginys.
