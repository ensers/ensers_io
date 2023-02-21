
FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN cp xpdf-tools-linux-4.04/bin64/pdftotext /usr/local/bin && cd server/

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
