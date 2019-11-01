Pluggr
------

A plug-and-play web application to learn about different technologies at all
levels of a standard web application stack, as well as trying to be able to
swap in substitutions at any level.

## Potential swappable components
- Cloud provider: can be AWS or GCP (using Terraform for either)
- Backing database: Postgres, MySql, Mongo?, Teradata?? (but let's not), random text files on S3???
- An application layer: Flask, Rails, something in Go or Rust?
- A fronting proxy: Nginx, whatever nginx's competion is?
- Memcache: Redis, non-redis?
- Containerization: Docker, are there alternatives?
- Orchestration: Kubernetes, something else?

Once the first iteration of this is done, maybe I'll get even crazier and add
some pubsub stuff on top.

## Requirements
- Everything needs to be able to be spun up and down at will, as for the time
being, none of this will be running long-lived.
- Try to follow best-practices at all times (TDD, etc), as this is a learning
project.
- Try to have a unified build/test entrypoint. Maybe `make`?
- Don't spend all my money.


## Structure

```
- application/   # all web applications live in her
  - <language>/     # grouped by language
    - <framework>/    # by framework
      - <application_name>/   # by name (if an application is created in more than one language/framework, it should use the same name)
- terraform/    # all terraform code lives here

```


### Applications:
- `dummy`:
  - receives `Post` with a string, stores that string in the database
  - receives `Get` with a string, gets and prints that string in the response


### Container tagging convention:
- fdm1-plugger:<layer>-<language>-<framework>-<name>-<gitsho> (where applicable for each attribute)
  - example tag for flask dummy app: fdm1-plugger:application-python-flask-dummy-123abcd
