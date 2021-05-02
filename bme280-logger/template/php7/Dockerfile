ARG TARGETPLATFORM
ARG BUILDPLATFORM

FROM --platform=${TARGETPLATFORM:-linux/amd64} ghcr.io/openfaas/classic-watchdog:0.1.5 as watchdog

# start with the official Composer image and name it
FROM --platform=${TARGETPLATFORM:-linux/amd64} composer:1.7 AS composer

# continue with the official PHP image
FROM --platform=${TARGETPLATFORM:-linux/amd64} php:7.2-alpine

# copy the Composer PHAR from the Composer image into the PHP image
COPY --from=composer /usr/bin/composer /usr/bin/composer

# Composer requirements
ARG COMPOSER_AUTH='{}'
ENV COMPOSER_AUTH=${COMPOSER_AUTH}

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog

RUN apk add --no-cache git

# create non-root user
RUN addgroup -S app && adduser -S -g app app && \
    mkdir -p /home/app

# Import function
WORKDIR /home/app
COPY index.php ./
COPY ./function ./function
WORKDIR /home/app/function

# Install php extensions
RUN [[ -f php-extension.sh ]] && sh ./php-extension.sh && \
    chown -R app /home/app

# Entry
USER app

# Install Composer Dependecies
RUN [[ -f composer.lock || -f composer.json ]] && composer install --no-dev

USER root

# Cleanup
RUN apk del git && \
    rm -rf /usr/src/php && \
    { find /usr/local/lib -type f -print0 | xargs -0r strip --strip-all -p 2>/dev/null || true; }

USER app

WORKDIR /home/app
ENV fprocess="php index.php"
HEALTHCHECK --interval=3s CMD [ -e /tmp/.lock ] || exit 1
CMD ["fwatchdog"]
