FROM python:3.7-buster
WORKDIR /servier
COPY . .

ENV INPUT_PATH ./input_string.txt

RUN pip install -r requirements.txt

EXPOSE 8791

ENTRYPOINT ["python", "main.py"]
