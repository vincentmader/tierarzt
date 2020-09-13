#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

from datetime import datetime as dt
from datetime import timedelta as td
import os
from PIL import Image

from config import PROJECT_PATH, NOTDIENST_DATES
from time_methods import get_quarters_that_need_update, get_all_quarters, get_current_quarter


def alphabetize(image):
    image = '.'.join(image.split('.')[:-1])
    while True:
        if image[-1].isnumeric():
            image = image[:-1]
        else:
            break
    return image


def create_gallery_bottom(quarter):
    with open('{}templates/gallery_bottom.txt'.format(PROJECT_PATH)) as fp:
        words = ''.join(fp.readlines()).split(' ')

    html_code = 110 * """
                \t\t<tr>
                    \t\t<td class="zpSO-PictureGallery-ThickBox-td1" style="text-align:center;vertical-align:top"></td>
                \t\t</tr>"""
    for idx, word in enumerate(words):
        if word == '<!--markerSeitenleisteAlt-->':
            html_code += '\n\t\t\t\t'
            for q in reversed(get_all_quarters()):
                if q[:2] != dt.now().strftime('%y'):
                    if q == quarter:
                        html_code += '<a class=\"subnav1active\" href=\"gallery_{}.html\" >'.format(
                            q)
                        html_code += '{}. Quartal 20{}</a>\n\t\t\t\t'.format(
                            q[3:4], q[0:2])
                    else:
                        html_code += '<a class=\"subnav1\" href=\"gallery_{}.html\" >'.format(
                            q)
                        html_code += '{}. Quartal 20{}</a>\n\t\t\t\t'.format(
                            q[3:4], q[0:2])
        elif word == '<!--markerAktualisiert-->':
            html_code += dt.now().strftime('%d.%m.%Y')
        elif word == '<!--markerGalleryYear-->':
            html_code += str(dt.now().year) + ' '
        else:
            html_code += word + ' '
    return html_code


def create_gallery_table(quarter):
    html_code = '\t\t\t\t\t\t<tr>'
    count = 0
    for image in sorted(os.listdir('{}site/media/Images_{}'.format(PROJECT_PATH, quarter))):
        if not image.lower().endswith('.jpg'):
            continue

        image_name = alphabetize(image)
        if count % 6 == 0 and count != 0:
            html_code += "\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t<tr>"
        count += 1

        html_code += '\n\t\t\t\t\t\t\t<td class=\"zpSO-PictureGallery-ThickBox-td1\" '
        html_code += 'style=\"text-align:center;vertical-align:top\">\n\t\t\t\t'
        html_code += '\t\t\t\t<a href=\"media/Images_{}/{}\" title=\"{}'.format(
            quarter, image, image_name)
        html_code += '\" class=\"thickbox\" rel=\"gallery1046\">\n\t\t\t\t\t\t\t\t\t<span style='
        html_code += '\"display:block;margin:0;padding:0;width:100px;height:75px;overflow:hidden;cursor:pointer\">'
        html_code += '\n\t\t\t\t\t\t\t\t\t\t<img src=\"media/Images_{}/thumbnails/'.format(
            quarter)
        html_code += '{}_100.jpg\" border=\"0\" alt=\"\" />'.format(
            '.'.join(image.split('.')[:-1]))
        html_code += '\n\t\t\t\t\t\t\t\t\t</span>\n\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t'
        html_code += '<span class=\"bildunterschrift\">\n\t\t\t\t\t'
        html_code += '\t\t\t\t<span class=\"zpSO-PictureGallery-desc\">{}'.format(
            image_name)
        html_code += '</span>\n\t\t\t\t\t\t\t\t</span>\n\t\t\t\t\t\t\t</td>\n'

    html_code += '\t\t\t\t\t\t</tr>'
    return html_code


def create_gallery_top(quarter):
    with open(os.path.join(PROJECT_PATH, 'templates/gallery_top.txt')) as fp:
        words = ''.join(fp.readlines()).split(' ')

    html_code = ''
    for idx, word in enumerate(words):
        if word == '<!--markerGalleryTitle-->':
            html_code += 'Bilder der Patienten {}. Quartal 20{}'.format(
                quarter[3:4], quarter[0:2]
            )
        elif word == '<!--markerGalleryKeywords-->':
            html_code += 'Galerie {} Quartal {}'.format(
                dt.now().year, get_current_quarter()[3:4]
            )
        elif word == '<!--markerGalleryYear-->':
            html_code += '{} '.format(dt.now().year)
        elif word == '<!--markerMenuGalleryLink-->':
            html_code += '<div class=\"menu-separator\"></div>'
            html_code += '<a class=\"topmenuactive\"'
            html_code += 'href=\"gallery_{}.html\">Bilder</a>\n'.format(
                get_current_quarter()
            )
        elif word == '<!--markerSeitenleisteNeu-->':
            for i in range(1, int(get_current_quarter()[3:4]) + 1):
                html_code += "\n\t\t\t\t"
                if '{}Q{}'.format(dt.now().strftime('%y'), i) == quarter:
                    html_code += '<a class=\"subnav1active\" href=\"gallery_'
                    html_code += '{}Q{}'.format(dt.now().strftime('%y'), i)
                    html_code += '.html\">{}. Quartal {}</a>'.format(
                        i, dt.now().year
                    )
                else:
                    html_code += '<a class=\"subnav1\" href=\"'
                    html_code += 'gallery_{}Q{}'.format(
                        dt.now().strftime('%y'), i
                    )
                    html_code += '.html\">{}. Quartal {}</a>'.format(
                        i, dt.now().year
                    )
        else:
            html_code += word + ' '
    return html_code


def create_thumbnails(quarter):
    """create thumbnails for all images inside a given quarter folder"""

    for image_file in os.listdir(
        '{}/site/media/Images_{}'.format(PROJECT_PATH, quarter)
    ):
        if image_file.lower().endswith('.jpg'):
            image_name = '.'.join(image_file.split('.')[:-1])

            img = Image.open('{}/site/media/Images_{}/{}'.format(
                PROJECT_PATH, quarter, image_file)
            )
            img.thumbnail((100, 100), Image.ANTIALIAS)
            img_save_path = os.path.join(
                PROJECT_PATH,
                'site/media/Images_{}/thumbnails/{}_100.jpg'.format(
                    quarter, image_name
                )
            )
            img.save(img_save_path)


def currently_notdienst():
    for date_range in NOTDIENST_DATES:
        start_date = date_range[0]
        end_date = date_range[1]

        if start_date <= dt.now() <= end_date + td(days=1):
            return True

    return False


def main():
    """create html files from templates"""

    print('Erzeuge HTML-Dateien')

    update_galleries()
    update_index()
    update_links()


def update_galleries():
    """create HTML file for each quarter's picture gallery"""

    print('  Erzeuge Galerien')
    for quarter in get_quarters_that_need_update():
        print('    Quartal {}'.format(quarter))
        create_thumbnails(quarter)

        gallery = create_gallery_top(quarter)
        gallery += create_gallery_table(quarter)
        gallery += create_gallery_bottom(quarter)
        with open(
            os.path.join(PROJECT_PATH, f'site/gallery_{quarter}.html'), 'w'
        ) as fp:
            fp.write(gallery)


def update_index():
    """update Notdienst text and links"""

    print('  Aktualisiere Index')
    with open('{}templates/index.txt'.format(PROJECT_PATH)) as fp:
        words = ''.join(fp.readlines()).split(' ')

    html_code = ''
    for word in words:
        if word == '<!--markerMenuGalleryLink-->':
            html_code += '<div class=\"menu-separator\"></div><a class="topmenu"'
            html_code += 'href=\"gallery_{}.html\">Bilder</a>\n'.format(
                get_current_quarter())
        elif word == '<!--markerNotdienst-->':
            if currently_notdienst():
                html_code += """
                <p style="color: red; font-weight:bold">
                    Liebe PatientenbesitzerInnen,<br>
                    die Praxis ist zur Zeit die notdiensthabende Praxis für Ulm und Neu-Ulm.<br>
                    In dringenden Fällen erreichen Sie mich unter der Nummer: 0177/ 20 65 066.<br>
                    <br>
                    Bitte beachten Sie, dass im Notdienst eine Notdienstgebühr fällig ist<br>
                    und die Rechnung sofort bar beglichen werden muss.<br>
                </p>"""
            else:
                pass
        elif word == '<!--markerGalleryYear-->':
            html_code += str(dt.now().year) + ' '
        elif word == '<!--markerAktualisiert-->':
            html_code += dt.now().strftime('%d.%m.%Y')
        else:
            html_code += word + ' '

    with open('{}site/index.html'.format(PROJECT_PATH), 'w') as fp:
        fp.write(html_code)


def update_links():
    """make sure menu links are complete and correct"""

    print('  Verknüpfe Galerien')
    for file in os.listdir('{}templates'.format(PROJECT_PATH)):
        if file in ['gallery_bottom.txt', 'gallery_top.txt', 'index.txt']:
            continue
        with open('{}templates/{}'.format(PROJECT_PATH, file)) as fp:
            words = ''.join(fp.readlines()).split(' ')

        html_code = ''
        for word in words:
            if word == '<!--markerMenuGalleryLink-->':
                html_code += '<div class=\"menu-separator\"></div>'
                html_code += '<a class=\"topmenu\"'
                html_code += 'href=\"gallery_{}.html\">Bilder</a>\n'.format(
                    get_current_quarter()
                )
            elif word == '<!--markerGalleryYear-->':
                html_code += str(dt.now().year) + ' '
            elif word == '<!--markerAktualisiert-->':
                html_code += dt.now().strftime('%d.%m.%Y')
            else:
                html_code += word + ' '

        html_file_name = file.split('.')[0] + '.html'
        with open('{}site/{}'.format(PROJECT_PATH, html_file_name), 'w') as fp:
            fp.write(html_code)


if __name__ == '__main__':
    main()
