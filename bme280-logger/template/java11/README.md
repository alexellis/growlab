## Template: java11

The Java11 template uses gradle as a build system.

Gradle version: 5.5.1

### Structure

There are three projects which make up a single gradle build:

- model - (Library) classes for parsing request/response
- function - (Library) your function code as a developer, you will only ever see this folder
- entrypoint - (App) HTTP server for re-using the JVM between requests

### Handler

The handler is written in the `./src/main/Handler.java` folder

Tests are supported with junit via files in `./src/test`

### External dependencies

External dependencies can be specified in ./build.gradle in the normal way using jcenter, a local JAR or some other remote repository.

