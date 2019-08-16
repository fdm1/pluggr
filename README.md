Pluggr
------

A plug-and-play web application to learn about different technologies at all
levels of a standard web application stack, as well as trying to be able to
swap in substitutions at any level.

## Potential swappable components
- Cloud provider: can be AWS or GCP (using Terraform for either)
- Backing database: Postgres, MySql, Mongo?, Terraform?, Random text files on S3???
- An application layer: Flask, Rails, something in Go or Rust?
- A fronting proxy: Nginx, whatever nginx's competion is?
- Memcache: Redis, non-redis?
- Containerization: Docker
- Orchestration: K8s

Once the first iteration of this is done, maybe I'll get even crazier and add
some pubsub stuff on top.

## Requirements
- Everything needs to be able to be spun up and down at will, as for the time
being, none of this will be running long-lived.
- Try to follow best-practices at all times (TDD, etc), as this is a learning
project.
- Don't spend all my money.
