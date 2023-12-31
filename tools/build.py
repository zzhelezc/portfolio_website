#!/usr/bin/env python3

import os
from photo_data import *
import dominate
from dominate.tags import *
from collections import namedtuple
from jinja2 import Template
import json
from dominate.util import raw

PATH = os.environ['WEBSITE_ROOT']
RELATIVE_PATH = '/photos'
PHOTO_PATH = PATH + RELATIVE_PATH

scrapbook_entries = []

####################################################################################
# Global Config
####################################################################################
def dir_to_href(d):
    return d.lower().replace(' ', '_').replace(':', '_') + '.html'

config = {
    'title': {
        'str': 'Zhulien Zhelezchev',
        'href': 'index.html'
    },

    'nav_prepend': [
         {
            'title': 'The Scrapbook Journal',
            'href': 'scrapbook.html',
            'template': 'templates/scrapbook.html',
            'nav_btm': False,
             
        },
    ],

    'nav_append': [
        {
            'title': 'About',
            'href': 'about.html',
            'template': 'templates/about.html',
            'nav_btm': True
        },
        # {
        #     'title': 'Zine',
        #     'href': 'zine.html',
        #     'template': 'templates/zine-etsy.html'
        # },
    ],

    'unliked_templated': [
        {
            'template': 'templates/zine.html',
            'filename': 'zine-flipbook.html'
        }
    ],

    'dir_to_href': dir_to_href,
    
}



####################################################################################
# Nav bar
####################################################################################

def gen_nav_bar():
     dirs = list_photo_directories()

     titles = []
     for d in dirs:
        cfg = load_sequence_cfg(d)
        nav_href = cfg['href']

        if not cfg['unlist']:
            titles.append((nav_href, cfg['title']))

     return gen_nav(titles)   

def gen_nav(titles):
    sidebar_container = div(cls='sidebarContainer')
    sidebar = div(cls='sidebar')
    navigation = nav(id='navigation')
        
    items = ul()
                
    items += li(h1(a(config['title']['str'],
                     href=config['title']['href'])),
                cls='logo', id='navItem')


    if config['nav_prepend']:
        for n, item in enumerate(config['nav_prepend']):
            # title =  item['title'] if item['nav_btm'] else f"➢ {item['title']}"
            items += li(a(f"➢ {item['title']}", href=item['href']),
                        cls='sidebarBottom' if item['nav_btm'] else 'navI',
                        id='navItem')

    for nav_href, page_title in titles:
        if page_title == 'index':
            continue
                        
        items += li(a(f"➢ {page_title}", href=nav_href),
                       id='navItem',
                    cls='navI')

    if config['nav_append']:
        for n, item in enumerate(config['nav_append']):
            # title =  item['title'] if item['nav_btm'] else f"➢ {item['title']}"
            items += li(a(f"➢ {item['title']}", href=item['href']),
                        cls='sidebarBottom' if item['nav_btm'] else 'navI',
                        id='navItem')
             

            

    navigation.add(items)
    sidebar.add(navigation)
    sidebar_container.add(sidebar)
           
    return sidebar_container 

####################################################################################
# Photo Gallery
####################################################################################

def gen_section_html(images, cfg):
    with div(cls='gallery') as gallery:
        if 'header' in cfg:
            gallery.add(h2(a(cfg['header']['content'],
                             href=cfg['header']['href'],
                             )))
            
        with div(cls='swiper', navigation="true"):
            with div(cls='swiper-wrapper'):
                for n, i in enumerate(images):
                    with div(cls='swiper-slide'):
                        img(src=f'{i}', loading='lazy')
                        div(cls='swiper-lazy-preloader')

            div(cls='swiper-pagination')            
            # div(cls='swiper-button-prev')
            # div(cls='swiper-button-next')
        return gallery



def gen_photo_section(directory):
    cfg = load_sequence_cfg(directory)
    images = [f'photos/{directory}/{i}' for i in cfg['sequence']]

    return gen_section_html(images, cfg)

####################################################################################
# Misc
####################################################################################
def gen_head_contents():
        title(config['title']['str'])
        meta(charset='utf-8')
        meta(name="viewport", content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0")
        meta(name='description', content=f"{config['title']['str']}'s photography")
        meta(property='og:title', content=config['title']['str'])
        meta(property='og:description', content=f"{config['title']['str']}'s photography")

        link(rel="stylesheet", href="style.css")
        link(rel="stylesheet", href="swiper.css")

def gen_head():
    with head() as h:
        gen_head_contents()
        return h
    
def gen_header():
    return header(a(config['title']['str'], href=config['title']['href']))

def gen_goat_counter():
    s = script(src="//gc.zgo.at/count.js", _async=True)
    s['data-goatcounter']="https://kappa.goatcounter.com/count"
    return s

def gen_scrapbook_entries():
    items = ul()
    for n, item in enumerate(scrapbook_entries):
        with div() as d:
            title = raw(f'➤ {item["title"]} &nbsp;&nbsp; {item["date"]}')
            li(h2(a(title, href=item['href']), cls='weeklyProj'))

            with open(item['desc'], 'r') as f:
                p(f.readlines())

        items += d
        
                
    return items
    
####################################################################################
# Pages 
####################################################################################

def gen_page(directory):
    cfg = load_sequence_cfg(directory)
    filename = cfg['href']

    doc = dominate.document(title=None)

    if 'scrapbook_entry' in cfg:
        scrapbook_entries.append({
            'title': cfg['title'],
            'href': cfg['href'],
            'date': cfg['scrapbook_entry']['date'],
            'desc': f"{PHOTO_PATH}/{directory}/{cfg['scrapbook_entry']['desc']}"
        })

    with doc.head:
        gen_head_contents()

    with doc:
        gen_header()
        gen_nav_bar()
        gen_photo_section(directory)
        script(src="swiper.js")
        script(src=cfg.get('swiper_config', 'script.js'))
        gen_goat_counter()

        
            

    dir = os.path.dirname(filename)
    if dir !='':
        os.makedirs(dir, exist_ok=True)
        
    with open(filename, 'w') as f:
        f.write(str(doc))

def gen_templated_page(template_filename, filename):
    data = {
        'head':    gen_head(),
        'header':  gen_header(),
        'sidebar': gen_nav_bar(),
        'goat_counter': gen_goat_counter(),
        'scrapbook_entries': gen_scrapbook_entries()
    }

    with open(template_filename, 'r') as tf:
        template = Template(tf.read())
        
        dir = os.path.dirname(filename)
        if dir != '':
            os.makedirs(dir, exist_ok=True)
            
        with open(filename, 'w') as f:
            f.write(template.render(data))


def gen_templated_pages():
    print('  linked')

    for i in config['nav_prepend']:
        template = i.get('template', False)
        if template:
            print(f"    - {i['href']} from {template}")
            gen_templated_page(template, i['href'])
    
    for i in config['nav_append']:
        template = i.get('template', False)
        if template:
            print(f"    - {i['href']} from {template}")
            gen_templated_page(template, i['href'])

    print('  unlinked')
    for i in config['unliked_templated']:
        print(f"    - {i['filename']} from {i['template']}")
        gen_templated_page(i['template'], i['filename'])

def list_photo_directories():
    dirs = [f.name for f in os.scandir(PHOTO_PATH) if f.is_dir()]
    return [d for d in dirs if os.path.isfile(f'{PHOTO_PATH}/{d}/sequence.json')]

def load_sequence_cfg(d):
    with open(f'{PHOTO_PATH}/{d}/sequence.json', 'r') as f:
            return json.load(f)

def main():
    photo_directories = []
    for d in list_photo_directories():
        print(f'generating page for {d}')
        gen_page(d)
    print('done.')    

    print('generating templated pages...')
    gen_templated_pages()
    print('done.')
        

if __name__ == '__main__':
    main()
