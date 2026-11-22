# ownCloud Infinite Scale

This template deploys ownCloud Infinite Scale (oCIS), a modern file sync and share platform with WebDAV and ownCloud client support.

## Access

- URL: `https://localhost`
- Admin user: `admin`
- Admin password: the generated `admin_password` value

The `owncloud_url` value must use `https://` because oCIS only supports HTTPS public URLs (its built-in identity provider rejects plain HTTP issuers). A bundled nginx gateway sits in front of oCIS and forwards requests with `X-Forwarded-Proto: https`, which keeps oCIS from redirecting every request when it runs behind the Dokploy proxy. Enable HTTPS on the Dokploy domain so the public URL matches `OCIS_URL`.

## Storage

The template creates persistent volumes for:

- `/etc/ocis` configuration
- `/var/lib/ocis` application data and user storage
- `/var/lib/ocis-thumbnails` generated thumbnails

Back up these volumes together before upgrades or migrations.
