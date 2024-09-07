FROM python:3.13.0rc1

COPY . /app

WORKDIR /app

RUN pip install pipenv

RUN pipenv install --system --dev

CMD ["/bin/sh", "-c", "chmod 777 /app/entrypoint.sh && /app/entrypoint.sh"]
