FROM python:3.12.3 as requirements-stage

#
WORKDIR /tmp

#
RUN pip install poetry

#
COPY ./pyproject.toml ./poetry.lock* /tmp/

#
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

#
FROM python:3.12.3

#
WORKDIR /code

#
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt


#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY . /code/app

COPY certs/.env ./.env

RUN . ./.env && \
    export DB_HOST=$DB_HOST && \
    export DB_PORT=$DB_PORT && \
    export DB_NAME=$DB_NAME && \
    export DB_USER=$DB_USER && \
    export DB_PASSWORD=$DB_PASSWORD

ENV DB_HOST=$DB_HOST
ENV DB_PORT=$DB_PORT
ENV DB_NAME=$DB_NAME
ENV DB_USER=$DB_USER
ENV DB_PASSWORD=$DB_PASSWORD
#
CMD ["python", "app/main.py"]