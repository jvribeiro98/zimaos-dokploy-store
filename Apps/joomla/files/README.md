# Joomla

This template deploys Joomla CMS with MariaDB using the official Joomla Apache image.

## Access

- URL: `http://localhost`
- Administrator username: the configured `admin_username` value
- Administrator password: the generated `admin_password` value
- Administrator email: the configured `admin_email` value

The template uses Joomla's auto-deployment environment variables so the site and administrator account are initialized on first start.

## Storage

The template creates persistent volumes for:

- Joomla application files at `/var/www/html`
- MariaDB data at `/var/lib/mysql`

Back up both volumes together before upgrades or migrations.
