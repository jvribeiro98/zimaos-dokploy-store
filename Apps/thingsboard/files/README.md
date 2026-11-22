# ThingsBoard

This template deploys ThingsBoard Community Edition with PostgreSQL using the official `thingsboard/tb-node` Docker image.

## First start

The `thingsboard-init` service initializes the database once before the main service starts. By default it performs a clean install. Set `load_demo` to `true` before deploying if you want ThingsBoard's sample tenant, dashboards, and demo devices.

## Login

Open `https://localhost` and sign in with the default system administrator account:

- Email: `sysadmin@thingsboard.org`
- Password: `sysadmin`

Change the default password before exposing the instance to production users.

## Device connectivity

The web UI and HTTP device API are available through the configured domain. MQTT, CoAP, and additional transport ports are not publicly exposed by this template; expose them separately in Dokploy if your deployment requires direct device connections over those protocols.
