#!/usr/local/bin/python3.7

from datetime import datetime as dt
import os

from config import PROJECT_PATH, IMAGE_DUMP_PATH, LOG_FILE_PATH
import time_methods as tm


def create_folder_structure():
    """make sure that folders for all quarters are in media folder """

    for quarter in tm.get_all_quarters():
        media_location = os.path.join(PROJECT_PATH, 'site/media/')
        if 'Images_{}'.format(quarter) not in os.listdir(media_location):
            os.system(f'mkdir "{media_location}/Images_{quarter}"')
        if 'thumbnails' not in os.listdir(os.path.join(media_location, f'Images_{quarter}')):
            os.system(f'mkdir "{media_location}/Images_{quarter}/thumbnails"')


def get_correct_filename(filename, media_folder_path):
    name_of_pet = filename
    while name_of_pet[-1].isnumeric() or name_of_pet[-1] == ' ':
        name_of_pet = name_of_pet[:-1]

    number_of_files_with_same_name_in_media_folder = 0
    for filename in os.listdir(media_folder_path):
        if filename.startswith(name_of_pet):
            number_of_files_with_same_name_in_media_folder += 1

    return '{}{}'.format(
        name_of_pet, number_of_files_with_same_name_in_media_folder + 1
    )


def main():
    """copy images from shared Dropbox folder into 'site/media/YYQX/'"""

    print('Kopiere Bilder aus der Dropbox')
    create_folder_structure()  # make sure media folders exist

    media_folder_path = '{}site/media/Images_{}/'.format(
        PROJECT_PATH, tm.get_current_quarter()
    )
    filenames = [
        f for f in os.listdir(IMAGE_DUMP_PATH)
        if f not in ['.DS_Store', 'Icon\r']
    ]

    # create log for dropbox folder content
    if filenames:
        with open(LOG_FILE_PATH, 'r') as fp:
            log = ''.join(fp.readlines())

        log += dt.now().strftime('%Y-%m-%d %H:%M:%S, ')
        log += 'content of dropbox folder:\n'
        for filename in filenames:
            log += f'{filename}\n'
        log += '\n'

        with open(LOG_FILE_PATH, 'w') as fp:
            fp.write(log)

    for filename in filenames:  # ends in '.jpg'
        # if not filename.lower().endswith('.jpg'):
        #     continue

        # change filename if already in media folder
        pet_name = '.'.join(filename.split('.')[:-1])  # does not end in '.jpg'
        new_filename = get_correct_filename(pet_name, media_folder_path)

        os.system(
            'mv "{}{}" "{}{}.jpg"'.format(
                IMAGE_DUMP_PATH, filename, media_folder_path, new_filename
            )
        )


if __name__ == '__main__':
    main()
