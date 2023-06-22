#!/usr/bin/env python3

import os
from photo_data import *
import dominate
from dominate.tags import *
from collections import namedtuple
from jinja2 import Template

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


    'nav_append': [
        {
            'title': 'About',
            'href': 'about.html',
            'template': 'templates/about.html'
        },
        {
            'title': 'Zine',
            'href': 'zine.html',
            'template': 'templates/zine-etsy.html'
        },
        {
            'title': 'Instagram',
            'href': 'https://www.instagram.com/wandering_nonsense/'
        }
    ],

    'unliked_templated': [
        {
            'template': 'templates/zine.html',
            'filename': 'zine-flipbook.html'
        }
    ],

    'dir_to_href': dir_to_href,

    'swiper_config': {
        'index.html': 'swiper-fade.js',
        'lost_in_time.html': 'swiper-fade.js'
    }
    
}



####################################################################################
# Nav bar
####################################################################################

def gen_nav_bar():
     dirs = list(photos.keys())

     titles = []
     for d in dirs:
        nav_href = config['dir_to_href'](d)
        titles.append((nav_href, d))

     return gen_nav(titles)   

def gen_nav(titles):
    sidebar_container = div(cls='sidebarContainer')
    sidebar = div(cls='sidebar')
    navigation = nav(id='navigation')
        
    items = ul()
                
    items += li(h1(a(config['title']['str'],
                     href=config['title']['href'])),
                cls='logo', id='navItem')

    for nav_href, page_title in titles:
        if page_title == 'index':
            continue
                        
        items += li(a(page_title, href=nav_href),
                       id='navItem')

    if config['nav_append']:
        for n, item in enumerate(config['nav_append']):
        
            items += li(a(item['title'], href=item['href']),
                       cls='sidebarBottom' if n == 0 else '',
                       id='navItem')

    navigation.add(items)
    sidebar.add(navigation)
    sidebar_container.add(sidebar)
           
    return sidebar_container 

####################################################################################
# Photo Gallery
####################################################################################

def gen_section_html(images):
    with div(cls='gallery') as gallery:
        with div(cls='swiper'):
            with div(cls='swiper-wrapper'):
                for n, i in enumerate(images):
                    with div(cls='swiper-slide'):
                        img(src=f'{i}', loading='lazy')
                        div(cls='swiper-lazy-preloader')
                
        return gallery



def gen_photo_section(album):
    d = album
    items = photos[d]
    images = []

    for i in items:
        
        if isinstance(i, tuple):
            a = i[0]
            b = i[1]

            a1 = a.replace('.jpg', '')
            b1 = b.replace('.jpg', '')
            
            cmd = f'montage "./photos/{d}/{a}" "./photos/{d}/{b}" -tile 2x1 -geometry +40+0 "./photos/{d}/{a1}-{b1}.jpg"'
                
            os.system(cmd)
            images.append(f'photos/{d}/{a1}-{b1}.jpg')

        else:
             images.append(f'photos/{d}/{i}')
             

    page = gen_section_html(images)

    return page

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
####################################################################################
# Pages 
####################################################################################

def gen_page(directory):
    filename = config['dir_to_href'](directory)

    doc = dominate.document(title=None)

    with doc.head:
        gen_head_contents()

    with doc:
        gen_header()
        gen_nav_bar()
        gen_photo_section(directory)
        script(src="swiper.js")
        script(src=config['swiper_config'].get(filename, 'script.js'))
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
        'goat_counter': gen_goat_counter()
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
    for i in config['nav_append']:
        template = i.get('template', False)
        if template:
            print(f"    - {i['href']} from {template}")
            gen_templated_page(template, i['href'])

    print('  unlinked')
    for i in config['unliked_templated']:
        print(f"    - {i['filename']} from {i['template']}")
        gen_templated_page(i['template'], i['filename'])
        
            
def main():
    for d in list(photos.keys()):
        print(f'generating page for {d}')
        gen_page(d)
    print('done.')    

    print('generating templated pages...')
    gen_templated_pages()
    print('done.')
        

if __name__ == '__main__':
    main()
