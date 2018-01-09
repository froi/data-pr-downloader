FROM python:alpine3.6

COPY data_pr_downloader.py Pipfile Pipfile.lock /Code/
WORKDIR /Code/
RUN pip install pipenv &&\
    pipenv install --system

CMD ["python","data_pr_downloader.py"] 
