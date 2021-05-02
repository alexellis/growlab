## Template: java11-vert-x

The Java11-Vert.x template uses gradle as a build system.

Gradle version: 4.8.1

### Structure

There are two projects which make up a single gradle build:

- function - (Library) your function code as a developer, you will only ever see this folder
- entrypoint - (App) Vert.x HTTP server

### Handler

The handler is written in the `./src/main/java/com/openfaas/function/Handler.java` folder

Tests are supported with junit via files in `./src/test`

### External dependencies

External dependencies can be specified in ./build.gradle in the normal way using jcenter, a local JAR or some other remote repository.

### Serve a "pure" static html web application

This template allow you to serve static html assets (eg: single page application)

#### First, update your yaml deployment file:

You only need to add to the `environment` key, a `FRONTAPP` variable (with a value set to `true`)

```yaml
environment:
  FRONTAPP: true
```

#### Then add assets in the webroot directory

Put your static assets in this directory: `/src/main/resources/webroot`

> If `FRONTAPP` is set to `false` (or does not exist), it's the `Handler` instance that serves the data.


#### Deployment yaml file sample:

```yaml
provider:
  name: faas
  gateway: http://openfaas.test:8080
functions:
  hello-vert-x:
    lang: java11-vert-x
    environment:
      FRONTAPP: true
    handler: ./function
    image: registry.test:5000/hello-vert-x:latest
```

