from pathlib import Path
from playwright.sync_api import sync_playwright
import json,os
root=Path(__file__).resolve().parent.parent
BASE=os.environ.get('PREVIEW_ORIGIN','http://127.0.0.1:4173')+os.environ.get('BASE_PATH','').rstrip('/')
routes=['/','/paslaugos/','/projektai/','/kompetencijos/','/kontaktai/']
report=[]
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 context=browser.new_context(viewport={'width':1440,'height':1050},device_scale_factor=1)
 page=context.new_page();errors=[]
 page.on('pageerror',lambda e:errors.append(str(e)))
 for width in [1440,390,320]:
  page.set_viewport_size({'width':width,'height':900})
  for route in routes:
   r=page.goto(BASE+route,wait_until='networkidle');assert r.status==200
   assert page.locator('h1').count()==1
   assert page.locator('html').get_attribute('lang')=='lt'
   assert page.locator('meta[name="description"]').get_attribute('content')
   assert page.locator('meta[name="robots"]').get_attribute('content')=='noindex, nofollow'
   assert page.locator('nav a[aria-current="page"]').count()==1
   overflow=page.evaluate('document.documentElement.scrollWidth > innerWidth')
   assert not overflow,(width,route,page.evaluate('document.documentElement.scrollWidth'))
   for img in page.locator('img').all():assert img.evaluate('(i)=>i.complete && i.naturalWidth>0')
   report.append({'viewport':width,'route':route,'status':'PASS'})
   if width in [1440,390]:
    slug='home' if route=='/' else route.strip('/')
    page.screenshot(path=str(root/f'docs/previews/{slug}-{width}.png'),full_page=True)
 page.set_viewport_size({'width':390,'height':844});page.goto(BASE+'/')
 toggle=page.locator('.menu-toggle');toggle.click();assert toggle.get_attribute('aria-expanded')=='true'
 page.get_by_role('navigation',name='Pagrindinė navigacija').get_by_role('link',name='Paslaugos',exact=True).click();page.wait_for_url('**/paslaugos/');assert page.locator('h1').inner_text().startswith('Inžineriniai')
 page.get_by_role('button',name='Atverti meniu').click();page.keyboard.press('Escape');assert page.get_by_role('button',name='Atverti meniu').get_attribute('aria-expanded')=='false'
 page.goto(BASE+'/projektai/');page.get_by_role('button',name='BMS',exact=True).click();assert page.locator('[data-category]:visible').count()==1
 page.get_by_role('button',name='Visos kryptys').click();assert page.locator('[data-category]:visible').count()==3
 context.grant_permissions(['clipboard-read','clipboard-write']);page.goto(BASE+'/kontaktai/');page.get_by_role('button',name='Kopijuoti užklausos ruošinį').click();page.wait_for_function("document.querySelector('.copy-status').textContent.includes('nukopijuotas')")
 assert 'Objektas ir vieta' in page.evaluate('navigator.clipboard.readText()')
 assert page.locator('.contact-heading .todo').count()==0
 assert page.locator('a[href="mailto:info@asgamyba.lt"]').count()>=1
 assert page.locator('a[href="tel:+37061001713"]').count()>=1
 for value in ['J. Janonio g. 8, Prienai','305725386','LT100013926116']:
  assert value in page.locator('.contact-heading').inner_text()
 assert page.get_by_role('link',name='Rašyti el. paštu').get_attribute('href').startswith('mailto:info@asgamyba.lt?subject=')
 page.goto(BASE+'/kompetencijos/')
 assert page.locator('time[datetime="2021-04-02"]').count()==1
 assert 'Komandos narių asmens duomenų neviešiname' in page.locator('main').inner_text()
 assert page.locator('.evidence-list .todo').count()==3

 # Verify all local navigation and asset URLs against the actual server.
 links=set()
 for route in routes:
  page.goto(BASE+route)
  links.update(page.locator('a[href^="/"], link[href^="/"], script[src^="/"], img[src^="/"]').evaluate_all('(els)=>els.map(x=>x.getAttribute("href")||x.getAttribute("src"))'))
 for link in links:
  pathname,_,anchor=link.partition('#');assert context.request.get(os.environ.get('PREVIEW_ORIGIN','http://127.0.0.1:4173')+pathname).status==200,link
  if anchor:
   page.goto(os.environ.get('PREVIEW_ORIGIN','http://127.0.0.1:4173')+pathname);assert page.locator('[id="'+anchor+'"]').count()==1,link
 assert context.request.get(BASE+'/neegzistuoja/').status==404
 assert not errors,errors
 browser.close()
(root/'docs/browser-checks.json').write_text(json.dumps({'viewports_and_routes':report,'mobile_menu':'PASS','keyboard_escape':'PASS','placeholder_filters':'PASS','clipboard_brief':'PASS','local_links_and_anchors':len(links),'404':'PASS','javascript_errors':errors},indent=2))
print(f'PASS: {len(report)} viewport/route combinations; mobile menu, keyboard, filters, clipboard, {len(links)} links/assets, 404. No JS errors.')
