# MB „AS gamyba“ — dizaino ir frontend versija 01

Pirma penkių puslapių svetainės kryptis. Statinis frontend, pritaikytas mobiliesiems. Be backend, npm bibliotekų ir nuotolinių šriftų.

## Paleidimas

Reikalingas Node.js 20 arba naujesnis. `npm install` nereikalingas.

```sh
cd as-gamyba
npm run dev
```

Naršyklėje atverti `http://localhost:4173`. Keičiant šaltinius pakartoti `npm run build` — šioje minimalioje versijoje nėra automatinio perkompiliavimo ar HMR. Veikiantis peržiūros serveris skaito atnaujintą `dist/`.

```sh
npm run build
npm run preview
```

Kitas prievadas: `PORT=8080 npm run dev` (POSIX aplinkoje).

## Puslapiai

- `/` — pilnas homepage: hero, 8 paslaugos, technologijos, projektų vietos, požiūris, CTA ir kontaktai footer.
- `/paslaugos/` — 8 paslaugų aprašymai, in-page navigacija, darbo eiga.
- `/projektai/` — neutrali projektų struktūra su veikiančiais filtrais.
- `/kompetencijos/` — įmonės kryptis, auditorijos ir kompetencijų pagrindimo vieta.
- `/kontaktai/` — tikrų kontaktų vieta ir vietinis užklausos ruošinio kopijavimas.

Sitemap, wireframe, tokenai ir UX sprendimai: [docs/STRUKTURA-IR-DIZAINAS.md](docs/STRUKTURA-IR-DIZAINAS.md).

## Kur įkelti logotipą

1. Įkelti SVG, WebP arba PNG į `public/assets/`, pvz., `public/assets/logo.svg`.
2. `content/site.json` nustatyti `"logo": "/assets/logo.svg"` ir tikslų `logoAlt`.
3. `src/styles.css` faile pakeisti `:root` spalvas pagal logotipą.
4. Paleisti `npm run build`.

Įtrauktas vartotojo pateiktas originalus AS gamyba SVG logotipas. Paletė priderinta prie jo raudonos `#DC0000` ir grafito `#2B2A29` spalvų. Logotipo proporcijos išsaugotos.

## Kur papildyti turinį

- `content/site.json` — įmonės pavadinimas, el. paštas, telefonas, adresas, rekvizitai, logotipas, tikras domenas `siteUrl`.
- `content/projects.json` — tik patvirtintų projektų sąrašas; dabar `[]`.
- `public/images/projects/` — būsimos patvirtintos projektų nuotraukos.
- `scripts/build.mjs` — puslapių tekstai, paslaugos ir komponentai.
- `src/styles.css` — bendra dizaino sistema ir responsive taisyklės.
- `public/assets/app.js` — mobilus meniu, projektų filtrai ir užklausos ruošinys.

Būsimo projekto įrašo schema (dabar tokių įrašų nesukuriama):

```json
{
  "title": "Patvirtintas projekto pavadinimas",
  "description": "Patvirtintas aprašymas",
  "category": "automatika",
  "image": "/images/projects/patvirtinta-nuotrauka.webp",
  "imageAlt": "Tikslus nuotraukos aprašymas",
  "scope": "Patvirtinta atliktų darbų apimtis"
}
```

Filtrų kategorijos: `automatika`, `bms`, `tinklai`. Prieš pridedant kitas kategorijas papildyti filtrų sąrašą generatoriuje. Projektų detalių puslapiai dar nekuriami — tai pirmo etapo peržiūros struktūra. Sertifikatai, atestatai, klientų ir partnerių ženklai neįtraukti; jie integruojami tik patvirtinus dizainą ir gavus tikrą medžiagą.

## Peržiūros ir patikra

`docs/previews/` — visų penkių puslapių desktop (1440 px) ir mobile (390 px) vaizdai. `docs/browser-checks.json` — naršyklės patikros rezultatai.

Papildoma kūrėjo patikra: `python scripts/check_frontend.py`, kai serveris jau veikia. Tam reikia Python Playwright ir Chromium; svetainės paleidimui jų nereikia.

## Deployment kryptis

`dist/` galima įkelti į Cloudflare Pages, Netlify ar bet kurį statinio hostingo serverį. Build komanda: `npm run build`; output katalogas: `dist`. GitHub Pages versija palaiko bazinį kelią: `BASE_PATH=/test SITE_URL=https://dariusserv-maker.github.io/test/ npm run build`. Lokaliai tokią versiją peržiūrėti su `BASE_PATH=/test PORT=4174 npm run preview`. Be `BASE_PATH` svetainė generuojama domeno šakniai.

GitHub peržiūrai paruoštos šakos `as-gamyba-preview` (šaltiniai) ir `gh-pages` (sugeneruotas turinys). Faktinis Pages veikimas priklauso nuo saugyklos Pages nustatymų. Prieš produkcinį paleidimą reikės įvesti tikrus kontaktus ir domeną, patvirtinti tekstus, pašalinti peržiūrai skirtą `noindex` / robots draudimą. Analitika, slapukai ir serverinė kontaktų forma neįdiegti.

## GitHub peržiūra ir automatiniai atnaujinimai

Numatytas adresas: https://dariusserv-maker.github.io/test/

Vienkartinis įjungimas: GitHub saugykloje **Settings → Pages → Build and deployment → Source: GitHub Actions**. Jei ankstesnis paleidimas nepavyko, atverti **Actions → AS gamyba preview** ir pakartoti paleidimą arba pasirinkti **Run workflow**, šaką `as-gamyba-preview`. Jeigu aplinkos `github-pages` taisyklės riboja šakas, leisti `as-gamyba-preview` per Settings → Environments.

`.github/workflows/as-gamyba-pages.yml` po `as-gamyba-preview` šakos pakeitimų automatiškai sugeneruoja svetainę, įkelia artefaktą ir publikuoja per oficialų `actions/deploy-pages`. Šis būdas nepriklauso nuo pakartotinio branch build aktyvavimo. `gh-pages` šaka papildomai saugo jau sugeneruotą pirmos versijos turinį, tačiau automatinei peržiūrai naudojama GitHub Actions publikacija. GitHub Actions ir Pages turi būti leidžiami saugykloje.

Papildomos `gh-pages` failų kopijos atnaujinimas su esama Git autentifikacija (tai savaime neaktyvina Actions publikacijos):

```sh
BASE_PATH=/test SITE_URL=https://dariusserv-maker.github.io/test/ npm run build
node scripts/publish-pages.mjs
```

`noindex` paliktas peržiūros puslapiuose. Tai nėra slaptažodžio apsauga: įjungta Pages peržiūra bus pasiekiama pagal jos adresą.
