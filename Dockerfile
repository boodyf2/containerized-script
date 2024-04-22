FROM python:latest
WORKDIR /script
COPY random_paragraphs.txt requirments.txt ./
RUN pip install -r requirments.txt
COPY script.py .
CMD python script.py