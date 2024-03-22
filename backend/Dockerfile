FROM python:3.10.14-alpine3.19

COPY . .
WORKDIR .

ENV PIPENV_VERBOSITY=-1

RUN mkdir .venv
RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile

EXPOSE 8000

CMD ["pipenv", "run", "python3", "src/main.py"]
