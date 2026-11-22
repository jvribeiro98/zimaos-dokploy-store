# OpenSourcePOS

This template deploys Open Source Point of Sale with MariaDB using the upstream Docker image and persistent storage for uploads, logs, and database data.

## Access

- URL: `http://localhost`
- Default application user: `admin`
- Default application password: `pointofsale`

Change the default application password immediately after the first login.

## Hostnames and HTTPS

OpenSourcePOS validates incoming host headers in production. The `allowed_hostnames` variable defaults to `localhost` and can be set to a comma-separated list such as `pos.example.com,www.pos.example.com`.

The template defaults `force_https` to `false` because Dokploy terminates TLS outside the container. Set it to `true` only when your deployment always reaches OpenSourcePOS through HTTPS and the reverse proxy sends the expected headers.

## Storage

The template creates persistent volumes for:

- MariaDB data
- uploaded files
- application logs
