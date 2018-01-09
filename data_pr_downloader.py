from datetime import datetime
import json
import logging
from mimetypes import guess_extension
import os
import requests
from slugify import slugify

FORMAT = '%(asctime)-15s - %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('data_pr')

BASE_DATA_DIR = 'data_files'
DATA_PR_CATALOG_PATH = f'{BASE_DATA_DIR}/data_pr_catalog_{datetime.now()}.json'
DATA_PR_CATALOG_URL = 'https://data.pr.gov/data.json'

def get_new_data_pr_catalog(url):
    data_pr_json_meta_response = requests.get(url)

    with open(DATA_PR_CATALOG_PATH, 'w') as data_pr_catalog_json:
        json.dump(data_pr_json_meta_response.json(), data_pr_catalog_json)

def get_datasets(data_pr_catalog, amount_to_download=None):
    with open(f'{data_pr_catalog}') as data_catalog:
        data_pr_json_meta = json.load(data_catalog)

    for dataset in data_pr_json_meta['dataset']:
        folder_name = slugify(dataset['title'])
        data_file_path = f'{BASE_DATA_DIR}/{folder_name}'

        logger.info(f"Start download of {dataset['title']} to {data_file_path}")

        if not os.path.exists(data_file_path):
            os.makedirs(data_file_path)

        for distribution in dataset['distribution']:
            file_extension = guess_extension(distribution['mediaType'])
            try:
                response = requests.get(distribution['downloadURL'], stream=True)
            except Exception as e:
                logger.error('Error requesting data: %s', e)
                continue

            logger.debug(f"Downloading distribution: {distribution['mediaType']}")

            with open(f'{data_file_path}/data{file_extension}', 'wb') as dataset_file:
                for data in response.iter_content(chunk_size=100):
                    dataset_file.write(data)

            logger.debug(f"Done downloading distribution: {distribution['mediaType']}")

        logger.info(f"Finished download of {dataset['title']} to {data_file_path}")
def main():
    try:
        get_new_data_pr_catalog(DATA_PR_CATALOG_URL)
    except Exception as e:
        logger.error('Error at get_new_data_pr_catalog: %s', e)
    
    try:
        get_datasets(DATA_PR_CATALOG_PATH)
    except Exception as e:
        logger.error('Error at get_datasets: %s', e)

if __name__ == '__main__':
    logger.setLevel(logging.DEBUG)

    logger.info(f'process started: {datetime.now()}')
    main()
    logger.info(f'process finished: {datetime.now()}')
