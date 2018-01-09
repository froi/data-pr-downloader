FROM python:alpine3.6

RUN pip install requests python-slugify pytest
RUN mkdir -p /Code/data_files
COPY data_pr_downloader.py /Code
WORKDIR /Code/

CMD ["python","data_pr_downloader.py"] 

