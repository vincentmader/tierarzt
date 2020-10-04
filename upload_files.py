#!/usr/local/bin/python3.7

from datetime import datetime as dt
import ftplib
import json
import os

from config import PROJECT_PATH
import time_methods as tm


def create_folder_structure(ftp):
    print('  Erzeuge Ordner-Strukturen')

    # get listing of all folders in media directory
    ftp.cwd('/media/')
    image_folders = []
    ftp.dir(image_folders.append)
    image_folders = [i.split(' ')[-1] for i in image_folders]

    for quarter in tm.get_all_quarters():
        if 'Images_{}'.format(quarter) not in image_folders:
            ftp.mkd('Images_{}'.format(quarter))
            ftp.cwd('Images_{}'.format(quarter))
            ftp.mkd('thumbnails')


def get_ftp_creds():
    path_to_creds = os.path.join(PROJECT_PATH, 'ftp_creds.json')
    with open(path_to_creds) as fp:
        content = json.load(fp)
        server = content['server']
        user = content['user']
        passwd = content['passwd']

    return server, user, passwd


def main():
    """connect to server using FTP, upload files"""

    print('Verbinde mit Server')
    server, user, passwd = get_ftp_creds()
    ftp = ftplib.FTP(server)
    ftp.encoding = 'utf-8'
    ftp.login(user=user, passwd=passwd)
    print('Upload zum Server')

    with open('{}last_update.json'.format(PROJECT_PATH)) as fp:
        last_update = json.load(fp)[0]
        quarter_of_last_update = tm.get_quarter_from_date(last_update)

    # case 1:
        # site has been updated during this quarter already
        # -> upload index + new images
    if quarter_of_last_update == tm.get_current_quarter():
        # create folder structure for image upload
        create_folder_structure(ftp)
        print('  Lade Bilder hoch')
        # upload new images
        upload_new_images(ftp, tm.get_current_quarter())
        print('  Lade HTML-Dateien hoch')
        # upload index
        upload_index(ftp)
        # upload gallery for current quarter
        upload_gallery(ftp, tm.get_current_quarter())

    # case 2:
        # site has not yet been updated
        # -> upload all html files + new images
    else:
        # create folder structure for image upload
        create_folder_structure(ftp)
        print('  Lade Bilder hoch')
        # upload new images
        for quarter in tm.get_all_quarters(start=quarter_of_last_update):
            upload_new_images(ftp, quarter)
        print('  Lade HTML-Dateien hoch')
        # upload all html files (so that links are correct)
        upload_all_html_files(ftp)

    ftp.quit()


def upload_all_html_files(ftp):
    ftp.cwd('/')
    for file in sorted(os.listdir('{}site'.format(PROJECT_PATH))):
        if not file.lower().endswith('.html'):
            continue

        print('    {}'.format(file))
        # upload file
        with open('{}site/{}'.format(PROJECT_PATH, file), 'rb') as fp:
            ftp.storbinary('STOR {}'.format(file), fp)


def upload_gallery(ftp, quarter):
    print('    gallery_{}.html'.format(quarter))

    ftp.cwd('/')
    gallery = 'gallery_{}.html'.format(quarter)
    with open('{}site/{}'.format(PROJECT_PATH, gallery), 'rb') as fp:
        ftp.storbinary('STOR {}'.format(gallery), fp)


def upload_index(ftp):
    print('    index.html')

    ftp.cwd('/')
    with open('{}site/index.html'.format(PROJECT_PATH), 'rb') as fp:
        ftp.storbinary('STOR index.html', fp)


def upload_new_images(ftp, quarter):
    print('    Quartal {}'.format(quarter))

    # get listing of all images in 'media/Images_YYQX/'
    ftp.cwd('/media/Images_{}'.format(quarter))
    images = []
    ftp.dir(images.append)

    images = [' '.join(i.split(' ')[11:])
              for i in images if i.lower().endswith('.jpg')]
    path_to_images = f'{PROJECT_PATH}site/media/Images_{quarter}'
    for image in sorted(os.listdir(path_to_images)):
        if not image.lower().endswith('.jpg'):
            continue

        # upload image if not already on server
        image_already_on_server = False
        for file_info in images:
            if file_info.endswith(image):
                image_already_on_server = True
        if image_already_on_server:
            # switch the commentation on the two lines below to toggle
            # reupload of all images in the currently processed quarter(s)
            continue
            # pass

        print('      {}'.format(image))

        ftp.cwd('/media/Images_{}'.format(quarter))
        path_to_file = f'{PROJECT_PATH}site/media/Images_{quarter}/{image}'
        with open(path_to_file, 'rb') as fp:
            ftp.storbinary('STOR {}'.format(image), fp)

        # also upload thumbnail
        ftp.cwd('/media/Images_{}/thumbnails'.format(quarter))
        thumbnail_filename = '.'.join(image.split('.')[:-1]) + '_100.jpg'
        path_to_file = '{}site/media/Images_{}/thumbnails/{}'.format(
            PROJECT_PATH, quarter, thumbnail_filename
        )
        with open(path_to_file, 'rb') as fp:
            ftp.storbinary('STOR {}'.format(thumbnail_filename), fp)


if __name__ == '__main__':
    main()
