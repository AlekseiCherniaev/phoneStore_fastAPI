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

#
CMD ["python", "app/main.py"]