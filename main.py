from datetime import datetime as dt
import json

import collect_images
import update_html_files
import upload_files
from config import PROJECT_PATH


START_TIME = dt.now()

if __name__ == '__main__':

    print('\n\n\nTIERARZT v3.0')
    print('-' * 79)
    print('Gespeichert unter')
    print(f'  {PROJECT_PATH}')
    print('-' * 79 + '\n')

    collect_images.main()
    update_html_files.main()
    upload_files.main()

    END_TIME = dt.now()
    run_time_minutes = str((END_TIME - START_TIME).seconds / 60).split('.')[0]
    run_time_seconds = (END_TIME - START_TIME).seconds % 60

    print('\n' + '-' * 79)
    print('Laufzeit: {} Minuten {} Sekunden\n'.format(
        run_time_minutes, run_time_seconds)
    )

    with open('{}/last_update.json'.format(PROJECT_PATH), 'w') as fp:
        json.dump([dt.now().strftime('%Y-%m-%d')], fp)

    with open(f'{PROJECT_PATH}/log.txt') as fp:
        content = fp.readlines()
        content.append(dt.now().strftime('%Y-%m-%d %H:%M:%S') + ' script executed successfully' )
    with open(f'{PROJECT_PATH}/log.txt', 'w') as fp:
        fp.write(''.join(content))
