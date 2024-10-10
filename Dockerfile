###########
# BUILDER #
###########

# pull official base image
FROM python:3.11-bookworm AS builder

# set work directory
WORKDIR /home/build

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


RUN pip install --upgrade pip poetry poetry-plugin-export

COPY pyproject.toml .
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

#########
# FINAL #
#########

# django-macaddress does not support 3.12 or higher
FROM python:3.11-bookworm


WORKDIR /home/app

# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends netcat-traditional
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /home/build/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy project
COPY . .

EXPOSE 8000

# Start gunicorn
RUN chmod +x launcher.sh
CMD ["./launcher.sh"]