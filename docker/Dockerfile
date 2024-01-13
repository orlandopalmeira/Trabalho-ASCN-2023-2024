FROM ubuntu:22.04

# Variável de ambiente para definir se o seed é feito ou não.
ENV seed_db=false 

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y software-properties-common

RUN apt update
RUN add-apt-repository ppa:ondrej/php && apt-get update

RUN apt-get install -y \
    php8.2 \
    php8.2-fpm \
    php8.2-zip \
    php8.2-mbstring \
    php8.2-tokenizer \
    php8.2-mysql \
    php8.2-gd \
    php8.2-xml \
    php8.2-bcmath \
    php8.2-intl \
    php8.2-curl

RUN apt install -y composer npm mysql-client

RUN git clone https://github.com/laravelio/laravel.io.git

WORKDIR /laravel.io

COPY .env .

RUN composer install

RUN php artisan key:generate

EXPOSE 8000

RUN npm install

COPY ./script.sh .

RUN chmod +x ./script.sh

CMD ./script.sh