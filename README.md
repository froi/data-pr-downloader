# data-pr-downloader
Dump of all datasets found in the dataset catalog @ https://data.pr.gov to disk. There are 148 datasets at the moment of the initial commit 2017-07-25. Please remember your disk space!

PRs are welcome!

# What does it do?

All created files are saved to the `data_files` directory using the following steps:

1. Fetches the catalog of datasets from https://data.pr.gov/data.json
2. Saves the dataset catalog to disk with a timestamp.
3. Consumes dataset catalog and downloads all distributions for each dataset.
    * All downloaded files will be named `data.{file_type}`

# Running the script

1. Install [pipenv](https://github.com/kennethreitz/pipenv) 'cause we fancy.
2. Initialize a Python 3 virtual environment `pipenv --three`
3. Install dependencies `pipenv install`
4. Activate the virtual environment `pipenv shell`
5. Execute `python data_pr_downloader.py`