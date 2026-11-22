# 🏪 Dokploy Templates para ZimaOS & CasaOS

Catálogo com **629 aplicações auto-hospedadas (self-hosted)** convertidas automaticamente do [Dokploy/templates](https://github.com/Dokploy/templates) para o formato nativo da Loja de Aplicativos do **ZimaOS** e **CasaOS** (suporte aos protocolos v2 e v1 ZIP).

---

## 📊 Estatísticas
- **Total de Apps:** `629`
- **Categorias:** `Productivity: 158` `Networking: 102` `Others: 99` `Developer: 98` `AI: 60` `Media: 51` `Finance: 25` `Social: 22` `Home: 14`
- **Sincronização:** Atualizado diariamente via GitHub Actions direto do Dokploy Canary.

---

## 🚀 Como Adicionar ao ZimaOS / CasaOS

### Método 1: URL de Repositório (Recomendado - Protocolo v1 / v2)
1. No seu **ZimaOS** ou **CasaOS**, abra a **App Store** (Loja de Apps).
2. Clique no ícone de engrenagem ⚙️ ou no botão **+ Adicionar Fonte** (**+ Add Source**).
3. Cole a seguinte URL:
   ```text
   https://github.com/jvribeiro98/zimaos-dokploy-store/archive/refs/heads/main.zip
   ```
   *Ou a URL direta do manifesto:*
   ```text
   https://raw.githubusercontent.com/jvribeiro98/zimaos-dokploy-store/main/store.json
   ```
4. Clique em **Adicionar** / **Confirmar**.
5. Aguarde alguns segundos até o ZimaOS sincronizar todos os 629 aplicativos no seu catálogo!

---

## 🛠️ Manutenção e Sincronização Automática
Este repositório possui uma GitHub Action (`.github/workflows/sync-dokploy.yml`) que roda todos os dias às 06:00 UTC, buscando novos templates e atualizações do repositório oficial do Dokploy e gerando os novos Compose files.

---

## 📦 Lista Completa de Aplicativos (629)

### 📁 Media (51 apps)

| App | Pasta | Descrição | Compose |
| :--- | :--- | :--- | :--- |
| **AllTube** | `alltube` | AllTube Download is an application designed to facilitate the downloading of videos fro... | [Compose](Apps/alltube/docker-compose.yml) |
| **Ampache** | `ampache` | Ampache is a web-based audio/video streaming application and file manager allowing you... | [Compose](Apps/ampache/docker-compose.yml) |
| **Audiobookshelf** | `audiobookshelf` | Audiobookshelf is a self-hosted server designed to manage and play your audiobooks and... | [Compose](Apps/audiobookshelf/docker-compose.yml) |
| **AzuraCast** | `azuracast` | AzuraCast is a self-hosted, all-in-one web radio management suite | [Compose](Apps/azuracast/docker-compose.yml) |
| **Booklore** | `booklore` | Booklore is an application for managing and serving book-related data, backed by a Mari... | [Compose](Apps/booklore/docker-compose.yml) |
| **BookOrbit** | `bookorbit` | BookOrbit is a self-hosted reading space to organize, track, and read your personal boo... | [Compose](Apps/bookorbit/docker-compose.yml) |
| **Brightbean Studio** | `brightbean-studio` | Open-source, self-hostable social media management platform: schedule, publish and mana... | [Compose](Apps/brightbean-studio/docker-compose.yml) |
| **Calibre-Web** | `calibre-web` | Calibre-Web is a web interface for browsing, reading, and downloading ebooks from a Cal... | [Compose](Apps/calibre-web/docker-compose.yml) |
| **Chibisafe** | `chibisafe` | A beautiful and performant vault to save all your files in the cloud | [Compose](Apps/chibisafe/docker-compose.yml) |
| **ConvertX** | `convertx` | ConvertX is a service for converting media files, with optional user registration and f... | [Compose](Apps/convertx/docker-compose.yml) |
| **Emby** | `emby` | Emby Server is a personal media server with apps on just about every device | [Compose](Apps/emby/docker-compose.yml) |
| **Frameleaf** | `frameleaf` | Frameleaf is a self-hosted photo and video library with native apps, private face and s... | [Compose](Apps/frameleaf/docker-compose.yml) |
| **FreeFrame** | `freeframe` | FreeFrame is an open-source, self-hostable alternative to Frame | [Compose](Apps/freeframe/docker-compose.yml) |
| **go2rtc** | `go2rtc` | Ultimate camera streaming application with support for dozens formats and protocols | [Compose](Apps/go2rtc/docker-compose.yml) |
| **imgproxy** | `imgproxy` | imgproxy is a fast and secure image processing server, fronted by nginx with built-in r... | [Compose](Apps/imgproxy/docker-compose.yml) |
| **Immich** | `immich` | Immich is a photo and video backup app and an alternative to Google Photos | [Compose](Apps/immich/docker-compose.yml) |
| **jellyfin** | `jellyfin` | Jellyfin is a Free Software Media System that puts you in control of managing and strea... | [Compose](Apps/jellyfin/docker-compose.yml) |
| **Jellyseerr** | `jellyseerr` | Jellyseerr is a media request manager for Jellyfin, Emby, and Plex | [Compose](Apps/jellyseerr/docker-compose.yml) |
| **Jitsi Meet** | `jitsi` | Jitsi Meet is an open-source video conferencing platform for secure, self-hosted meetings | [Compose](Apps/jitsi/docker-compose.yml) |
| **Kavita** | `kavita` | Kavita is a digital library server for comics, manga, and ebooks | [Compose](Apps/kavita/docker-compose.yml) |
| **Legejo** | `legejo` | Legejo is a self-hosted library for your EPUB books, with a web reader, Kobo sync, OPDS... | [Compose](Apps/legejo/docker-compose.yml) |
| **Livekit** | `livekit` | LiveKit is an open source platform for developers building realtime media applications | [Compose](Apps/livekit/docker-compose.yml) |
| **MAZANOKE** | `mazanoke` | MAZANOKE is a modern, self-hosted image hosting and sharing platform | [Compose](Apps/mazanoke/docker-compose.yml) |
| **MediaCMS** | `mediacms` | MediaCMS is an open-source video and media CMS | [Compose](Apps/mediacms/docker-compose.yml) |
| **MediaFetch** | `mediafetch` | A tiny, self-hosted web wrapper for yt-dlp to download video and audio | [Compose](Apps/mediafetch/docker-compose.yml) |
| **MeTube** | `metube` | MeTube is a web-based YouTube downloader that allows downloading videos and audio using... | [Compose](Apps/metube/docker-compose.yml) |
| **Misaka Danmu Server** | `misaka-danmu-server` | A self-hosted danmaku (bullet comments) server for live streaming and video platforms | [Compose](Apps/misaka-danmu-server/docker-compose.yml) |
| **Mixpost** | `mixpost` | Mixpost is an open-source social media management tool that allows you to create, sched... | [Compose](Apps/mixpost/docker-compose.yml) |
| **Movary** | `movary` | Movary is a self-hosted platform for tracking and managing your watched movies using TMDB | [Compose](Apps/movary/docker-compose.yml) |
| **Navidrome** | `navidrome` | Navidrome is a modern music server and streamer compatible with Subsonic/Airsonic | [Compose](Apps/navidrome/docker-compose.yml) |
| **NaviMusic** | `navi-music` | A Discord music bot that plays YouTube and Spotify tracks and playlists in voice channels | [Compose](Apps/navi-music/docker-compose.yml) |
| **NodeLink** | `nodelink` | NodeLink is a lightweight Lavalink-compatible audio server built in Node | [Compose](Apps/nodelink/docker-compose.yml) |
| **Openinary** | `openinary` | Openinary is a self-hosted Cloudinary alternative | [Compose](Apps/openinary/docker-compose.yml) |
| **Oryx** | `oryx` | Oryx (formerly SRS Stack) is an all-in-one, open-source video streaming server with a w... | [Compose](Apps/oryx/docker-compose.yml) |
| **Owncast** | `owncast` | Owncast is a self-hosted live video streaming and chat server for use with existing bro... | [Compose](Apps/owncast/docker-compose.yml) |
| **Photoprism** | `photoprism` | PhotoPrism is an AI-powered app for browsing, organizing, and sharing your photo library | [Compose](Apps/photoprism/docker-compose.yml) |
| **Picsur** | `picsur` | Picsur is a simple, self-hosted image hosting service with an admin interface and Postg... | [Compose](Apps/picsur/docker-compose.yml) |
| **Pinchflat** | `pinchflat` | Pinchflat is a self-hosted YouTube downloader that allows you to download videos and pl... | [Compose](Apps/pinchflat/docker-compose.yml) |
| **PodFetch** | `podfetch` | PodFetch is a sleek, self-hosted podcast manager that automatically downloads new episo... | [Compose](Apps/podfetch/docker-compose.yml) |
| **Poke** | `poke` | Poke is an open-source, self-hosted alternative to YouTube | [Compose](Apps/poke/docker-compose.yml) |
| **qBittorrent Web UI** | `qbitwebui` | A modern web interface for managing multiple qBittorrent instances | [Compose](Apps/qbitwebui/docker-compose.yml) |
| **qui** | `qui` | A fast, modern web interface for qBittorrent | [Compose](Apps/qui/docker-compose.yml) |
| **Reelsaw** | `reelsaw` | Reelsaw is a self-hosted, AI-powered video clipper: paste a YouTube link or upload a vi... | [Compose](Apps/reelsaw/docker-compose.yml) |
| **Ryot** | `ryot` | A self-hosted platform for tracking various media types including movies, TV shows, vid... | [Compose](Apps/ryot/docker-compose.yml) |
| **Seanime** | `seanime` | A self-hosted anime streaming platform | [Compose](Apps/seanime/docker-compose.yml) |
| **Shoutrrr** | `shoutrrr` | Shoutrrr is an open source social media scheduler for drafting, scheduling, and publish... | [Compose](Apps/shoutrrr/docker-compose.yml) |
| **StreamFlow** | `streamflow` | StreamFlow is a multi-platform live streaming web application that enables simultaneous... | [Compose](Apps/streamflow/docker-compose.yml) |
| **TryPost** | `trypost` | TryPost is an open source social media scheduler with team workspaces, a post composer,... | [Compose](Apps/trypost/docker-compose.yml) |
| **Yamtrack** | `yamtrack` | Yamtrack is a self-hosted anime and manga tracker with Redis backend support | [Compose](Apps/yamtrack/docker-compose.yml) |
| **yt-dlp-webui** | `yt-dlp-webui` | yt-dlp-webui is a web interface for yt-dlp, allowing you to download videos and audio f... | [Compose](Apps/yt-dlp-webui/docker-compose.yml) |
| **Zipline** | `zipline` | A ShareX/file upload server that is easy to use, packed with features, and with an easy... | [Compose](Apps/zipline/docker-compose.yml) |
### 📁 Productivity (158 apps)

| App | Pasta | Descrição | Compose |
| :--- | :--- | :--- | :--- |
| **Activepieces** | `activepieces` | Open-source no-code business automation tool | [Compose](Apps/activepieces/docker-compose.yml) |
| **Affine Pro** | `affinepro` | AFFiNE is a workspace for notes, docs, and whiteboards, and an alternative to Notion | [Compose](Apps/affinepro/docker-compose.yml) |
| **Alarik** | `alarik` | Alarik is a high-performance, S3-compatible object storage | [Compose](Apps/alarik/docker-compose.yml) |
| **AList** | `alist` | ðŸ—‚ï¸A file list/WebDAV program that supports multiple storages, powered by Gin and S... | [Compose](Apps/alist/docker-compose.yml) |
| **App Flowy** | `appflowy` | AppFlowy is a workspace app for notes, docs, and projects, and an open-source alternati... | [Compose](Apps/appflowy/docker-compose.yml) |
| **Appsmith** | `appsmith` | Appsmith is a free and open source platform for building internal tools and applications | [Compose](Apps/appsmith/docker-compose.yml) |
| **ArchiveBox** | `archivebox` | ArchiveBox is a self-hosted internet archiving solution for saving websites, media, and... | [Compose](Apps/archivebox/docker-compose.yml) |
| **Automatisch** | `automatisch` | Automatisch is a powerful, self-hosted workflow automation tool designed for connecting... | [Compose](Apps/automatisch/docker-compose.yml) |
| **Baikal** | `baikal` | Baikal is a lightweight, self-hosted CalDAV and CardDAV server that enables users to ma... | [Compose](Apps/baikal/docker-compose.yml) |
| **BentoPDF** | `bentopdf` | BentoPDF is a lightweight PDF conversion microservice that exposes a simple HTTP API fo... | [Compose](Apps/bentopdf/docker-compose.yml) |
| **Blinko** | `blinko` | Blinko is a modern web application for managing and organizing your digital content and... | [Compose](Apps/blinko/docker-compose.yml) |
| **BookStack** | `bookstack` | BookStack is a wiki platform for organizing documentation | [Compose](Apps/bookstack/docker-compose.yml) |
| **Browserless** | `browserless` | Browserless allows remote clients to connect and execute headless work, all inside of d... | [Compose](Apps/browserless/docker-compose.yml) |
| **Calnode** | `calnode` | Calnode is a Calendly-style booking app — with first-party video meetings, recording, a... | [Compose](Apps/calnode/docker-compose.yml) |
| **Carbone** | `carbone` | Carbone is a high-performance, self-hosted document generation engine | [Compose](Apps/carbone/docker-compose.yml) |
| **ClassicPress** | `classicpress` | ClassicPress is a community-led open source content management system for creators | [Compose](Apps/classicpress/docker-compose.yml) |
| **Cloudflare DDNS** | `cloudflare-ddns` | A small, feature-rich, and robust Cloudflare DDNS updater | [Compose](Apps/cloudflare-ddns/docker-compose.yml) |
| **Cloudflared** | `cloudflared` | A lightweight daemon that securely connects local services to the internet through Clou... | [Compose](Apps/cloudflared/docker-compose.yml) |
| **Cloudreve** | `cloudreve` | Self-hosted file management and sharing system with multi-cloud storage support | [Compose](Apps/cloudreve/docker-compose.yml) |
| **Cockpit** | `cockpit` | Cockpit is a headless content platform designed to streamline the creation, connection,... | [Compose](Apps/cockpit/docker-compose.yml) |
| **CodeX Docs** | `codex-docs` | CodeX is a comprehensive platform that brings together passionate engineers, designers,... | [Compose](Apps/codex-docs/docker-compose.yml) |
| **Colanode Server** | `colanode` | Open-source and local-first Slack and Notion alternative that puts you in control of yo... | [Compose](Apps/colanode/docker-compose.yml) |
| **Collabora Office** | `collabora-office` | Collabora Online is a powerful, flexible, and secure online office suite designed to br... | [Compose](Apps/collabora-office/docker-compose.yml) |
| **CommaFeed** | `commafeed` | CommaFeed is an open-source feed reader and news aggregator, designed to be lightweight... | [Compose](Apps/commafeed/docker-compose.yml) |
| **Confluence** | `confluence` | Confluence is a powerful team collaboration and knowledge-sharing tool | [Compose](Apps/confluence/docker-compose.yml) |
| **Customermates** | `customermates` | Customermates is an open-source CRM for contacts, organizations, deals, services and ta... | [Compose](Apps/customermates/docker-compose.yml) |
| **Cypht** | `cypht` | Lightweight open source webmail aggregator | [Compose](Apps/cypht/docker-compose.yml) |
| **Dagu** | `dagu` | Dagu is a self-contained workflow engine with a Web UI | [Compose](Apps/dagu/docker-compose.yml) |
| **Dexio** | `dexio` | One wiki for all your agents | [Compose](Apps/dexio/docker-compose.yml) |
| **Directus** | `directus` | Directus is an open-source headless CMS that adds an API and admin app to your SQL data... | [Compose](Apps/directus/docker-compose.yml) |
| **Dolibarr** | `dolibarr` | Dolibarr ERP & CRM is a modern software package that helps manage your organization's a... | [Compose](Apps/dolibarr/docker-compose.yml) |
| **Dossier** | `dossier` | Dossier is a personal job search app with a career profile, resume and cover letter dra... | [Compose](Apps/dossier/docker-compose.yml) |
| **Double Zero** | `doublezero` | 00 is a self hostable SES dashboard for sending and monitoring emails with AWS | [Compose](Apps/doublezero/docker-compose.yml) |
| **EmDash** | `emdash` | EmDash is an Astro-native CMS with a visual editor, structured content, media library,... | [Compose](Apps/emdash/docker-compose.yml) |
| **ERPNext** | `erpnext` | ERPNext is an ERP system for managing accounting, inventory, sales, and more | [Compose](Apps/erpnext/docker-compose.yml) |
| **ERPNext** | `erpnext-v16` | 100% Open Source and highly customizable ERP software | [Compose](Apps/erpnext-v16/docker-compose.yml) |
| **Evolution CRM** | `evolutioncrm` | Evo CRM Community is the open-source edition of the Evo CRM platform — a complete suite... | [Compose](Apps/evolutioncrm/docker-compose.yml) |
| **File Browser** | `filebrowser` | Filebrowser is a standalone file manager for uploading, deleting, previewing, renaming,... | [Compose](Apps/filebrowser/docker-compose.yml) |
| **FileGator** | `filegator` | FileGator is a simple self-hosted web file manager with multi-user support | [Compose](Apps/filegator/docker-compose.yml) |
| **FileRun** | `filerun` | FileRun is a self-hosted file manager and file sharing platform | [Compose](Apps/filerun/docker-compose.yml) |
| **Flatnotes** | `flatnotes` | A self-hosted, modern note-taking web app that saves your notes as plain text Markdown... | [Compose](Apps/flatnotes/docker-compose.yml) |
| **Flatnotes (TOTP)** | `flatnotes-totp` | Flatnotes with TOTP authentication enabled (username + password + one-time passcode) | [Compose](Apps/flatnotes-totp/docker-compose.yml) |
| **Focalboard** | `focalboard` | Open source project management for technical teams | [Compose](Apps/focalboard/docker-compose.yml) |
| **Forgejo** | `forgejo` | Forgejo is a self-hosted lightweight software forge | [Compose](Apps/forgejo/docker-compose.yml) |
| **Formbricks** | `formbricks` | Formbricks is an open-source survey platform for collecting user and customer feedback | [Compose](Apps/formbricks/docker-compose.yml) |
| **FreshRSS** | `freshrss` | FreshRSS is a lightweight RSS and Atom feed aggregator | [Compose](Apps/freshrss/docker-compose.yml) |
| **Garage S3** | `garage` | Garage is an open-source distributed object storage service tailored for self-hosting | [Compose](Apps/garage/docker-compose.yml) |
| **Garage S3 with Web UI** | `garage-with-ui` | Garage is an open-source distributed object storage service tailored for self-hosting | [Compose](Apps/garage-with-ui/docker-compose.yml) |
| **Ghost** | `ghost` | Ghost is an open-source publishing platform for blogs, newsletters, and paid memberships | [Compose](Apps/ghost/docker-compose.yml) |
| **GitHub Actions Runner** | `dokploy-actions-runner` | Self-hosted GitHub Actions runner for repositories or organizations, with independent n... | [Compose](Apps/dokploy-actions-runner/docker-compose.yml) |
| **GLPI Project** | `glpi` | The most complete open source service management software | [Compose](Apps/glpi/docker-compose.yml) |
| **Grimoire** | `grimoire` | Grimoire is a self-hosted bookmarking app designed for speed and simplicity | [Compose](Apps/grimoire/docker-compose.yml) |
| **Habitica** | `habitica` | Habitica is a habit and productivity tracker that works like a role-playing game | [Compose](Apps/habitica/docker-compose.yml) |
| **HedgeDoc** | `hedgedoc` | HedgeDoc is a collaborative Markdown editor for teams that need real-time notes, docume... | [Compose](Apps/hedgedoc/docker-compose.yml) |
| **Heyo Docs** | `heyo-docs` | A themeable documentation toolkit for React Router, Next | [Compose](Apps/heyo-docs/docker-compose.yml) |
| **Hoarder** | `hoarder` | Hoarder is an open source "Bookmark Everything" app that uses AI for automatically tagg... | [Compose](Apps/hoarder/docker-compose.yml) |
| **Homepage** | `homepage` | Homepage is a customizable dashboard and start page for your apps and services | [Compose](Apps/homepage/docker-compose.yml) |
| **HortusFox** | `hortusfox` | HortusFox is an open source task and photo management app, designed for photographers a... | [Compose](Apps/hortusfox/docker-compose.yml) |
| **Huly** | `huly` | Huly is an all-in-one project management platform and an alternative to Linear and Jira | [Compose](Apps/huly/docker-compose.yml) |
| **i18n Blog (Kuno)** | `i18n-blog` | Kuno is an internationalized blogging platform with a backend built in Go and a fronten... | [Compose](Apps/i18n-blog/docker-compose.yml) |
| **InfluxDB** | `influxdb` | InfluxDB 2 | [Compose](Apps/influxdb/docker-compose.yml) |
| **Inngest** | `inngest` | Inngest is a developer platform for serverless event-driven workflows | [Compose](Apps/inngest/docker-compose.yml) |
| **Instatic** | `instatic` | Instatic is a self-hosted, open-source visual CMS combining a canvas editor, content en... | [Compose](Apps/instatic/docker-compose.yml) |
| **IPFS (Kubo)** | `ipfs` | IPFS (Kubo) is a decentralized peer-to-peer file sharing and storage network node | [Compose](Apps/ipfs/docker-compose.yml) |
| **It's a Plan** | `itsaplan` | It's a Plan is an open-source project management and issue tracking platform where peop... | [Compose](Apps/itsaplan/docker-compose.yml) |
| **Joomla** | `joomla` | Joomla is a flexible open-source content management system for building websites, porta... | [Compose](Apps/joomla/docker-compose.yml) |
| **Joplin Server** | `joplin-server` | Joplin Server is the sync backend for the Joplin note-taking app | [Compose](Apps/joplin-server/docker-compose.yml) |
| **Kanbn** | `kanbn` | The open-source project management alternative to Trello | [Compose](Apps/kanbn/docker-compose.yml) |
| **KaraKeep** | `karakeep` | A self-hostable bookmark-everything app (links, notes and images) with AI-based automat... | [Compose](Apps/karakeep/docker-compose.yml) |
| **Kestra** | `kestra` | Unified Orchestration Platform to Simplify Business-Critical Workflows and Govern them... | [Compose](Apps/kestra/docker-compose.yml) |
| **Kotonoba** | `kotonoba` | A high-performance, self-hosted, multi-tenant blog CMS built with Next | [Compose](Apps/kotonoba/docker-compose.yml) |
| **Leantime** | `leantime` | Leantime is an open-source project management system for small teams and startups, buil... | [Compose](Apps/leantime/docker-compose.yml) |
| **Letterfeed** | `letterfeed` | Convert email newsletters into RSS feeds | [Compose](Apps/letterfeed/docker-compose.yml) |
| **Libredesk** | `libredesk` | Open source, self-hosted customer support desk | [Compose](Apps/libredesk/docker-compose.yml) |
| **Life Console** | `life-console` | Life Console is a keyboard-first planner that shows what to do right now: time-block yo... | [Compose](Apps/life-console/docker-compose.yml) |
| **LimeSurvey** | `limesurvey` | LimeSurvey is an open-source research platform for building and running online surveys | [Compose](Apps/limesurvey/docker-compose.yml) |
| **LinkStack** | `linkstack` | LinkStack is an open-source link-in-bio platform for sharing multiple links using a cus... | [Compose](Apps/linkstack/docker-compose.yml) |
| **Linkwarden** | `linkwarden` | Linkwarden is an open-source bookmark manager for saving, organizing, and archiving links | [Compose](Apps/linkwarden/docker-compose.yml) |
| **Listmonk** | `listmonk` | High performance, self-hosted, newsletter and mailing list manager with a modern dashboard | [Compose](Apps/listmonk/docker-compose.yml) |
| **MailCatcher NG** | `mailcatcher-ng` | MailCatcher NG runs a super simple SMTP server which catches any message sent to it to... | [Compose](Apps/mailcatcher-ng/docker-compose.yml) |
| **Mailpit** | `mailpit` | Mailpit is a tiny, self-contained, and secure email & SMTP testing tool with API for de... | [Compose](Apps/mailpit/docker-compose.yml) |
| **Mailu** | `mailu` | Full-featured open-source mail server as a set of Docker containers: SMTP (Postfix), IM... | [Compose](Apps/mailu/docker-compose.yml) |
| **Maily** | `maily` | Temporary email REST API gateway with multi-provider rotation, real-time SSE streaming,... | [Compose](Apps/maily/docker-compose.yml) |
| **Markup** | `markup` | Markup is a fast, keyboard-first markdown workspace with live preview, graph view, whit... | [Compose](Apps/markup/docker-compose.yml) |
| **Mautic** | `mautic` | Mautic is the world's largest open-source marketing automation project | [Compose](Apps/mautic/docker-compose.yml) |
| **MaxIO** | `maxio` | MaxIO is a lightweight, single-binary S3-compatible object storage server written in Rust | [Compose](Apps/maxio/docker-compose.yml) |
| **Memos** | `memos` | Memos is a self-hosted, open-source note-taking application that allows you to create,... | [Compose](Apps/memos/docker-compose.yml) |
| **Miniflux** | `miniflux` | Miniflux is a minimalist and opinionated feed reader for self-hosted RSS and Atom subsc... | [Compose](Apps/miniflux/docker-compose.yml) |
| **Minio** | `minio` | MinIO is an open-source, S3-compatible object storage server | [Compose](Apps/minio/docker-compose.yml) |
| **Montara Mail** | `montara-mail` | AI mail client for teams: connect Gmail, Outlook, Yahoo, iCloud, Lark, Zoho or any IMAP... | [Compose](Apps/montara-mail/docker-compose.yml) |
| **MyLinks** | `my-links` | Self-hostable bookmark manager to organize, search and share your favorite links | [Compose](Apps/my-links/docker-compose.yml) |
| **n8n** | `n8n` | n8n is an open-source, low-code platform for automating workflows and integrations | [Compose](Apps/n8n/docker-compose.yml) |
| **n8n Queue Mode** | `n8n-queue` | n8n running in queue mode for high-throughput production workloads: the main instance h... | [Compose](Apps/n8n-queue/docker-compose.yml) |
| **n8n with Postgres** | `n8n-with-postgres` | n8n is an open source low-code platform for automating workflows and integrations with... | [Compose](Apps/n8n-with-postgres/docker-compose.yml) |
| **Notifuse** | `notifuse` | Open-source newsletter and notification platform that empowers teams to create, send, a... | [Compose](Apps/notifuse/docker-compose.yml) |
| **Novu** | `novu` | Open-source notification infrastructure for multi-channel workflows — in-app Inbox, ema... | [Compose](Apps/novu/docker-compose.yml) |
| **Nyxiontech PDF Tools** | `nyxiontech-pdf-tools` | 25 PDF and image tools that run entirely in the browser | [Compose](Apps/nyxiontech-pdf-tools/docker-compose.yml) |
| **Odoo** | `odoo_17` | Odoo is a free and open source business management software that helps you manage your... | [Compose](Apps/odoo_17/docker-compose.yml) |
| **Odoo** | `odoo_18` | Odoo is a free and open source business management software that helps you manage your... | [Compose](Apps/odoo_18/docker-compose.yml) |
| **Odoo** | `odoo_19` | Odoo is a suite of business management apps, including ERP, CRM, and accounting | [Compose](Apps/odoo_19/docker-compose.yml) |
| **OpenCloud** | `opencloud` | Open source cloud platform for secure file sync, sharing, and content collaboration | [Compose](Apps/opencloud/docker-compose.yml) |
| **OpenHabitTracker** | `openhabittracker` | Take notes, plan tasks and track habits - free, ad-free, open source, with all data on... | [Compose](Apps/openhabittracker/docker-compose.yml) |
| **OpenProject** | `openproject` | OpenProject 17 slim: web, worker, cron, Postgres 17, memcached | [Compose](Apps/openproject/docker-compose.yml) |
| **OpenTodo** | `opentodo` | Open-source, local-first task manager | [Compose](Apps/opentodo/docker-compose.yml) |
| **Orbit by Coolify** | `orbit-coollabs` | Self-hosted workspace for teams: tasks, docs and chat in one app on your own server, wi... | [Compose](Apps/orbit-coollabs/docker-compose.yml) |
| **Orbit by Noveum** | `orbit` | Open-source task management with issues, projects, sprints, docs, files, realtime colla... | [Compose](Apps/orbit/docker-compose.yml) |
| **Otter Wiki** | `otterwiki` | An Otter Wiki is a simple, lightweight, and fast wiki engine built with Python and Flask | [Compose](Apps/otterwiki/docker-compose.yml) |
| **Outline** | `outline` | Outline is a self-hosted knowledge base for team documentation | [Compose](Apps/outline/docker-compose.yml) |
| **ownCloud Infinite Scale** | `owncloud-infinite-scale` | ownCloud Infinite Scale is a modern file sync and share platform with WebDAV and ownClo... | [Compose](Apps/owncloud-infinite-scale/docker-compose.yml) |
| **Paperless-ngx** | `paperless-ngx` | Paperless-ngx is a document management system that turns scanned paperwork into a searc... | [Compose](Apps/paperless-ngx/docker-compose.yml) |
| **Plane** | `plane` | Plane is a project management tool and an open-source alternative to Jira and Asana | [Compose](Apps/plane/docker-compose.yml) |
| **Plark** | `plark` | Self-hosted Website Builder | [Compose](Apps/plark/docker-compose.yml) |
| **Plunk** | `plunk` | Plunk is the open-source, affordable email platform that brings together marketing, tra... | [Compose](Apps/plunk/docker-compose.yml) |
| **Portainer** | `portainer` | Portainer is a container management tool for deploying, troubleshooting, and securing a... | [Compose](Apps/portainer/docker-compose.yml) |
| **Poste.io** | `poste.io` | Complete mail server solution with SMTP, IMAP, POP3, antispam, antivirus, web administr... | [Compose](Apps/poste.io/docker-compose.yml) |
| **Postiz** | `postiz` | Postiz is a modern, open-source platform for managing and publishing content across mul... | [Compose](Apps/postiz/docker-compose.yml) |
| **Prefect** | `prefect` | Prefect is an open-source workflow orchestration platform for building, scheduling, mon... | [Compose](Apps/prefect/docker-compose.yml) |
| **PrivatePaste** | `privatepaste` | Self-hosted clipboard sync: copy on one device, paste on your others, with an encrypted... | [Compose](Apps/privatepaste/docker-compose.yml) |
| **Puppetflow** | `puppetflow` | A self-hosted browser automation platform for building, running, and monitoring JavaScr... | [Compose](Apps/puppetflow/docker-compose.yml) |
| **Puppetflow with Postgres** | `puppetflow-postgres` | A self-hosted browser automation platform for building, running, and monitoring JavaScr... | [Compose](Apps/puppetflow-postgres/docker-compose.yml) |
| **Quire Ink** | `quireink` | A self-hosted blog in one container: a real editor over Markdown with tables, footnotes... | [Compose](Apps/quireink/docker-compose.yml) |
| **Reactive Resume** | `reactive-resume` | A free and open-source resume builder that simplifies the process of creating, updating... | [Compose](Apps/reactive-resume/docker-compose.yml) |
| **Reloop** | `reloop` | Open-source email platform for transactional mail, campaigns and inbound, with its own... | [Compose](Apps/reloop/docker-compose.yml) |
| **Rote** | `rote` | Rote is an open-source multi-platform personal note system featuring an open API, full... | [Compose](Apps/rote/docker-compose.yml) |
| **Roundcube** | `roundcube` | Free and open source webmail software for the masses, written in PHP | [Compose](Apps/roundcube/docker-compose.yml) |
| **RSS-Bridge** | `rss-bridge` | RSS-Bridge is a PHP project capable of generating Atom feeds for websites that don't ha... | [Compose](Apps/rss-bridge/docker-compose.yml) |
| **RSSHub** | `rsshub` | RSSHub is the world's largest RSS network, consisting of over 5,000 global instances | [Compose](Apps/rsshub/docker-compose.yml) |
| **RustDesk** | `rustdesk` | RustDesk is a remote desktop tool and an open-source alternative to TeamViewer | [Compose](Apps/rustdesk/docker-compose.yml) |
| **RustFS** | `rustfs` | RustFS is a high-performance, S3-compatible distributed object storage system built in... | [Compose](Apps/rustfs/docker-compose.yml) |
| **Seafile** | `seafile` | Seafile is an open-source file sync and sharing platform | [Compose](Apps/seafile/docker-compose.yml) |
| **SeaweedFS** | `seaweedfs` | SeaweedFS is a fast distributed storage system for blobs, objects, and files | [Compose](Apps/seaweedfs/docker-compose.yml) |
| **SendDock** | `senddock` | Open-source, self-hosted email marketing platform with BYO SMTP | [Compose](Apps/senddock/docker-compose.yml) |
| **SFTPGo** | `sftpgo` | SFTPGo is a full-featured and highly configurable SFTP, HTTP/S, FTP/S, and WebDAV server | [Compose](Apps/sftpgo/docker-compose.yml) |
| **Shiori** | `shiori` | Shiori is a simple self-hosted bookmark manager with offline archive support and a web... | [Compose](Apps/shiori/docker-compose.yml) |
| **Silo** | `silo` | S3-Compatible Object Storage | [Compose](Apps/silo/docker-compose.yml) |
| **SilverBullet** | `silverbullet` | SilverBullet is a personal knowledge base and collaborative note-taking platform | [Compose](Apps/silverbullet/docker-compose.yml) |
| **Slash** | `slash` | Slash is a modern, self-hosted bookmarking service and link shortener that helps you or... | [Compose](Apps/slash/docker-compose.yml) |
| **Spacedrive** | `spacedrive` | Spacedrive is a cross-platform file manager | [Compose](Apps/spacedrive/docker-compose.yml) |
| **Stalwart** | `stalwart` | Stalwart Mail Server is an open-source mail server solution with JMAP, IMAP4, POP3, and... | [Compose](Apps/stalwart/docker-compose.yml) |
| **Steedos** | `steedos` | Steedos is an open-source low-code platform and alternative to Salesforce, designed to... | [Compose](Apps/steedos/docker-compose.yml) |
| **Stirling PDF** | `stirling` | A locally hosted one-stop shop for all your PDF needs | [Compose](Apps/stirling/docker-compose.yml) |
| **Taiga** | `taiga` | Taiga is a free and open-source project management platform for agile developers, desig... | [Compose](Apps/taiga/docker-compose.yml) |
| **tela** | `tela` | Self-hostable, markdown-native team wiki with live collaboration, full-text and semanti... | [Compose](Apps/tela/docker-compose.yml) |
| **TREK** | `trek` | A minimalist, self-hosted trip planner with Kanban-style task boards, budgets, packing... | [Compose](Apps/trek/docker-compose.yml) |
| **Trilium** | `trilium` | Trilium Notes is a hierarchical note taking application with focus on building large pe... | [Compose](Apps/trilium/docker-compose.yml) |
| **TriliumNext** | `trilium-next` | Is a free and open-source, cross-platform hierarchical note taking application with foc... | [Compose](Apps/trilium-next/docker-compose.yml) |
| **Twenty CRM** | `twenty` | Twenty is a modern CRM and an open-source alternative to Salesforce | [Compose](Apps/twenty/docker-compose.yml) |
| **Typecho** | `typecho` | Typecho æ˜¯ä¸€ä¸ªè½»é‡çº§çš„å¼€æºåšå®¢ç¨‹åºï¼ŒåŸºäºŽ PHP å¼€å‘ï¼Œæ”¯æŒå¤šç§æ•°æ... | [Compose](Apps/typecho/docker-compose.yml) |
| **VersityGW** | `versitygw` | VersityGW is a high-performance S3-compatible gateway that exposes POSIX filesystems, S... | [Compose](Apps/versitygw/docker-compose.yml) |
| **Vikunja** | `vikunja` | Vikunja is an open-source to-do list and task management app | [Compose](Apps/vikunja/docker-compose.yml) |
| **wallabag** | `wallabag` | wallabag is a self-hosted read-it-later application for saving, classifying, and readin... | [Compose](Apps/wallabag/docker-compose.yml) |
| **Whatomate** | `whatomate` | Modern, open-source WhatsApp Business Platform with real-time chat, chatbot automation,... | [Compose](Apps/whatomate/docker-compose.yml) |
| **Wiki.js** | `wikijs` | The most powerful and extensible open source Wiki software | [Compose](Apps/wikijs/docker-compose.yml) |
| **Windmill** | `windmill` | A developer platform to build production-grade workflows and internal apps | [Compose](Apps/windmill/docker-compose.yml) |
| **Windshift** | `windshift` | Self-hosted work management platform with projects, tasks, sprints, and team collaboration | [Compose](Apps/windshift/docker-compose.yml) |
| **Wordpress** | `wordpress` | Wordpress is a free and open source content management system (CMS) for publishing and... | [Compose](Apps/wordpress/docker-compose.yml) |
| **WupNext** | `wupnext` | WupNext is a self-hosted to-do and task queue app: groups, subtasks, deadlines, a built... | [Compose](Apps/wupnext/docker-compose.yml) |
| **Yuvomi** | `yuvomi` | Privacy-first, self-hosted family planner: tasks, calendar sync, shopping, meals, budge... | [Compose](Apps/yuvomi/docker-compose.yml) |
### 📁 Home (14 apps)

| App | Pasta | Descrição | Compose |
| :--- | :--- | :--- | :--- |
| **ChirpStack** | `chirpstack` | Open-source LoRaWAN Network Server for IoT applications | [Compose](Apps/chirpstack/docker-compose.yml) |
| **Eclipse Mosquitto** | `mosquitto` | A lightweight, open-source MQTT broker for IoT and home automation with persistent mess... | [Compose](Apps/mosquitto/docker-compose.yml) |
| **EMQX** | `emqx` | A scalable and reliable MQTT broker for AI, IoT, IIoT and connected vehicles | [Compose](Apps/emqx/docker-compose.yml) |
| **Ferret** | `ferret` | Self-hosted home inventory: find anything you own | [Compose](Apps/ferret/docker-compose.yml) |
| **HiveMQ Community Edition** | `hivemq-ce` | Open-source MQTT 3 | [Compose](Apps/hivemq-ce/docker-compose.yml) |
| **Home Assistant** | `homeassistant` | Home Assistant is a home automation platform that makes sure you can control your smart... | [Compose](Apps/homeassistant/docker-compose.yml) |
| **Homebox** | `homebox` | Homebox is a self-hosted home inventory and organization app for tracking belongings, l... | [Compose](Apps/homebox/docker-compose.yml) |
| **Homebridge** | `homebridge` | Homebridge is a tool that brings Apple HomeKit support to smart home devices that don't... | [Compose](Apps/homebridge/docker-compose.yml) |
| **Homelable** | `homelable` | Self-hosted homelab infrastructure visualisation, documentation, network scanning and l... | [Compose](Apps/homelable/docker-compose.yml) |
| **KitchenOwl** | `kitchenowl` | KitchenOwl is a self-hosted grocery list and recipe manager | [Compose](Apps/kitchenowl/docker-compose.yml) |
| **Mealie (sqlite version)** | `mealie` | Mealie is an intuitive and easy to use recipe management app | [Compose](Apps/mealie/docker-compose.yml) |
| **Scrypted** | `scrypted` | Scrypted is a home automation platform that integrates with various smart home devices... | [Compose](Apps/scrypted/docker-compose.yml) |
| **Tandoor Recipes** | `tandoor-recipes` | Tandoor Recipes is a self-hosted recipe manager, meal planner, and shopping list applic... | [Compose](Apps/tandoor-recipes/docker-compose.yml) |
| **ThingsBoard** | `thingsboard` | ThingsBoard is an open-source IoT platform for device management, data collection, proc... | [Compose](Apps/thingsboard/docker-compose.yml) |
### 📁 Networking (102 apps)

| App | Pasta | Descrição | Compose |
| :--- | :--- | :--- | :--- |
| **2FAuth** | `2fauth` | 2FAuth is a self-hosted web app for managing two-factor authentication tokens: organize... | [Compose](Apps/2fauth/docker-compose.yml) |
| **3Dokploy** | `3dokploy` | A live, isometric 3D view of your Dokploy: projects as buildings, services as racks, de... | [Compose](Apps/3dokploy/docker-compose.yml) |
| **Ackee** | `ackee` | Ackee is a self-hosted analytics tool for your website | [Compose](Apps/ackee/docker-compose.yml) |
| **AdGuard Home** | `adguardhome` | AdGuard Home is a network-wide ad and tracker blocker | [Compose](Apps/adguardhome/docker-compose.yml) |
| **Agent DVR** | `agentdvr` | Agent DVR is a comprehensive video surveillance software with motion detection, alerts,... | [Compose](Apps/agentdvr/docker-compose.yml) |
| **Airbyte** | `airbyte` | Open-source data movement for ELT pipelines and AI agents | [Compose](Apps/airbyte/docker-compose.yml) |
| **Aptabase** | `aptabase` | Aptabase is a self-hosted web analytics platform that lets you track website traffic an... | [Compose](Apps/aptabase/docker-compose.yml) |
| **Authelia** | `authelia` | Authelia is an open-source authentication portal for single sign-on (SSO) and two-facto... | [Compose](Apps/authelia/docker-compose.yml) |
| **Authentik** | `authentik` | Authentik is an identity provider for single sign-on (SSO) authorization and authentica... | [Compose](Apps/authentik/docker-compose.yml) |
| **Authorizer** | `authorizer` | Authorizer is a powerful tool designed to simplify the process of user authentication a... | [Compose](Apps/authorizer/docker-compose.yml) |
| **Beszel** | `beszel` | A lightweight server monitoring hub with historical data, docker stats, and alerts | [Compose](Apps/beszel/docker-compose.yml) |
| **Cachkey** | `cachkey` | Cachkey is an open-source, self-hosted manager for secrets and environment variables: e... | [Compose](Apps/cachkey/docker-compose.yml) |
| **Casdoor** | `casdoor` | An open-source UI-first Identity and Access Management (IAM) / Single-Sign-On (SSO) pla... | [Compose](Apps/casdoor/docker-compose.yml) |
| **CertMate** | `certmate` | CertMate is an SSL certificate management system with a web UI and REST API | [Compose](Apps/certmate/docker-compose.yml) |
| **Change Detection** | `changedetection` | Changedetection | [Compose](Apps/changedetection/docker-compose.yml) |
| **Checkcle** | `checkcle` | Checkcle is a security and compliance tool by Operacle, providing insights into system... | [Compose](Apps/checkcle/docker-compose.yml) |
| **Checkmate** | `checkmate` | Checkmate is an open-source, self-hosted tool designed to track and monitor server hard... | [Compose](Apps/checkmate/docker-compose.yml) |
| **Container Monitoring** | `container-monitoring` | Per-container and host monitoring with cAdvisor, node-exporter, Prometheus and Grafana | [Compose](Apps/container-monitoring/docker-compose.yml) |
| **Corsfix** | `corsfix` | Corsfix is an open source CORS proxy platform for fetching APIs from browser applicatio... | [Compose](Apps/corsfix/docker-compose.yml) |
| **Crowdsec** | `crowdsec` | CrowdSec provides open source solution for detecting and blocking malicious IPs, safegu... | [Compose](Apps/crowdsec/docker-compose.yml) |
| **CyberChef** | `cyberchef` | CyberChef is a web application for encryption, encoding, compression, and data analysis... | [Compose](Apps/cyberchef/docker-compose.yml) |
| **Dashy** | `dashy` | Dashy is a customizable dashboard for organizing your apps and services | [Compose](Apps/dashy/docker-compose.yml) |
| **DataLens** | `datalens` | A modern, scalable business intelligence and data visualization system | [Compose](Apps/datalens/docker-compose.yml) |
| **DockRoute** | `dockroute` | External-DNS for plain Docker hosts: watches container labels and reconciles DNS record... | [Compose](Apps/dockroute/docker-compose.yml) |
| **DockTail** | `docktail` | DockTail exposes Docker containers as native Tailscale Services using labels, with no p... | [Compose](Apps/docktail/docker-compose.yml) |
| **Dokploy Prometheus Monitoring Extension** | `dokploy-prom-monitoring-extension` | Dokploy monitoring extension with Prometheus metrics export for external monitoring sys... | [Compose](Apps/dokploy-prom-monitoring-extension/docker-compose.yml) |
| **Dozzle** | `dozzle` | Dozzle is a real-time log viewer for Docker containers | [Compose](Apps/dozzle/docker-compose.yml) |
| **Falco** | `falco` | Monitor Linux host and container activity with Falco's modern eBPF engine | [Compose](Apps/falco/docker-compose.yml) |
| **FlareSolverr** | `flaresolverr` | FlareSolverr is a proxy server to bypass Cloudflare and DDoS-GUARD protection | [Compose](Apps/flaresolverr/docker-compose.yml) |
| **FMD Server** | `fmd-server` | A server to communicate with the FMD Android app, to locate and control your devices | [Compose](Apps/fmd-server/docker-compose.yml) |
| **Gatus** | `gatus` | Gatus is an automated service health dashboard for monitoring HTTP, DNS, TCP, ICMP, and... | [Compose](Apps/gatus/docker-compose.yml) |
| **Gitingest** | `gitingest` | Gitingest is an application that supports Prometheus metrics, Sentry integration, and S... | [Compose](Apps/gitingest/docker-compose.yml) |
| **Glance** | `glance` | A self-hosted dashboard that puts all your feeds in one place | [Compose](Apps/glance/docker-compose.yml) |
| **Glances** | `glances` | Glances is a cross-platform system monitoring tool | [Compose](Apps/glances/docker-compose.yml) |
| **GoatCounter** | `goatcounter` | GoatCounter is an open source web analytics platform available as a free donation-suppo... | [Compose](Apps/goatcounter/docker-compose.yml) |
| **Grafana** | `grafana` | Grafana is an open-source dashboard tool for monitoring and visualizing data | [Compose](Apps/grafana/docker-compose.yml) |
| **Graylog** | `graylog` | Graylog Open collects, indexes, and searches logs, with dashboards and alerts | [Compose](Apps/graylog/docker-compose.yml) |
| **Grovs** | `grovs` | Self-hosted deep linking, attribution and analytics for mobile and web apps | [Compose](Apps/grovs/docker-compose.yml) |
| **Healthchecks** | `healthchecks` | Healthchecks is an open-source cron job and background task monitoring service that ale... | [Compose](Apps/healthchecks/docker-compose.yml) |
| **Homarr** | `homarr` | Homarr is a dashboard for organizing and accessing all your apps from one place | [Compose](Apps/homarr/docker-compose.yml) |
| **HyperDX** | `hyperdx` | HyperDX searches and visualizes logs, traces, metrics, and session replays | [Compose](Apps/hyperdx/docker-compose.yml) |
| **Kener** | `kener` | Kener is an open-source status page system for monitoring and alerting | [Compose](Apps/kener/docker-compose.yml) |
| **Keycloak** | `keycloak` | Keycloak is an open-source identity and access management tool with single sign-on (SSO) | [Compose](Apps/keycloak/docker-compose.yml) |
| **Keyzori** | `keyzori` | Self-hosted software license server with customer management, device access controls, s... | [Compose](Apps/keyzori/docker-compose.yml) |
| **Komari Monitor** | `komari-monitor` | A lightweight, self-hosted server monitoring tool for tracking server performance | [Compose](Apps/komari-monitor/docker-compose.yml) |
| **kuukura** | `kuukura` | kuukura is a self-hosted secrets vault for small teams: values are decrypted only on yo... | [Compose](Apps/kuukura/docker-compose.yml) |
| **LibreSpeed** | `librespeed` | LibreSpeed is a lightweight, self-hosted HTML5 speed test for measuring download, uploa... | [Compose](Apps/librespeed/docker-compose.yml) |
| **maintenant** | `maintenant` | Self-hosted monitoring for Docker, Swarm and Kubernetes in a single Go binary that uses... | [Compose](Apps/maintenant/docker-compose.yml) |
| **Marketing Dashboard** | `marketing-dashboard` | Self-hosted marketing operations dashboard for product-led growth, checkout analytics,... | [Compose](Apps/marketing-dashboard/docker-compose.yml) |
| **Matomo** | `matomo` | Matomo is an open-source web analytics platform that gives you full ownership of your data | [Compose](Apps/matomo/docker-compose.yml) |
| **mcpspan** | `mcpspan` | mcpspan is open-source analytics for MCP servers: which tools agents call, how often th... | [Compose](Apps/mcpspan/docker-compose.yml) |
| **MikroTik RouterOS** | `mikrotik` | MikroTik RouterOS CHR running in a container — routing and firewall managed with WinBox... | [Compose](Apps/mikrotik/docker-compose.yml) |
| **Montara Pass** | `montara-pass` | Self-hosted password manager with an end-to-end encrypted vault — the server stores cip... | [Compose](Apps/montara-pass/docker-compose.yml) |
| **Netdata** | `netdata` | Netdata is a real-time monitoring tool for system and application performance | [Compose](Apps/netdata/docker-compose.yml) |
| **Networking Toolbox** | `networking-toolbox` | A collection of handy networking utilities by Lissy93, packaged as a self-hostable web app | [Compose](Apps/networking-toolbox/docker-compose.yml) |
| **One Time Secret** | `onetimesecret` | Share sensitive information securely with self-destructing links that are only viewable... | [Compose](Apps/onetimesecret/docker-compose.yml) |
| **OneUptime** | `oneuptime` | OneUptime is an open-source observability platform: uptime monitoring, status pages, in... | [Compose](Apps/oneuptime/docker-compose.yml) |
| **Open Analytics** | `openanalytics` | Open Analytics is an open-source, AI-native web analytics platform: realtime dashboards... | [Compose](Apps/openanalytics/docker-compose.yml) |
| **OpenBao** | `openbao` | OpenBao is an open-source, community-driven fork of HashiCorp Vault under the Linux Fou... | [Compose](Apps/openbao/docker-compose.yml) |
| **OpenFault** | `openfault` | Self-hosted, Sentry-compatible error tracker | [Compose](Apps/openfault/docker-compose.yml) |
| **OpenPanel** | `openpanel` | An open-source web and product analytics platform that combines the power of Mixpanel w... | [Compose](Apps/openpanel/docker-compose.yml) |
| **OpenResty Manager** | `openresty-manager` | The easiest using, powerful and beautiful OpenResty Manager (Nginx Enhanced Version) ,... | [Compose](Apps/openresty-manager/docker-compose.yml) |
| **OpenSEO** | `openseo` | OpenSEO is an open source, self-hosted alternative to Semrush and Ahrefs for keyword re... | [Compose](Apps/openseo/docker-compose.yml) |
| **OpenSpeedTest** | `openspeedtest` | OpenSpeedTest is a 100% browser-based HTML5 network performance estimation tool for acc... | [Compose](Apps/openspeedtest/docker-compose.yml) |
| **OpenStatus** | `openstatus` | OpenStatus is an open-source synthetic monitoring platform with beautiful status pages,... | [Compose](Apps/openstatus/docker-compose.yml) |
| **Passbolt** | `passbolt` | Passbolt is an open-source password manager built for teams | [Compose](Apps/passbolt/docker-compose.yml) |
| **Pastefy** | `pastefy` | Pastefy is an open-source pastebin with support for syntax highlighting and OAuth2 auth... | [Compose](Apps/pastefy/docker-compose.yml) |
| **Plausible** | `plausible` | Plausible is an open-source, lightweight, and privacy-friendly web analytics tool | [Compose](Apps/plausible/docker-compose.yml) |
| **Pocket ID** | `pocket-id` | Pocket ID is a simple OpenID Connect and OAuth 2 | [Compose](Apps/pocket-id/docker-compose.yml) |
| **PostHog** | `posthog` | PostHog is an open-source product analytics platform with feature flags and session replay | [Compose](Apps/posthog/docker-compose.yml) |
| **Prometheus** | `prometheus` | Prometheus is an open-source monitoring and alerting toolkit that collects metrics from... | [Compose](Apps/prometheus/docker-compose.yml) |
| **Pulse** | `pulse` | A responsive monitoring platform for Proxmox VE, PBS, and Docker with real-time metrics... | [Compose](Apps/pulse/docker-compose.yml) |
| **Rustrak** | `rustrak` | Self-hosted error tracking compatible with Sentry SDKs | [Compose](Apps/rustrak/docker-compose.yml) |
| **Rustrak (Full Stack SQLite)** | `rustrak-sqlite` | Self-hosted error tracking compatible with Sentry SDKs | [Compose](Apps/rustrak-sqlite/docker-compose.yml) |
| **Rustrak (Full Stack)** | `rustrak-full` | Self-hosted error tracking compatible with Sentry SDKs | [Compose](Apps/rustrak-full/docker-compose.yml) |
| **Rybbit** | `rybbit` | Open-source and privacy-friendly alternative to Google Analytics that is 10x more intui... | [Compose](Apps/rybbit/docker-compose.yml) |
| **Sable** | `sable` | Sable is a modern, high-performance DNS platform with recursive and authoritative DNS,... | [Compose](Apps/sable/docker-compose.yml) |
| **Scrutiny** | `scrutiny` | Hard Drive S | [Compose](Apps/scrutiny/docker-compose.yml) |
| **SigNoz** | `signoz` | SigNoz is an open-source Datadog or New Relic alternative | [Compose](Apps/signoz/docker-compose.yml) |
| **Snapp** | `snapp` | Snapp is a self-hosted screenshot sharing service with user management and authentication | [Compose](Apps/snapp/docker-compose.yml) |
| **SolidPing** | `solidping` | Distributed, self-hostable uptime monitoring: 40+ check types, multi-region workers, pr... | [Compose](Apps/solidping/docker-compose.yml) |
| **Speedtest Tracker** | `speedtest-tracker` | Speedtest Tracker runs scheduled internet speed tests and stores the results in a self-... | [Compose](Apps/speedtest-tracker/docker-compose.yml) |
| **Stack Auth** | `stack-auth` | Open-source Auth0/Clerk alternative | [Compose](Apps/stack-auth/docker-compose.yml) |
| **Statping-NG** | `statping-ng` | Statping-NG is an easy-to-use status page for monitoring websites and applications with... | [Compose](Apps/statping-ng/docker-compose.yml) |
| **Superset (Unofficial)** | `superset` | Data visualization and data exploration platform | [Compose](Apps/superset/docker-compose.yml) |
| **Tailscale Exit nodes** | `tailscale-exitnode` | Tailscale ExitNode is a feature that lets you route your internet traffic through a spe... | [Compose](Apps/tailscale-exitnode/docker-compose.yml) |
| **Tianji** | `tianji` | Tianji is a lightweight web analytic service and uptime monitoring tool | [Compose](Apps/tianji/docker-compose.yml) |
| **Tor Browser** | `tor-browser` | A Dockerized Tor Browser accessible via web VNC (noVNC) and VNC client | [Compose](Apps/tor-browser/docker-compose.yml) |
| **Umami** | `umami` | Umami is a simple website analytics tool and an alternative to Google Analytics | [Compose](Apps/umami/docker-compose.yml) |
| **Unifi Network** | `unifi` | Unifi Network is an open-source enterprise network management platform for wireless net... | [Compose](Apps/unifi/docker-compose.yml) |
| **Upsnap** | `upsnap` | Upsnap is a simple network device monitor and dashboard built on PocketBase | [Compose](Apps/upsnap/docker-compose.yml) |
| **Uptime Kotlin** | `uptime-kotlin` | Uptime Kotlin is an open-source monitoring tool that tracks the uptime of your websites... | [Compose](Apps/uptime-kotlin/docker-compose.yml) |
| **Uptime Kuma** | `uptime-kuma` | Uptime Kuma is an open-source monitoring tool that tracks the uptime of your websites a... | [Compose](Apps/uptime-kuma/docker-compose.yml) |
| **Uptimekit** | `uptimekit` | The modern open-source status page and monitoring solution | [Compose](Apps/uptimekit/docker-compose.yml) |
| **Uptimy Agent** | `uptimy-agent` | Uptimy Agent is a lightweight, open-source uptime monitor with a status page: HTTP, TCP... | [Compose](Apps/uptimy-agent/docker-compose.yml) |
| **Vault** | `vault` | Vault is HashiCorp's tool for securely storing and managing secrets and encryption keys | [Compose](Apps/vault/docker-compose.yml) |
| **VictoriaMetrics** | `victoriametrics` | VictoriaMetrics is a fast, cost-effective, and scalable monitoring solution and time se... | [Compose](Apps/victoriametrics/docker-compose.yml) |
| **Wazuh** | `wazuh` | Open source security platform (SIEM/XDR): threat detection, integrity monitoring, vulne... | [Compose](Apps/wazuh/docker-compose.yml) |
| **Web-Check** | `web-check` | Web-Check is a powerful all-in-one website analyzer that provides detailed insights int... | [Compose](Apps/web-check/docker-compose.yml) |
| **WG-Easy** | `wg-easy` | WG-Easy is a simple and user-friendly WireGuard VPN server with a web interface for eas... | [Compose](Apps/wg-easy/docker-compose.yml) |
| **WUD (What's Up Docker?)** | `wud` | WUD monitors Docker containers for image updates and shows available versions in a web... | [Compose](Apps/wud/docker-compose.yml) |
| **Zabbix** | `zabbix` | Zabbix is an open-source enterprise-grade monitoring platform for networks, servers, vi... | [Compose](Apps/zabbix/docker-compose.yml) |
### 📁 AI (60 apps)

| App | Pasta | Descrição | Compose |
| :--- | :--- | :--- | :--- |
| **9Router** | `9router` | Self-hosted AI model router that rotates requests across 40+ providers with automatic f... | [Compose](Apps/9router/docker-compose.yml) |
| **Agent Zero** | `agent-zero` | Agent Zero is an open-source autonomous AI agent framework with memory and tool use cap... | [Compose](Apps/agent-zero/docker-compose.yml) |
| **Anse** | `anse` | Anse is an open-source alternative to ChatGPT web UI, supporting OpenAI-compatible APIs | [Compose](Apps/anse/docker-compose.yml) |
| **AnythingLLM** | `anythingllm` | AnythingLLM is a private AI chat app for working with your own documents | [Compose](Apps/anythingllm/docker-compose.yml) |
| **Arche** | `arche` | Arche is a self-hosted AI workspace platform that spawns per-user OpenCode coding conta... | [Compose](Apps/arche/docker-compose.yml) |
| **Argilla** | `argilla` | Argilla is a robust platform designed to help engineers and data scientists streamline... | [Compose](Apps/argilla/docker-compose.yml) |
| **BlogFactory** | `blogfactory` | Self-hosted control plane for AI-assisted content operations and human-approved CMS dra... | [Compose](Apps/blogfactory/docker-compose.yml) |
| **bolt.diy** | `bolt.diy` | Prompt, run, edit, and deploy full-stack web applications using any LLM you want! | [Compose](Apps/bolt.diy/docker-compose.yml) |
| **Botpress** | `botpress` | Botpress is a platform for building conversational AI agents | [Compose](Apps/botpress/docker-compose.yml) |
| **ByteStash** | `bytestash` | ByteStash is a self-hosted web application designed to store, organise, and manage your... | [Compose](Apps/bytestash/docker-compose.yml) |
| **Chroma** | `chroma` | Chroma is an open-source embedding database for AI applications, with persistent vector... | [Compose](Apps/chroma/docker-compose.yml) |
| **Creed** | `creed` | One personal context file every AI agent reads before answering and proposes updates to... | [Compose](Apps/creed/docker-compose.yml) |
| **Dify** | `dify` | Dify is an open-source LLM app development platform | [Compose](Apps/dify/docker-compose.yml) |
| **Domain Locker** | `domain-locker` | Domain Locker is an open-source tool for tracking domain expirations and sending renewa... | [Compose](Apps/domain-locker/docker-compose.yml) |
| **Engram** | `engram` | Persistent memory for AI coding agents — self-hosted Engram Cloud sync server with a we... | [Compose](Apps/engram/docker-compose.yml) |
| **Flowise** | `flowise` | Flowise is an open-source UI visual tool to build and run LLM-powered applications | [Compose](Apps/flowise/docker-compose.yml) |
| **Free Image to Video Generator** | `fitv-video-starter` | Free image to video AI with no daily cap: start with no sign-up, keep going on a free a... | [Compose](Apps/fitv-video-starter/docker-compose.yml) |
| **FreeLLMAPI** | `freellmapi` | FreeLLMAPI aggregates free tiers from 29 LLM providers into a single OpenAI-compatible... | [Compose](Apps/freellmapi/docker-compose.yml) |
| **Hermes** | `hermes` | Hermes is an open agent runtime from Nous Research, exposing an OpenAI-compatible gatew... | [Compose](Apps/hermes/docker-compose.yml) |
| **HeyForm** | `heyform` | Allows anyone to create engaging conversational forms for surveys, questionnaires, quiz... | [Compose](Apps/heyform/docker-compose.yml) |
| **Junctio** | `junctio` | Self-hosted MCP gateway that puts stdio, Docker and remote MCP servers behind one endpo... | [Compose](Apps/junctio/docker-compose.yml) |
| **Kavel Image Starter** | `kavel-image-starter` | One-page text-to-image web app: type a prompt, pick an aspect ratio, get the image back... | [Compose](Apps/kavel-image-starter/docker-compose.yml) |
| **Kokoro TTS** | `kokoro-tts` | Dockerized FastAPI wrapper for the Kokoro-82M text-to-speech model with multi-language... | [Compose](Apps/kokoro-tts/docker-compose.yml) |
| **Kokoro Web** | `kokoro-web` | Kokoro Web provides an interface for text-to-speech using advanced AI voice synthesis | [Compose](Apps/kokoro-web/docker-compose.yml) |
| **Kortix** | `kortix` | Kortix is an open source AI Operating System: AI agents that do real work for your team... | [Compose](Apps/kortix/docker-compose.yml) |
| **Langflow** | `langflow` | Langflow is a low-code app builder for RAG and multi-agent AI applications | [Compose](Apps/langflow/docker-compose.yml) |
| **Langfuse** | `langfuse` | Langfuse is an open-source LLM engineering platform for tracing, prompt management, eva... | [Compose](Apps/langfuse/docker-compose.yml) |
| **LibreChat** | `librechat` | LibreChat is the ultimate open-source app for all your AI conversations, fully customiz... | [Compose](Apps/librechat/docker-compose.yml) |
| **LiteLLM** | `litellm` | LiteLLM is a lightweight OpenAI API-compatible proxy for managing multiple LLM provider... | [Compose](Apps/litellm/docker-compose.yml) |
| **LubeLogger** | `lubelogger` | LubeLogger is a self-hosted vehicle maintenance and fuel mileage tracker for managing s... | [Compose](Apps/lubelogger/docker-compose.yml) |
| **Moltbot** | `moltbot` | WhatsApp gateway CLI with Pi RPC agent - self-hosted AI-powered messaging platform | [Compose](Apps/moltbot/docker-compose.yml) |
| **Multica** | `multica` | Multica is an open-source managed agents platform for teams | [Compose](Apps/multica/docker-compose.yml) |
| **n8n + Worker + Runner with Redis/Postgres and Ollama** | `n8n-runner-postgres-ollama` | n8n is an open source low-code platform for automating workflows and integrations with... | [Compose](Apps/n8n-runner-postgres-ollama/docker-compose.yml) |
| **Nakama** | `nakama` | AI agent platform for teams: a shared workspace where agents get their own tools, skill... | [Compose](Apps/nakama/docker-compose.yml) |
| **Obscura Browser** | `obscura` | Headless browser for AI agents with authenticated remote MCP and Chrome DevTools Protoc... | [Compose](Apps/obscura/docker-compose.yml) |
| **Ollama Chat Tone** | `ollama-chat-tone` | Self-contained Ollama chat client with local auth, streaming responses, and per-user co... | [Compose](Apps/ollama-chat-tone/docker-compose.yml) |
| **OmniRoute** | `omniroute` | The Free AI Gateway - Never stop coding | [Compose](Apps/omniroute/docker-compose.yml) |
| **Open Fiesta** | `open-fiesta` | Open Fiesta is an open-source AI chat and inference UI, supporting multiple backends su... | [Compose](Apps/open-fiesta/docker-compose.yml) |
| **Open Notebook** | `open_notebook` | Open Notebook with SurrealDB for data storage and AI-powered features | [Compose](Apps/open_notebook/docker-compose.yml) |
| **Openclaw** | `openclaw` | WhatsApp gateway CLI with Pi RPC agent - self-hosted AI-powered messaging platform | [Compose](Apps/openclaw/docker-compose.yml) |
| **OpenCode** | `opencode` | OpenCode is an open source AI coding agent | [Compose](Apps/opencode/docker-compose.yml) |
| **OpenDots** | `opendots` | OpenDots is an open-source template from CopilotKit for always-on AI coworkers: special... | [Compose](Apps/opendots/docker-compose.yml) |
| **OpenHands** | `openhands` | OpenHands is an open-source platform for running and managing AI agents | [Compose](Apps/openhands/docker-compose.yml) |
| **OpenLivery** | `openlivery` | MIT-licensed WhatsApp AI agents for agencies, with separate client workspaces and brand... | [Compose](Apps/openlivery/docker-compose.yml) |
| **OpenSourcePOS** | `opensourcepos` | OpenSourcePOS is a web-based point of sale system for managing sales, inventory, custom... | [Compose](Apps/opensourcepos/docker-compose.yml) |
| **Orca Server** | `orca-server` | Headless Orca runtime: run a fleet of parallel coding agents in isolated git worktrees... | [Compose](Apps/orca-server/docker-compose.yml) |
| **Paperclip** | `paperclip` | Paperclip is an open-source control plane for managing teams of AI agents, goals, budge... | [Compose](Apps/paperclip/docker-compose.yml) |
| **Ponos** | `ponos` | A harness around Claude Code that runs your tasks — code or not — from Notion or its ow... | [Compose](Apps/ponos/docker-compose.yml) |
| **Prozesswerk** | `prozesswerk` | Describe business processes in plain language and get editable BPMN 2 | [Compose](Apps/prozesswerk/docker-compose.yml) |
| **Reef Chain - Dev Cluster** | `reef-dev-cluster` | Self-contained Reef dev cluster with bootnode, validators, spec server, substrate RPC,... | [Compose](Apps/reef-dev-cluster/docker-compose.yml) |
| **Reef Chain - Keys Generator** | `reef-keygen` | Generates 3 Validators keys for a custom Reef Chain cluster | [Compose](Apps/reef-keygen/docker-compose.yml) |
| **Satgas** | `satgas` | Your own AI team, self-hosted | [Compose](Apps/satgas/docker-compose.yml) |
| **Seedance 2.5 Video Generator** | `emaki-video-starter` | One-page text-to-video and image-to-video web app on the Seedance 2 | [Compose](Apps/emaki-video-starter/docker-compose.yml) |
| **Sim** | `sim` | Open-source visual workflow builder for building and deploying AI agent workflows | [Compose](Apps/sim/docker-compose.yml) |
| **systemprompt** | `systemprompt` | Self-owned AI control plane: governance gateway for Claude, OpenAI, and Gemini with pol... | [Compose](Apps/systemprompt/docker-compose.yml) |
| **Tera Router** | `terarouter` | Self-hosted AI router: a single OpenAI/Anthropic-compatible gateway in front of all you... | [Compose](Apps/terarouter/docker-compose.yml) |
| **Typebot** | `typebot` | Typebot is an open-source chatbot builder platform | [Compose](Apps/typebot/docker-compose.yml) |
| **useSend** | `usesend` | Open source alternative to Resend, Sendgrid, Postmark etc | [Compose](Apps/usesend/docker-compose.yml) |
| **Wise MCP (unofficial)** | `wise-mcp` | Self-hosted MCP connector that lets Claude and ChatGPT read your Wise balances, card pa... | [Compose](Apps/wise-mcp/docker-compose.yml) |
| **Zeqqat** | `zeqqat` | Give AI agents access to your Dokploy without handing them your API key | [Compose](Apps/zeqqat/docker-compose.yml) |
### 📁 Finance (25 apps)

| App | Pasta | Descrição | Compose |
| :--- | :--- | :--- | :--- |
| **Actual Budget** | `actualbudget` | A super fast and privacy-focused app for managing your finances | [Compose](Apps/actualbudget/docker-compose.yml) |
| **Akaunting** | `akaunting` | Akaunting is a self-hosted, open-source accounting app for small businesses | [Compose](Apps/akaunting/docker-compose.yml) |
| **BigCapital** | `bigcapital` | BigCapital is a great open source alternative to QuickBooks | [Compose](Apps/bigcapital/docker-compose.yml) |
| **Billmora** | `billmora` | Billmora (Billing Management, Operation, and Recurring Automation) is a free, open-sour... | [Compose](Apps/billmora/docker-compose.yml) |
| **Budget Board** | `budget-board` | Self-hosted budgeting app with a web UI and a server backed by PostgreSQL | [Compose](Apps/budget-board/docker-compose.yml) |
| **Calibre** | `calibre` | Calibre is a comprehensive e-book management tool designed to organize, convert, and re... | [Compose](Apps/calibre/docker-compose.yml) |
| **DumbBudget** | `dumbbudget` | DumbBudget is a simple, self-hosted budget tracking service with PIN protection and no... | [Compose](Apps/dumbbudget/docker-compose.yml) |
| **Evershop** | `evershop` | Your All-in-One open source ecommerce solution | [Compose](Apps/evershop/docker-compose.yml) |
| **EZBookkeeping** | `ezbookkeeping` | EZBookkeeping is a self-hosted bookkeeping application that helps you manage your perso... | [Compose](Apps/ezbookkeeping/docker-compose.yml) |
| **Firefly III** | `firefly-iii` | Firefly III is a personal finance manager for tracking budgets and expenses | [Compose](Apps/firefly-iii/docker-compose.yml) |
| **Frappe Lending** | `frappe-lending` | A comprehensive loan management system built on Frappe Framework | [Compose](Apps/frappe-lending/docker-compose.yml) |
| **I Hate Money** | `ihatemoney` | I Hate Money is a web application for managing shared expenses among groups of people | [Compose](Apps/ihatemoney/docker-compose.yml) |
| **Inkvoice** | `inkvoice` | Open-source invoicing for freelancers and small teams: invoices, online payments (Strip... | [Compose](Apps/inkvoice/docker-compose.yml) |
| **InvoiceShelf** | `invoiceshelf` | InvoiceShelf is a self-hosted open source invoicing system for freelancers and small bu... | [Compose](Apps/invoiceshelf/docker-compose.yml) |
| **Kimai** | `kimai` | Kimai is a time-tracking app for freelancers and teams | [Compose](Apps/kimai/docker-compose.yml) |
| **Louez** | `louez` | Open-source equipment rental platform: a branded booking storefront with live availabil... | [Compose](Apps/louez/docker-compose.yml) |
| **Maybe** | `maybe` | Maybe is a self-hosted finance tracking application designed to simplify budgeting and... | [Compose](Apps/maybe/docker-compose.yml) |
| **OpenAlgo** | `openalgo` | OpenAlgo is an open-source algorithmic trading platform with a unified API layer across... | [Compose](Apps/openalgo/docker-compose.yml) |
| **OpenLMNP** | `openlmnp` | Self-hosted accounting for French furnished rentals (LMNP): depreciation schedules, rea... | [Compose](Apps/openlmnp/docker-compose.yml) |
| **Paymenter** | `paymenter` | Paymenter is a modern billing and payment management system for hosting providers, with... | [Compose](Apps/paymenter/docker-compose.yml) |
| **Pretix** | `pretix` | Ticket shop application for conferences, festivals, concerts, tech events, shows, works... | [Compose](Apps/pretix/docker-compose.yml) |
| **ShopNex** | `shopnex` | Open-source ecommerce platform with an admin, hosted checkout, storefront and Stripe pa... | [Compose](Apps/shopnex/docker-compose.yml) |
| **Shopware** | `shopware` | One-click Shopware 6 blueprint with bundled MySQL, Redis, bootstrap, init, worker, and... | [Compose](Apps/shopware/docker-compose.yml) |
| **Spliit** | `spliit` | Spliit is a lightweight, self-hosted alternative to Auth0 and Clerk | [Compose](Apps/spliit/docker-compose.yml) |
| **Wallos** | `wallos` | Wallos is a self-hosted subscription tracking application that helps you manage and mon... | [Compose](Apps/wallos/docker-compose.yml) |
### 📁 Social (22 apps)

| App | Pasta | Descrição | Compose |
| :--- | :--- | :--- | :--- |
| **Bonfire** | `bonfire` | Federated social networking toolkit for communities: customizable digital spaces with A... | [Compose](Apps/bonfire/docker-compose.yml) |
| **Chatto (single binary)** | `chatto` | A fully-featured real-time chat application for teams and communities | [Compose](Apps/chatto/docker-compose.yml) |
| **Chatwoot** | `chatwoot` | Chatwoot is an open-source customer support and engagement platform with a shared inbox... | [Compose](Apps/chatwoot/docker-compose.yml) |
| **Conduit** | `conduit` | Conduit is a simple, fast and reliable chat server powered by Matrix | [Compose](Apps/conduit/docker-compose.yml) |
| **Coral** | `coralproject` | Coral is a revolutionary commenting platform designed to enhance website interactions | [Compose](Apps/coralproject/docker-compose.yml) |
| **Discord Tickets** | `discord-tickets` | An open-source Discord bot for creating and managing support ticket channels | [Compose](Apps/discord-tickets/docker-compose.yml) |
| **Discourse** | `discourse` | Discourse is forum software for running online communities | [Compose](Apps/discourse/docker-compose.yml) |
| **Ethora Core** | `ethora-core` | Self-hosted chat and messaging server: API, web chat and admin panel, XMPP server (ejab... | [Compose](Apps/ethora-core/docker-compose.yml) |
| **Flarum** | `flarum` | Flarum is a delightfully simple, modern forum software | [Compose](Apps/flarum/docker-compose.yml) |
| **Fluxer** | `fluxer` | Fluxer is a self-hosted, scalable chat and community platform | [Compose](Apps/fluxer/docker-compose.yml) |
| **FreeScout** | `freescout` | FreeScout is a free open source help desk and shared inbox system | [Compose](Apps/freescout/docker-compose.yml) |
| **Lobe Chat** | `lobe-chat` | Lobe Chat - an open-source, modern-design AI chat framework | [Compose](Apps/lobe-chat/docker-compose.yml) |
| **Mattermost** | `mattermost` | Mattermost is a team chat platform and an alternative to Slack | [Compose](Apps/mattermost/docker-compose.yml) |
| **Mumble** | `mumble` | Mumble is an open-source, low-latency, high-quality voice chat software primarily inten... | [Compose](Apps/mumble/docker-compose.yml) |
| **Nebulynk** | `nebulynk` | Nebulynk is a self-hosted collaboration platform for teams with real-time messaging, fi... | [Compose](Apps/nebulynk/docker-compose.yml) |
| **Open WebUI** | `open-webui` | Open WebUI is an OpenSource ChatGPT-style chat interface for running AI models | [Compose](Apps/open-webui/docker-compose.yml) |
| **Rocketchat** | `rocketchat` | Rocket | [Compose](Apps/rocketchat/docker-compose.yml) |
| **Soketi** | `soketi` | Soketi is your simple, fast, and resilient open-source WebSockets server | [Compose](Apps/soketi/docker-compose.yml) |
| **Storyden** | `storyden` | With a fresh new take on traditional bulletin board forum software, Storyden is a moder... | [Compose](Apps/storyden/docker-compose.yml) |
| **Synapse** | `synapse` | Synapse is the reference homeserver implementation for Matrix, an open standard for sec... | [Compose](Apps/synapse/docker-compose.yml) |
| **Tuwunel** | `tuwunel` | High performance Matrix homeserver written in Rust | [Compose](Apps/tuwunel/docker-compose.yml) |
| **Zulip** | `zulip` | Open-source threaded team chat designed to keep team communication organized and produc... | [Compose](Apps/zulip/docker-compose.yml) |
### 📁 Developer (98 apps)

| App | Pasta | Descrição | Compose |
| :--- | :--- | :--- | :--- |
| **Adminer** | `adminer` | Adminer is a lightweight, web-based database management tool | [Compose](Apps/adminer/docker-compose.yml) |
| **Apprise API** | `apprise-api` | Apprise API provides a simple interface for sending notifications to almost all of the... | [Compose](Apps/apprise-api/docker-compose.yml) |
| **Appwrite** | `appwrite` | Appwrite is an end-to-end platform for building Web, Mobile, Native, or Backend apps, p... | [Compose](Apps/appwrite/docker-compose.yml) |
| **ArangoDB** | `arangodb` | ArangoDB is a native multi-model database with flexible data models for documents, grap... | [Compose](Apps/arangodb/docker-compose.yml) |
| **Autobase** | `autobase` | Autobase for PostgreSQL® is an open-source alternative to cloud-managed databases (self... | [Compose](Apps/autobase/docker-compose.yml) |
| **Baserow** | `baserow` | Baserow is an open source database management tool that allows you to create and manage... | [Compose](Apps/baserow/docker-compose.yml) |
| **Budibase** | `budibase` | Budibase is an open-source low-code platform that saves engineers 100s of hours buildin... | [Compose](Apps/budibase/docker-compose.yml) |
| **Bytebase** | `bytebase` | Bytebase is a database management tool that allows you to manage your databases with ease | [Compose](Apps/bytebase/docker-compose.yml) |
| **Cap.so** | `capso` | Cap | [Compose](Apps/capso/docker-compose.yml) |
| **ClickHouse** | `clickhouse` | ClickHouse is a fast, open-source columnar database built for real-time analytics | [Compose](Apps/clickhouse/docker-compose.yml) |
| **Cloud9** | `cloud9` | Cloud9 is a cloud-based integrated development environment (IDE) designed for developer... | [Compose](Apps/cloud9/docker-compose.yml) |
| **code-server** | `code-server` | code-server is a version of VS Code that runs in your browser | [Compose](Apps/code-server/docker-compose.yml) |
| **Convex** | `convex` | Convex is an open-source reactive database designed to make life easy for web app devel... | [Compose](Apps/convex/docker-compose.yml) |
| **CouchDB** | `couchdb` | CouchDB is a document-oriented NoSQL database that excels at replication and horizontal... | [Compose](Apps/couchdb/docker-compose.yml) |
| **Crawl4AI** | `crawl4ai` | Crawl4AI is a modern AI-powered web crawler with support for screenshots, PDFs, JavaScr... | [Compose](Apps/crawl4ai/docker-compose.yml) |
| **Crawlab (Master)** | `crawlab-master` | Crawlab is a distributed web crawler admin platform supporting multiple programming lan... | [Compose](Apps/crawlab-master/docker-compose.yml) |
| **Crawlab (Worker)** | `crawlab-worker` | Crawlab worker node for distributed web crawling | [Compose](Apps/crawlab-worker/docker-compose.yml) |
| **Cup** | `cup` | Cup is a self-hosted Docker container management UI | [Compose](Apps/cup/docker-compose.yml) |
| **Databasement** | `databasement` | Self-hosted database backup manager with a web UI | [Compose](Apps/databasement/docker-compose.yml) |
| **Docker Registry** | `registry` | Distribution implementation for storing and distributing of Docker container images and... | [Compose](Apps/registry/docker-compose.yml) |
| **Dockge** | `dockge` | Dockge is a web interface for managing Docker Compose stacks | [Compose](Apps/dockge/docker-compose.yml) |
| **Docling Serve** | `docling-serve` | Running Docling as an API service for document processing and conversion with AI-powere... | [Compose](Apps/docling-serve/docker-compose.yml) |
| **Dragonfly** | `dragonfly-db` | Dragonfly is a drop-in Redis replacement that is designed for heavy data workloads runn... | [Compose](Apps/dragonfly-db/docker-compose.yml) |
| **drizzle gateway** | `drizzle-gateway` | Drizzle Gateway is a self-hosted database gateway that allows you to connect to your da... | [Compose](Apps/drizzle-gateway/docker-compose.yml) |
| **Elasticsearch** | `elastic-search` | Elasticsearch is an open-source search and analytics engine, used for full-text search... | [Compose](Apps/elastic-search/docker-compose.yml) |
| **Evolution API** | `evolutionapi` | Evolution API is a robust platform dedicated to empowering small businesses with limite... | [Compose](Apps/evolutionapi/docker-compose.yml) |
| **Evolution API (Almog Cohen fork)** | `almog-evolution-api` | Unofficial Evolution API 2 | [Compose](Apps/almog-evolution-api/docker-compose.yml) |
| **Evolution GO** | `evolutiongo` | Evolution Go is a high-performance implementation of the WhatsApp API, written in Go | [Compose](Apps/evolutiongo/docker-compose.yml) |
| **FalkorDB** | `falkordb` | A high-performance graph database for knowledge graphs, GraphRAG, agent memory, fraud d... | [Compose](Apps/falkordb/docker-compose.yml) |
| **Feedbacks** | `feedbacks` | Self-hosted website feedback, browser evidence and MCP handoff for coding assistants | [Compose](Apps/feedbacks/docker-compose.yml) |
| **Firecrawl** | `firecrawl` | Production-ready, authenticated Firecrawl with persistent queues, browser rendering, a... | [Compose](Apps/firecrawl/docker-compose.yml) |
| **Gel** | `gel` | Gel is a next-generation graph-relational database (formerly EdgeDB) with a built-in mi... | [Compose](Apps/gel/docker-compose.yml) |
| **Gitea (MySQL)** | `gitea-mysql` | Gitea bundled with MySQL 8 | [Compose](Apps/gitea-mysql/docker-compose.yml) |
| **Gitea (PostgreSQL)** | `gitea-postgres` | Gitea is a lightweight Git service for hosting code repositories | [Compose](Apps/gitea-postgres/docker-compose.yml) |
| **Gitea (SQLite)** | `gitea-sqlite` | Self-hosted Git service using SQLite for a simple one-container setup | [Compose](Apps/gitea-sqlite/docker-compose.yml) |
| **Gitea Mirror** | `gitea-mirror` | Gitea Mirror is a modern web app for automatically mirroring repositories from GitHub t... | [Compose](Apps/gitea-mirror/docker-compose.yml) |
| **GitLab CE** | `gitlab-ce` | GitLab CE is a platform for Git repositories, CI/CD, and project management | [Compose](Apps/gitlab-ce/docker-compose.yml) |
| **Gotenberg** | `gotenberg` | Gotenberg is a Docker-powered stateless API for PDF files | [Compose](Apps/gotenberg/docker-compose.yml) |
| **Grist** | `grist` | Grist is an open-source spreadsheet and database alternative that combines the flexibil... | [Compose](Apps/grist/docker-compose.yml) |
| **Harbor** | `harbor` | Harbor is an open source container and OCI artifact registry with access control and Tr... | [Compose](Apps/harbor/docker-compose.yml) |
| **Hoppscotch (AIO + Migrations)** | `hoppscotch` | Hoppscotch Community Edition (All-in-One) with automatic database migrations | [Compose](Apps/hoppscotch/docker-compose.yml) |
| **InstantDB** | `instantdb` | InstantDB is a real-time database server that provides instant data synchronization and... | [Compose](Apps/instantdb/docker-compose.yml) |
| **IT Tools** | `it-tools` | A collection of handy online it-tools for developers | [Compose](Apps/it-tools/docker-compose.yml) |
| **jenkins** | `jenkins` | Jenkins is an open-source automation server for building CI/CD pipelines | [Compose](Apps/jenkins/docker-compose.yml) |
| **KeyDB** | `keydb` | KeyDB is a high-performance fork of Redis with multithreading, active replication, and... | [Compose](Apps/keydb/docker-compose.yml) |
| **KiviDB** | `kividb` | KiviDB is a Redis-compatible in-memory database written in Rust, with full-text and vec... | [Compose](Apps/kividb/docker-compose.yml) |
| **LanguageTool** | `languagetool` | LanguageTool is an open-source grammar, spelling, and style checker | [Compose](Apps/languagetool/docker-compose.yml) |
| **LFSX** | `lfsx` | Self-hosted Git LFS server that keeps large binaries off your forge's metered storage | [Compose](Apps/lfsx/docker-compose.yml) |
| **LibreDB Studio** | `libredb-studio` | The open-source SQL IDE you host yourself | [Compose](Apps/libredb-studio/docker-compose.yml) |
| **LibreTranslate** | `libretranslate` | LibreTranslate is a free and open-source machine translation API, powered by Argos Tran... | [Compose](Apps/libretranslate/docker-compose.yml) |
| **Logto** | `logto` | Logto is an open-source Identity and Access Management (IAM) platform designed to strea... | [Compose](Apps/logto/docker-compose.yml) |
| **Lowcoder** | `lowcoder` | Rapid business App Builder for Everyone | [Compose](Apps/lowcoder/docker-compose.yml) |
| **Meilisearch** | `meilisearch` | Meilisearch is a free and open-source search engine that allows you to easily add searc... | [Compose](Apps/meilisearch/docker-compose.yml) |
| **Metabase** | `metabase` | Metabase is an open-source business intelligence tool for exploring and visualizing data | [Compose](Apps/metabase/docker-compose.yml) |
| **Minepanel** | `minepanel` | Web panel for managing Minecraft servers with Docker | [Compose](Apps/minepanel/docker-compose.yml) |
| **MuleSoft ESB Runtime Community Edition** | `mulesoft-esb` | MuleSoft ESB Runtime  is a lightweight, Java-based integration platform that allows you... | [Compose](Apps/mulesoft-esb/docker-compose.yml) |
| **NocoDB** | `nocodb` | NocoDB is an open-source alternative to Airtable that turns your database into a smart... | [Compose](Apps/nocodb/docker-compose.yml) |
| **NTFY** | `ntfy` | ntfy lets you send push notifications to your phone or desktop via scripts from any com... | [Compose](Apps/ntfy/docker-compose.yml) |
| **Obsidian LiveSync** | `obsidian-livesync` | Obsidian LiveSync with CouchDB for real-time note synchronization | [Compose](Apps/obsidian-livesync/docker-compose.yml) |
| **Open Journal Systems** | `ojs` | Open Journal Systems (OJS) is a journal management and publishing system that has been... | [Compose](Apps/ojs/docker-compose.yml) |
| **OpenGist** | `opengist` | OpenGist is a self-hosted pastebin alternative | [Compose](Apps/opengist/docker-compose.yml) |
| **Openobserve** | `openobserve` | OpenObserve (O2) is a cloud-native observability platform that unifies logs, metrics, a... | [Compose](Apps/openobserve/docker-compose.yml) |
| **OpenWA** | `openwa` | OpenWA is a free, self-hosted WhatsApp API gateway with a REST API, webhooks, multi-ses... | [Compose](Apps/openwa/docker-compose.yml) |
| **Parseable** | `parseable` | Fast observability and log analytics platform on object storage | [Compose](Apps/parseable/docker-compose.yml) |
| **PeerDB** | `peerdb` | Data integration platform that synchronizes and federates data across databases with a... | [Compose](Apps/peerdb/docker-compose.yml) |
| **Peppermint** | `peppermint` | Peppermint is a modern, open-source API development platform that helps you build, test... | [Compose](Apps/peppermint/docker-compose.yml) |
| **pgAdmin** | `pgadmin` | pgAdmin is an administration and management tool for PostgreSQL databases | [Compose](Apps/pgadmin/docker-compose.yml) |
| **Phpmyadmin** | `phpmyadmin` | phpMyAdmin is an open-source web interface for managing MySQL and MariaDB databases | [Compose](Apps/phpmyadmin/docker-compose.yml) |
| **PocketBase** | `pocketbase` | Open Source backend in 1 file | [Compose](Apps/pocketbase/docker-compose.yml) |
| **Portabase** | `portabase` | A free, open-source and self-hosted tool from a non-profit organization that helps you... | [Compose](Apps/portabase/docker-compose.yml) |
| **PostgreSQL + pgAdmin** | `postgres-pgadmin` | PostgreSQL 18 Alpine with pgAdmin 4 web UI, persistent volumes and healthchecks for eas... | [Compose](Apps/postgres-pgadmin/docker-compose.yml) |
| **PostgreSQL with 80+ Extensions** | `postgres-extensor` | The official PostgreSQL 18 image with 80+ tested extensions preinstalled: pgvector, Pos... | [Compose](Apps/postgres-extensor/docker-compose.yml) |
| **PostgreSQL with PgDog** | `postgres-pgdog` | PostgreSQL database with PgDog connection pooler, load balancer, and horizontal scaling... | [Compose](Apps/postgres-pgdog/docker-compose.yml) |
| **PowerSync** | `powersync` | PowerSync is a sync engine for local-first apps | [Compose](Apps/powersync/docker-compose.yml) |
| **Qdrant** | `qdrant` | An open-source vector database designed for high-performance similarity search and stor... | [Compose](Apps/qdrant/docker-compose.yml) |
| **Quant-UX** | `quant-ux` | Quant-UX is an open-source UX design and prototyping tool that allows you to create int... | [Compose](Apps/quant-ux/docker-compose.yml) |
| **RabbitMQ** | `rabbitmq` | RabbitMQ is an open source multi-protocol messaging broker | [Compose](Apps/rabbitmq/docker-compose.yml) |
| **SearXNG** | `searxng` | SearXNG is a privacy-respecting metasearch engine that combines results from many searc... | [Compose](Apps/searxng/docker-compose.yml) |
| **Seq** | `seq` | Seq is a self-hosted search, analysis, and alerting server for structured application l... | [Compose](Apps/seq/docker-compose.yml) |
| **Silex** | `silex` | Silex is a free and open-source website builder for professional designers | [Compose](Apps/silex/docker-compose.yml) |
| **Soft Serve** | `soft-serve` | Soft Serve is a self-hosted Git server with an SSH TUI, HTTP Git access, Git LFS suppor... | [Compose](Apps/soft-serve/docker-compose.yml) |
| **SpacetimeDB** | `spacetimedb` | SpacetimeDB is a relational database with a built-in server runtime | [Compose](Apps/spacetimedb/docker-compose.yml) |
| **Strapi** | `strapi` | Strapi is an open-source headless CMS for building APIs and managing content | [Compose](Apps/strapi/docker-compose.yml) |
| **SupaBase** | `pre0.22.5-supabase` | The open source Firebase alternative | [Compose](Apps/pre0.22.5-supabase/docker-compose.yml) |
| **SupaBase** | `supabase` | Supabase is a Postgres-based backend platform and an open-source alternative to Firebase | [Compose](Apps/supabase/docker-compose.yml) |
| **SurrealDB** | `surrealdb` | SurrealDB is a native, open-source, multi-model database that lets you store and manage... | [Compose](Apps/surrealdb/docker-compose.yml) |
| **teable** | `teable` | Teable is a Super fast, Real-time, Professional, Developer friendly, No-code database b... | [Compose](Apps/teable/docker-compose.yml) |
| **TimescaleDB** | `timescaledb` | TimescaleDB is an open-source time-series database packaged as a PostgreSQL extension,... | [Compose](Apps/timescaledb/docker-compose.yml) |
| **TrailBase** | `trailbase` | TrailBase is a blazingly fast, open-source application server with type-safe APIs, buil... | [Compose](Apps/trailbase/docker-compose.yml) |
| **Typesense** | `typesense` | Typesense is a fast, open-source search engine for building modern search experiences | [Compose](Apps/typesense/docker-compose.yml) |
| **Valkey** | `valkey` | Valkey is an open-source fork of Redis, backed by AWS and the Linux Foundation | [Compose](Apps/valkey/docker-compose.yml) |
| **Velix API** | `velix-api` | Self-hosted WhatsApp API with multi-instance support, webhooks, n8n node, and Chatwoot... | [Compose](Apps/velix-api/docker-compose.yml) |
| **Wakapi** | `wakapi` | Wakapi is a self-hosted WakaTime-compatible backend for tracking coding activity and de... | [Compose](Apps/wakapi/docker-compose.yml) |
| **Wanderer** | `wanderer` | Wanderer is a self-hosted mapping and geolocation platform powered by Meilisearch, Pock... | [Compose](Apps/wanderer/docker-compose.yml) |
| **Waxum** | `waxum` | Waxum is a WhatsApp REST API gateway written in Rust, shipped as a single native binary | [Compose](Apps/waxum/docker-compose.yml) |
| **WhatsApp API Multi Device Version** | `go-whatsapp-web-multidevice` | WhatsApp API Multi Device Version the open-source, self-hosted whatsapp api | [Compose](Apps/go-whatsapp-web-multidevice/docker-compose.yml) |
| **WuzAPI** | `wuzapi` | A RESTful API service for WhatsApp with multiple device support and concurrent sessions | [Compose](Apps/wuzapi/docker-compose.yml) |
| **Zitadel** | `zitadel` | Open-source identity and access management platform with multi-tenancy, OpenID Connect,... | [Compose](Apps/zitadel/docker-compose.yml) |
### 📁 Others (99 apps)

| App | Pasta | Descrição | Compose |
| :--- | :--- | :--- | :--- |
| **AdventureLog** | `adventurelog` | AdventureLog is an open-source activity tracker with maps, journaling, and Strava integ... | [Compose](Apps/adventurelog/docker-compose.yml) |
| **AnonUpload** | `anonupload` | AnonUpload is a secure, anonymous file sharing application that does not require a data... | [Compose](Apps/anonupload/docker-compose.yml) |
| **Answer** | `answer` | Answer is an open-source Q&A platform for building a self-hosted question-and-answer se... | [Compose](Apps/answer/docker-compose.yml) |
| **Anubis** | `anubis` | Anubis is a bot protector, It will block bots from accessing your website | [Compose](Apps/anubis/docker-compose.yml) |
| **Anytype** | `anytype` | Anytype is a private, offline-first app for notes and personal knowledge | [Compose](Apps/anytype/docker-compose.yml) |
| **AzerothCore** | `azerothcore` | A modular open source World of Warcraft: Wrath of the Lich King 3 | [Compose](Apps/azerothcore/docker-compose.yml) |
| **BabyBuddy** | `babybuddy` | BabyBuddy is a comprehensive, user-friendly platform designed to help parents and careg... | [Compose](Apps/babybuddy/docker-compose.yml) |
| **Backrest** | `backrest` | Backrest is a web-based backup solution powered by restic, offering an intuitive WebUI... | [Compose](Apps/backrest/docker-compose.yml) |
| **Barrage** | `barrage` | Barrage is a minimalistic Deluge WebUI app with full mobile support | [Compose](Apps/barrage/docker-compose.yml) |
| **Bazarr** | `bazarr` | Bazarr is a companion application to Sonarr and Radarr that manages and downloads subti... | [Compose](Apps/bazarr/docker-compose.yml) |
| **Blender** | `blender` | Blender is a free and open-source 3D creation suite | [Compose](Apps/blender/docker-compose.yml) |
| **Bluesky PDS** | `bluesky-pds` | Bluesky PDS is a personal data server for Bluesky | [Compose](Apps/bluesky-pds/docker-compose.yml) |
| **Borgitory** | `borgitory` | A web interface for managing BorgBackup archives | [Compose](Apps/borgitory/docker-compose.yml) |
| **Bugsink** | `bugsink` | Bugsink is a self-hosted Error Tracker | [Compose](Apps/bugsink/docker-compose.yml) |
| **CakePHP 5** | `cakephp` | CakePHP 5 starter app running on the themusicdev/php-apache 8 | [Compose](Apps/cakephp/docker-compose.yml) |
| **Calcom** | `calcom` | Cal | [Compose](Apps/calcom/docker-compose.yml) |
| **Chevereto** | `chevereto` | Chevereto is a powerful, self-hosted image and video hosting platform designed for indi... | [Compose](Apps/chevereto/docker-compose.yml) |
| **Chief-Onboarding** | `chiefonboarding` | Chief-Onboarding is a comprehensive, self-hosted onboarding and employee management pla... | [Compose](Apps/chiefonboarding/docker-compose.yml) |
| **Chromium** | `chromium` | Chromium is an open-source browser project that is designed to provide a safer, faster,... | [Compose](Apps/chromium/docker-compose.yml) |
| **Cloud Commander** | `cloudcommander` | Cloud Commander is a file manager for the web | [Compose](Apps/cloudcommander/docker-compose.yml) |
| **Coder** | `coder` | Coder is an open-source cloud development environment (CDE) that you host in your cloud... | [Compose](Apps/coder/docker-compose.yml) |
| **Commento** | `commento` | Commento is a comments widget designed to enhance the interaction on your website | [Compose](Apps/commento/docker-compose.yml) |
| **Commento++** | `commentoplusplus` | Commento++ is a free, open-source application designed to provide a fast, lightweight c... | [Compose](Apps/commentoplusplus/docker-compose.yml) |
| **CookieCloud** | `cookie-cloud` | CookieCloud lets you sync and manage browser cookies across devices securely using a se... | [Compose](Apps/cookie-cloud/docker-compose.yml) |
| **Cut** | `cut` | A tiny, self-hosted URL shortener — short links that are entirely yours, with per-link... | [Compose](Apps/cut/docker-compose.yml) |
| **Databasus** | `databasus` | Free, open source and self-hosted tool to backup PostgreSQL, MySQL, MariaDB and MongoDB | [Compose](Apps/databasus/docker-compose.yml) |
| **Didacta** | `didacta` | Didacta is a fair-code, self-hosted learning platform (LMS) with multi-tenant isolation... | [Compose](Apps/didacta/docker-compose.yml) |
| **Directory Lister** | `directory-lister` | Directory Lister is a simple PHP application that lists the contents of any web-accessi... | [Compose](Apps/directory-lister/docker-compose.yml) |
| **Docmost** | `docmost` | Docmost is a collaborative wiki and documentation tool | [Compose](Apps/docmost/docker-compose.yml) |
| **Documenso** | `documenso` | Documenso is the open source alternative to DocuSign for signing documents digitally | [Compose](Apps/documenso/docker-compose.yml) |
| **Docuseal** | `docuseal` | Docuseal is a self-hosted document management system | [Compose](Apps/docuseal/docker-compose.yml) |
| **draw.io** | `drawio` | draw | [Compose](Apps/drawio/docker-compose.yml) |
| **Drawnix** | `drawnix` | Drawnix is an application for generating and managing visual content, powered by pubuzh... | [Compose](Apps/drawnix/docker-compose.yml) |
| **DumbAssets** | `dumbassets` | DumbAssets is a simple, self-hosted asset tracking service with no database or authenti... | [Compose](Apps/dumbassets/docker-compose.yml) |
| **DumbDrop** | `dumbdrop` | DumbDrop is a simple, self-hosted file sharing service with no database or authenticati... | [Compose](Apps/dumbdrop/docker-compose.yml) |
| **DumbPad** | `dumbpad` | DumbPad is a simple, self-hosted notepad service with PIN protection and no database re... | [Compose](Apps/dumbpad/docker-compose.yml) |
| **Duplicati** | `duplicati` | Duplicati is a free, open-source backup solution that offers zero-trust, fully encrypte... | [Compose](Apps/duplicati/docker-compose.yml) |
| **Easy!Appointments** | `easyappointments` | Easy!Appointments is a highly customizable web application that allows customers to boo... | [Compose](Apps/easyappointments/docker-compose.yml) |
| **Enshrouded** | `enshrouded` | Enshrouded steam dedicated server | [Compose](Apps/enshrouded/docker-compose.yml) |
| **Etherpad** | `etherpad` | Etherpad is a real-time collaborative text editor that allows multiple users to edit do... | [Compose](Apps/etherpad/docker-compose.yml) |
| **Excalidraw** | `excalidraw` | Excalidraw is an open-source whiteboard tool for sketching hand-drawn-style diagrams | [Compose](Apps/excalidraw/docker-compose.yml) |
| **Excaliself** | `excaliself` | Self-hosted, open-source alternative to Excalidraw+ for teams | [Compose](Apps/excaliself/docker-compose.yml) |
| **Fider** | `fider` | Fider is an open-source feedback portal for collecting, discussing, and prioritizing fe... | [Compose](Apps/fider/docker-compose.yml) |
| **Filestash** | `filestash` | Filestash is the enterprise-grade file manager connecting your storage with your identi... | [Compose](Apps/filestash/docker-compose.yml) |
| **FiveM Server** | `fivem` | A modded GTA V multiplayer server with optional txAdmin web interface for easy server m... | [Compose](Apps/fivem/docker-compose.yml) |
| **Flagsmith** | `flagsmith` | Flagsmith is an open-source feature flagging and remote config service | [Compose](Apps/flagsmith/docker-compose.yml) |
| **Fonoster** | `fonoster` | Fonoster is an open-source alternative to Twilio | [Compose](Apps/fonoster/docker-compose.yml) |
| **Frappe HR** | `frappe-hr` | Feature rich HR & Payroll software | [Compose](Apps/frappe-hr/docker-compose.yml) |
| **Frappe LMS** | `frappe-lms` | Easy to use, open source learning management system to structure courses and reach out... | [Compose](Apps/frappe-lms/docker-compose.yml) |
| **GeoServer & PostGIS** | `geoserver` | An open-source server for sharing geospatial data, paired with a PostGIS database | [Compose](Apps/geoserver/docker-compose.yml) |
| **Glitchtip** | `glitchtip` | Glitchtip is simple, open source error tracking | [Compose](Apps/glitchtip/docker-compose.yml) |
| **Gotify** | `gotify` | Gotify is a simple server for sending and receiving self-hosted push notifications | [Compose](Apps/gotify/docker-compose.yml) |
| **Hi.events** | `hi-events` | Hi | [Compose](Apps/hi-events/docker-compose.yml) |
| **Hydrodactyl** | `hydrodactyl` | Hydrodactyl is a modern, performance-focused game server management panel forked from P... | [Compose](Apps/hydrodactyl/docker-compose.yml) |
| **Infisical** | `infisical` | All-in-one platform to securely manage application configuration and secrets across you... | [Compose](Apps/infisical/docker-compose.yml) |
| **Java Runtime (Multi-Version)** | `java` | Configurable Java runtime environment supporting versions 8, 11, 16, 17, and 21 | [Compose](Apps/java/docker-compose.yml) |
| **Kaneo** | `kaneo` | Kaneo - an open source project management platform focused on simplicity and efficiency | [Compose](Apps/kaneo/docker-compose.yml) |
| **Kutt** | `kutt` | Kutt is a modern URL shortener with support for custom domains | [Compose](Apps/kutt/docker-compose.yml) |
| **Lavalink** | `lavalink` | Lavalink is an open source standalone audio sending node based on Lavaplayer | [Compose](Apps/lavalink/docker-compose.yml) |
| **Linkding** | `linkding` | Linkding is a self-hosted bookmark manager with a clean and simple interface | [Compose](Apps/linkding/docker-compose.yml) |
| **Lodestone** | `lodestone` | A free, open source server hosting tool for Minecraft and other multiplayers games | [Compose](Apps/lodestone/docker-compose.yml) |
| **MacOS (dockerized)** | `macos` | MacOS inside a Docker container | [Compose](Apps/macos/docker-compose.yml) |
| **Mage AI** | `mage-ai` | Build, run, and manage data pipelines for integrating and transforming data | [Compose](Apps/mage-ai/docker-compose.yml) |
| **MC Controller** | `mc-controller` | A self-hosted Minecraft control panel for creating and managing multiple Vanilla, Fabri... | [Compose](Apps/mc-controller/docker-compose.yml) |
| **MCSManager** | `mcsmanager` | A modern dashboard for managing Minecraft servers | [Compose](Apps/mcsmanager/docker-compose.yml) |
| **Morphos** | `morphos` | Morphos is a lightweight service for distributed operations and orchestration | [Compose](Apps/morphos/docker-compose.yml) |
| **NaviServer** | `naviserver` | A lightweight Minecraft server manager with a web interface, CLI, automatic JVM managem... | [Compose](Apps/naviserver/docker-compose.yml) |
| **Neko** | `neko` | Neko is a self-hosted virtual browser that runs in Docker and allows you to share brows... | [Compose](Apps/neko/docker-compose.yml) |
| **Nextcloud** | `nextcloud-aio` | Nextcloud is a self-hosted file storage and sync platform with powerful collaboration c... | [Compose](Apps/nextcloud-aio/docker-compose.yml) |
| **Nginx** | `nginx` | Nginx is a high-performance web server and reverse proxy | [Compose](Apps/nginx/docker-compose.yml) |
| **Omni-Tools** | `omni-tools` | Omni-Tools is a collection of useful tools in a single self-hosted web application | [Compose](Apps/omni-tools/docker-compose.yml) |
| **OneDev** | `onedev` | Git server with CI/CD, kanban, and packages | [Compose](Apps/onedev/docker-compose.yml) |
| **Ontime** | `ontime` | Ontime is browser-based application that manages event rundowns, scheduliing and cuing | [Compose](Apps/ontime/docker-compose.yml) |
| **Open Design** | `open-design` | Open Design is a local-first, open-source design tool with native desktop apps, a large... | [Compose](Apps/open-design/docker-compose.yml) |
| **PairDrop** | `pairdrop` | PairDrop is a self-hosted local file sharing web app for sending files and text between... | [Compose](Apps/pairdrop/docker-compose.yml) |
| **Palmr** | `palmr` | Palmr the open-source, self-hosted alternative to WeTransfer | [Compose](Apps/palmr/docker-compose.yml) |
| **Penpot** | `penpot` | Penpot is the web-based open-source design tool that bridges the gap between designers... | [Compose](Apps/penpot/docker-compose.yml) |
| **Postgresus** | `postgresus` | Deprecated: the project was renamed to Databasus, use the Databasus template instead | [Compose](Apps/postgresus/docker-compose.yml) |
| **PrivateBin** | `privatebin` | PrivateBin is a minimalist, open-source online pastebin where the server has zero knowl... | [Compose](Apps/privatebin/docker-compose.yml) |
| **Pterodactyl** | `pterodactyl` | A free, open-source game server management panel | [Compose](Apps/pterodactyl/docker-compose.yml) |
| **Pyrodactyl** | `pyrodactyl` | Pyrodactyl is the Pterodactyl-based game server panel that's faster, smaller, safer, an... | [Compose](Apps/pyrodactyl/docker-compose.yml) |
| **qBittorrent** | `qbittorrent` | qBittorrent is an open-source BitTorrent client you can control from a web interface | [Compose](Apps/qbittorrent/docker-compose.yml) |
| **Rallly** | `rallly` | Rallly is an open-source scheduling and collaboration tool for organizing events and me... | [Compose](Apps/rallly/docker-compose.yml) |
| **ruTorrent** | `rutorrent` | ruTorrent + rTorrent BitTorrent client (crazy-max image) | [Compose](Apps/rutorrent/docker-compose.yml) |
| **Shlink** | `shlink` | URL shortener that can be used to serve shortened URLs under your own domain | [Compose](Apps/shlink/docker-compose.yml) |
| **Snipe-IT** | `snipe-it` | Snipe-IT is an open-source IT asset management system for tracking hardware, software l... | [Compose](Apps/snipe-it/docker-compose.yml) |
| **Struxa** | `struxa` | Struxa is a self-hosted, open-source server management panel — a modern, fully typed re... | [Compose](Apps/struxa/docker-compose.yml) |
| **Syncthing** | `syncthing` | Syncthing keeps your devices and files continuously in sync | [Compose](Apps/syncthing/docker-compose.yml) |
| **Tolgee** | `tolgee` | Developer & translator friendly web-based localization platform | [Compose](Apps/tolgee/docker-compose.yml) |
| **Tooljet** | `tooljet` | Tooljet is an open-source low-code platform that allows you to build internal tools qui... | [Compose](Apps/tooljet/docker-compose.yml) |
| **Trigger.dev** | `triggerdotdev` | Trigger is a platform for building event-driven applications | [Compose](Apps/triggerdotdev/docker-compose.yml) |
| **TRMNL LaraPaper** | `trmnl-larapaper` | LaraPaper is a self-hosted application (BYOS) to manage TRMNL e-ink devices | [Compose](Apps/trmnl-larapaper/docker-compose.yml) |
| **Unleash** | `unleash` | Open-source feature management platform | [Compose](Apps/unleash/docker-compose.yml) |
| **Vaultwarden** | `vaultwarden` | Vaultwarden is a lightweight password manager that works with Bitwarden apps | [Compose](Apps/vaultwarden/docker-compose.yml) |
| **Verdaccio** | `verdaccio` | A lightweight Node | [Compose](Apps/verdaccio/docker-compose.yml) |
| **Weblate** | `weblate` | Weblate is a libre web-based continuous localization platform with tight version contro... | [Compose](Apps/weblate/docker-compose.yml) |
| **Windows (dockerized)** | `windows` | Windows inside a Docker container | [Compose](Apps/windows/docker-compose.yml) |
| **XSSHunter** | `xsshunter` | XSSHunter is an open-source platform designed to identify and exploit blind Cross-Site... | [Compose](Apps/xsshunter/docker-compose.yml) |
| **YOURLS** | `yourls` | YOURLS (Your Own URL Shortener) is a set of PHP scripts that will allow you to run your... | [Compose](Apps/yourls/docker-compose.yml) |


---

Feito com ❤️ pela comunidade para o ecossistema ZimaOS / CasaOS.
