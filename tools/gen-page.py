#!/usr/bin/env python3

from photo_data import *
import sys




def gen_section_html(title, group_id, images):
    images_body = ''
    
    for n, i in enumerate(images):
        item = (
            f'<div class="swiper-slide" >\n' 
            f'<img src="{i}" loading="lazy" \>\n'
            '<div class="swiper-lazy-preloader"></div>\n'
            '</div>\n'
        )
        images_body += item 
    
    page = (f'<section id="{group_id}">\n'
            '<div class="gallery">\n'
            '<div class="swiper">\n'
            '<div class="swiper-wrapper">\n'
            f'{images_body}\n'
            '</div>\n'
            '</div>\n'
            '</div>\n'
            '</section>\n'
            )

    return page



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
             

    title = d.lower().replace(' ', '_').replace(':', '_')
    page = gen_section_html(d, title, images)
    page += '\n\n\n'

    # with open(filename, 'w') as f:
    #     f.write(page)
    return page


def gen_nav(titles):
    titles_html = ''
    for n, t in titles:
        if t == "index":
            continue
        titles_html += f'<li id="navItem"><a href="{n}.html">{t}</a></li>\n'
    
    page = ('<div class="sidebarContainer">\n'
            '<div class="sidebar">\n'
            '<nav id="navigation">\n'
            '<ul>\n'
            '<li class="logo" id="navItem">\n'
            '<h1><a href="index.html">Zhulien Zhelezchev</a></h1>\n'
            '</li>\n'
            f'{titles_html}'
            '<li class="sidebarBottom" id="navItem"><a href="about.html">About</a></li>\n'
            '<li id="navItem"><a href="https://www.instagram.com/wandering_nonsense/">Instagram</a></li>\n'
            '</ul>\n'
            '</nav>\n'
            '</div>\n'
            '</div>\n'
            )

    return page

def gen_page(d, titles):
    filename = d.lower().replace(' ', '_').replace(':', '_') + '.html'

    page = (
        '<!DOCTYPE html>\n'
        '<html lang="en">\n'
        '<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1, maximum-scale=1, user-scalable=0">\n'
        '<title>Zhulien Zhelezchev</title>\n'
        '<meta name="description" content="Zhulien Zhelezchev">\n'
        '<!-- Recommended minimum -->\n'
        '<meta property="og:title" content="Zhulien Zhelezchev">\n'
        '<meta property="og:description" content="Zhulien Zhelezchev">\n'
        '<!-- <meta property="og:image" content="img/site-image.jpg"> -->\n'
        '<link rel="stylesheet" href="style.css">\n'
        '<link rel="stylesheet" href="swiper.css" />\n'
        '</head>\n'
        '<header>\n'
        '<a href="index.html">Zhulien Zhelezchev</a>\n'
        '</header>\n'
        '<body>\n'
        '<main>\n'
        f'{gen_nav(titles)}\n'
        f'{gen_photo_section(d)}\n'
        # f'{load_page("about.html")}'
        '</main>\n'
        '<script src="swiper.js"></script>\n'
        '<script src="script.js"></script>\n'
        '</body>\n'
        '</html>\n'
    )


    with open(filename, 'w') as f:
        f.write(page)

def load_page(filename):
    with open(filename, 'r') as file:
        return file.read()


def gen_pages(dirs):
    titles = []
    
    for d in dirs:
        nav_title = d.lower().replace(' ', '_').replace(':', '_')
        titles.append((nav_title, d))

    for d in dirs:
        print(f'generating page for {d}')
        gen_page(d, titles)
        
        

def main():
    dirs = list(photos.keys())
    
    gen_pages(dirs)
        
    print('done.')    
            
        

if __name__ == '__main__':
    main()
