FROM python:3.7.9

ADD requirements.txt /app/requirements.txt

# RUN set -ex \
#     && apk add --no-cache --virtual .build-deps postgresql-dev build-base \
#     && python -m venv /env \
#     && /env/bin/pip install --upgrade pip \
#     && /env/bin/pip install --no-cache-dir -r /app/requirements.txt \
#     && runDeps="$(scanelf --needed --nobanner --recursive /env \
#         | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
#         | sort -u \
#         | xargs -r apk info --installed \
#         | sort -u)" \
#     && apk add --virtual rundeps $runDeps \
#     && apk del .build-deps

ADD . /app
WORKDIR /app

# ENV VIRTUAL_ENV /env
# ENV PATH /env/bin:$PATH
RUN python -m pip install -r requirements.txt

EXPOSE 8000

# CMD ["gunicorn", "--bind", ":80", "--workers", "3", "momken.wsgi"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]