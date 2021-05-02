# PHP7 Template

Templates are built using the latest minor version of the major release.

| Modules (by default) |
| ------------- |
| Core, date, libxml, openssl, pcre, sqlite3, zlib, ctype, curl, dom, fileinfo, filter, ftp, hash, iconv, json, mbstring, SPL, PDO, pdo_sqlite, session, posix, readline, Reflection, standard, SimpleXML, Phar, tokenizer, xml, xmlreader, xmlwriter, mysqlnd, sodium |

## Usage:

```shell
faas-cli new my-function --lang php7
```

You will find in the newly created directory `my-function`:

- `src/Handler.php` : entrypoint
- `php-extension.sh` : is for installing PHP extensions if needed
- `composer.json` : is for dependency management

## Extra Extensions

If you need to install [Phalcon](https://github.com/phalcon) for example, check out the
following sample which you could use in your functions `src/php-extension.sh` file;

- [php-extension.sh-example](php-extension.sh-example)

You can also refer to the PHP Docker image [documentation](https://github.com/docker-library/docs/blob/master/php/README.md#how-to-install-more-php-extensions) for additional instructions on the installation and configuration of extensions

## Private Composer Auth

In some cases, you may need to use private composer repositories - using the `faas-cli` you can pass in
a build argument during build, for example;

```
faas-cli build -f ./functions.yml \
  --build-arg COMPOSER_AUTH='{"bitbucket-oauth": {"bitbucket.org": {"consumer-key": "xxxxxxxx","consumer-secret": "xxxxxxx"}}}'
```
See more information [here](https://getcomposer.org/doc/05-repositories.md#git-alternatives).

That way you can pass in tokens for Composer, if necessary, GitHub tokens to get around rate-limit issues.
