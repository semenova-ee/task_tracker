FROM python:3

WORKDIR /katya_dip

COPY reqs.txt .

RUN pip install --no-cache-dir -r reqs.txt

COPY . .
