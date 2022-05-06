FROM python:3.8-slim-buster
LABEL maintainer="Hetic"

RUN pip install pipenv
COPY Pipfile .
RUN pipenv install

COPY app.py /app.py

COPY data/model.json ./data/

# EXPOSE 5000

CMD ["pipenv", "run", "python", "app.py"]