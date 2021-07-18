FROM python:3.9.5

RUN pip3 install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
COPY api/ api
COPY app.py app.py

RUN pipenv install --system --deploy --ignore-pipfile

CMD flask run -h 0.0.0.0 -p 5000
