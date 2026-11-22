# Brightbean Studio (Dokploy template)

Open-source social media management: schedule, publish and manage content
across 10+ platforms from one dashboard (Buffer/Sendible alternative).

## After deploying

1. **Admin** — create your superuser once the stack is up:
   `docker exec -it <app-container> python manage.py createsuperuser`
   (or open https://<your-domain>/admin/ and use a first-login flow if enabled).
2. **Platform credentials** (Facebook, Instagram, LinkedIn, TikTok, YouTube,
   Pinterest, Threads, Bluesky, Google Business, Mastodon, DEV.to): add them in
   Django admin under *Platform credentials*, or set the `PLATFORM_*` env vars
   on this compose service in Dokploy and redeploy.
3. **Media storage** — default is local disk on the `media_data` volume
   (served by Django via SERVE_MEDIA=true at /media/). To move to S3, set
   `STORAGE_BACKEND=s3` plus `S3_*` vars and set `SERVE_MEDIA=false`.
4. **Email** — set `EMAIL_HOST` / `EMAIL_HOST_USER` / `EMAIL_HOST_PASSWORD` /
   `DEFAULT_FROM_EMAIL` if you want password resets and notifications.
5. **Google login** — set `GOOGLE_AUTH_CLIENT_ID` / `GOOGLE_AUTH_CLIENT_SECRET`
   for Google sign-in.

## Notes

- The image is built from source on every deploy (takes a few minutes the
  first time). The three services share the same Dockerfile, so only the
  first build pays the full cost.
- `migrate` is a one-shot service: it runs Django migrations, then exits.
  `app` and `worker` wait for it via `service_completed_successfully`.
- Traefik (Dokploy) handles TLS; the upstream Caddy edge is not used.
