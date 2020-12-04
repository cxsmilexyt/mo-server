FROM python:3.8-alpine

WORKDIR /usr/src/app

COPY . .

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk update \
    && apk add --no-cache gcc linux-headers musl-dev \
    && pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple

CMD [ "python", "./mo-server.py" ]
