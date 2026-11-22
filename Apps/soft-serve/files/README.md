# Soft Serve

This template deploys Soft Serve, a self-hosted Git server with an SSH TUI, HTTP Git access, Git LFS support, and a lightweight web endpoint.

## First Start

Set `initial_admin_keys` to one or more SSH public keys before the first deployment. Soft Serve uses this value to create the initial `admin` user. The keys are consumed during initialization, so changing this variable later does not rewrite an already initialized data volume.

Example value:

```text
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA... your-name
```

## HTTP Access

The Dokploy domain routes to Soft Serve's HTTP listener:

- HTTP public URL: `http://localhost`
- HTTP Git clone example: `git clone http://localhost/repo.git`

Set `http_public_url` to `https://localhost` before deploying if your Dokploy domain enforces TLS.

Private HTTP access uses tokens created through the SSH admin interface.

## SSH and Git Protocol Ports

Soft Serve also listens inside the deployment on:

- SSH/TUI: `23231`
- Stats: `23233`
- Git protocol: `9418`

This template does not publish host TCP ports directly. Expose the SSH or Git protocol ports separately in Dokploy if you need direct terminal/TUI access, then use the configured `ssh_public_url` for clone commands.

## Storage

Repositories, configuration, keys, and the default SQLite database are stored in the persistent `soft-serve-data` volume mounted at `/soft-serve`.
