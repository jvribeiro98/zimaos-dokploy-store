# NodeLink

This template deploys NodeLink, a Lavalink-compatible audio server for Discord music bots and real-time audio systems.

## Connection

Use the deployed domain as your NodeLink/Lavalink server URL:

- Host: `https://localhost`
- Port: `443` when connecting through the Dokploy domain
- Password: the generated `server_password` value

NodeLink exposes the `/version`, `/v4/stats`, and Lavalink-compatible WebSocket/API endpoints through the same domain.

## Local Music

The template creates a persistent `nodelink-local-music` volume mounted at `/app/local-music`. Set `local_source_enabled` to `true` before deployment if you want NodeLink to resolve `file:///app/local-music/...` tracks.

## Metrics

Set `metrics_enabled` to `true` to expose Prometheus metrics at `/v4/metrics`. Keep this disabled unless your deployment is protected and monitored.
