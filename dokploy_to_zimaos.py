#!/usr/bin/env python3
"""
dokploy_to_zimaos.py — Converte o catálogo de templates do Dokploy
(https://github.com/Dokploy/templates) para o formato da Loja de Apps do ZimaOS
(compatível com protocolo v2 e ZIP legado v1).

Uso rápido:
    pip install pyyaml
    python3 dokploy_to_zimaos.py --clone --output ./zimaos-dokploy-store --zip

Ou usando um clone local já existente:
    python3 dokploy_to_zimaos.py --source ./templates --output ./zimaos-dokploy-store --zip
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import json
import re
import secrets
import shutil
import string
import subprocess
import sys
import time
import uuid
import zipfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import tomllib  # Python 3.11+
except ImportError:  # pragma: no cover
    try:
        import tomli as tomllib  # type: ignore
    except ImportError:
        sys.exit("Erro: requer Python 3.11+ (tomllib nativo) ou 'pip install tomli'.")

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("Erro: instale PyYAML com 'pip install pyyaml'.")


DOKPLOY_REPO_URL = "https://github.com/Dokploy/templates.git"

# Categorias oficiais do protocolo v2 da loja do ZimaOS
# Ref: https://www.zimaspace.com/docs/developer/app-store-compose-x-casaos
ZIMAOS_V2_CATEGORIES = [
    "Media",
    "Productivity",
    "Home",
    "Networking",
    "AI",
    "Finance",
    "Social",
    "Developer",
    "Others",
]

# Mapeamento de tags do Dokploy -> categoria oficial v2 do ZimaOS
TAG_TO_CATEGORY: dict[str, str] = {
    # AI
    "ai": "AI",
    "llm": "AI",
    "ml": "AI",
    "machine-learning": "AI",
    "chatbot": "AI",
    "openai": "AI",
    "rag": "AI",
    "agents": "AI",
    "vector-database": "AI",
    # Media
    "media": "Media",
    "video": "Media",
    "audio": "Media",
    "music": "Media",
    "streaming": "Media",
    "photos": "Media",
    "gallery": "Media",
    "books": "Media",
    "ebooks": "Media",
    "podcast": "Media",
    "iptv": "Media",
    "plex": "Media",
    "jellyfin": "Media",
    # Productivity
    "productivity": "Productivity",
    "notes": "Productivity",
    "wiki": "Productivity",
    "knowledge": "Productivity",
    "docs": "Productivity",
    "documentation": "Productivity",
    "cms": "Productivity",
    "blog": "Productivity",
    "wordpress": "Productivity",
    "project-management": "Productivity",
    "kanban": "Productivity",
    "tasks": "Productivity",
    "calendar": "Productivity",
    "forms": "Productivity",
    "bookmarks": "Productivity",
    "files": "Productivity",
    "storage": "Productivity",
    "cloud": "Productivity",
    "office": "Productivity",
    "pdf": "Productivity",
    "mail": "Productivity",
    "email": "Productivity",
    "crm": "Productivity",
    "erp": "Productivity",
    "rss": "Productivity",
    "automation": "Productivity",
    "workflow": "Productivity",
    # Home
    "home": "Home",
    "home-automation": "Home",
    "iot": "Home",
    "smart-home": "Home",
    "recipes": "Home",
    "fitness": "Home",
    "health": "Home",
    # Networking
    "network": "Networking",
    "networking": "Networking",
    "vpn": "Networking",
    "proxy": "Networking",
    "reverse-proxy": "Networking",
    "dns": "Networking",
    "security": "Networking",
    "auth": "Networking",
    "authentication": "Networking",
    "sso": "Networking",
    "firewall": "Networking",
    "tunnel": "Networking",
    "monitoring": "Networking",
    "uptime": "Networking",
    "status": "Networking",
    "analytics": "Networking",
    # Finance
    "finance": "Finance",
    "accounting": "Finance",
    "billing": "Finance",
    "invoicing": "Finance",
    "budget": "Finance",
    "crypto": "Finance",
    "ecommerce": "Finance",
    "e-commerce": "Finance",
    "shop": "Finance",
    "payments": "Finance",
    # Social
    "social": "Social",
    "chat": "Social",
    "messaging": "Social",
    "forum": "Social",
    "community": "Social",
    "fediverse": "Social",
    "matrix": "Social",
    "support": "Social",
    "helpdesk": "Social",
    # Developer
    "developer": "Developer",
    "devops": "Developer",
    "database": "Developer",
    "databases": "Developer",
    "sql": "Developer",
    "nosql": "Developer",
    "cache": "Developer",
    "queue": "Developer",
    "git": "Developer",
    "ci-cd": "Developer",
    "cicd": "Developer",
    "code": "Developer",
    "ide": "Developer",
    "api": "Developer",
    "backend": "Developer",
    "baas": "Developer",
    "docker": "Developer",
    "containers": "Developer",
    "logging": "Developer",
    "observability": "Developer",
    "metrics": "Developer",
    "tracing": "Developer",
    "search": "Developer",
    "testing": "Developer",
    "low-code": "Developer",
    "no-code": "Developer",
    "headless": "Developer",
    "webhooks": "Developer",
    "registry": "Developer",
}

HELPER_PATTERN = re.compile(r"\$\{([^{}]+)\}")
ENV_REF_PATTERN = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)(?::-[^}]*)?\}")

# Serviços auxiliares comuns que NÃO devem ser escolhidos como x-casaos.main
NON_MAIN_SERVICE_HINTS = (
    "postgres",
    "postgresql",
    "mysql",
    "mariadb",
    "mongo",
    "mongodb",
    "redis",
    "valkey",
    "dragonfly",
    "memcached",
    "rabbitmq",
    "kafka",
    "zookeeper",
    "clickhouse",
    "elasticsearch",
    "meilisearch",
    "typesense",
    "minio",
    "worker",
    "scheduler",
    "cron",
    "migrate",
    "init",
    "db",
)


class QuotedString(str):
    """Força aspas duplas no YAML (obrigatório para x-casaos.port_map e version)."""


def _quoted_str_representer(dumper: yaml.SafeDumper, data: QuotedString) -> Any:
    return dumper.represent_scalar("tag:yaml.org,2002:str", str(data), style='"')


class ZimaOSDumper(yaml.SafeDumper):
    pass


ZimaOSDumper.add_representer(QuotedString, _quoted_str_representer)


def slugify_app_id(raw_id: str) -> str:
    cleaned = re.sub(r"[^a-z0-9_-]+", "-", raw_id.strip().lower()).strip("-")
    return cleaned or "app"


def folder_name_from_id(raw_id: str, display_name: str | None = None) -> str:
    base = raw_id.strip() or (display_name or "app")
    cleaned = re.sub(r"[^a-zA-Z0-9._-]+", "-", base).strip("-")
    return cleaned or "app"


def map_category(tags: list[str] | None) -> str:
    if not tags:
        return "Others"
    for tag in tags:
        key = str(tag).strip().lower()
        if key in TAG_TO_CATEGORY:
            return TAG_TO_CATEGORY[key]
        for k, cat in TAG_TO_CATEGORY.items():
            if k in key:
                return cat
    return "Others"


def _random_password(length: int = 32) -> str:
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(max(8, length)))


def _b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def _generate_jwt(secret: str, payload_raw: str | None = None) -> str:
    header = {"alg": "HS256", "typ": "JWT"}
    if payload_raw:
        try:
            payload = json.loads(payload_raw)
        except json.JSONDecodeError:
            payload = {"iss": "dokploy-zimaos", "iat": int(time.time())}
    else:
        payload = {"iss": "dokploy-zimaos", "iat": int(time.time())}
    h_enc = _b64url(json.dumps(header, separators=(",", ":")).encode("utf-8"))
    p_enc = _b64url(json.dumps(payload, separators=(",", ":")).encode("utf-8"))
    sig = hmac.new(secret.encode("utf-8"), f"{h_enc}.{p_enc}".encode("utf-8"), hashlib.sha256).digest()
    return f"{h_enc}.{p_enc}.{_b64url(sig)}"


def _parse_iso_timestamp(dt_str: str) -> float:
    s = dt_str.strip()
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    try:
        return datetime.fromisoformat(s).timestamp()
    except ValueError:
        return time.time()


def resolve_helper(expr: str, resolved_vars: dict[str, str], default_domain: str) -> str:
    """Resolve helpers e referências ${...} do template.toml do Dokploy."""
    expr = expr.strip()

    if expr in resolved_vars:
        return resolved_vars[expr]

    parts = expr.split(":")
    head = parts[0].strip()

    if head == "domain":
        return default_domain
    if head == "password":
        length = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 32
        return _random_password(length)
    if head == "base64":
        nbytes = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 32
        return base64.b64encode(secrets.token_bytes(max(8, nbytes))).decode("ascii")
    if head == "hash":
        nbytes = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 16
        return secrets.token_hex(max(4, nbytes))
    if head == "uuid":
        return str(uuid.uuid4())
    if head == "randomPort":
        return str(secrets.randbelow(20000) + 20000)
    if head == "email":
        return "admin@example.com"
    if head == "username":
        return "admin"
    if head == "timestamp":
        return str(int(time.time() * 1000))
    if head == "timestampms":
        if len(parts) > 1:
            dt = ":".join(parts[1:])
            return str(int(_parse_iso_timestamp(dt) * 1000))
        return str(int(time.time() * 1000))
    if head == "timestamps":
        if len(parts) > 1:
            dt = ":".join(parts[1:])
            return str(int(_parse_iso_timestamp(dt)))
        return str(int(time.time()))
    if head == "jwt":
        if len(parts) == 2 and parts[1].isdigit():
            return secrets.token_hex(int(parts[1]))
        secret_key = parts[1] if len(parts) > 1 else ""
        secret_val = resolved_vars.get(secret_key, secret_key or _random_password(32))
        payload_val = resolved_vars.get(parts[2]) if len(parts) > 2 else None
        return _generate_jwt(secret_val, payload_val)

    return f"${{{expr}}}"


def interpolate_string(value: str, resolved_vars: dict[str, str], default_domain: str) -> str:
    """Substitui todas as ocorrências ${...} em uma string."""
    result = value
    for _ in range(5):
        changed = False

        def _repl(match: re.Match[str]) -> str:
            nonlocal changed
            token = match.group(1)
            new_val = resolve_helper(token, resolved_vars, default_domain)
            if new_val != match.group(0):
                changed = True
            return new_val

        result = HELPER_PATTERN.sub(_repl, result)
        if not changed:
            break
    return result


def _collect_env_entries(raw_env: Any, resolved_vars: dict[str, str], default_domain: str) -> dict[str, str]:
    env_map: dict[str, str] = {}
    if isinstance(raw_env, list):
        for entry in raw_env:
            line = str(entry).strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env_map[k.strip()] = interpolate_string(v, resolved_vars, default_domain)
    elif isinstance(raw_env, dict):
        for k, v in raw_env.items():
            env_map[str(k).strip()] = interpolate_string(str(v), resolved_vars, default_domain)
    return env_map


def parse_template_toml(toml_path: Path, default_domain: str) -> dict[str, Any]:
    """Lê e resolve template.toml do Dokploy (variables, domains, env, mounts)."""
    if not toml_path.exists():
        return {"variables": {}, "domains": [], "env": {}, "mounts": []}

    raw = tomllib.loads(toml_path.read_text(encoding="utf-8"))
    raw_vars = raw.get("variables") or {}
    resolved_vars: dict[str, str] = {}

    for k, v in raw_vars.items():
        resolved_vars[k] = interpolate_string(str(v), resolved_vars, default_domain)

    config = raw.get("config") or {}
    env_map: dict[str, str] = {}

    # Env no nível [config] ou [config.env]
    env_map.update(_collect_env_entries(config.get("env"), resolved_vars, default_domain))

    # Domains (também coleta env se algum template posicionou env após [[config.domains]])
    domains: list[dict[str, Any]] = []
    for d in config.get("domains") or []:
        if not isinstance(d, dict):
            continue
        if "env" in d:
            env_map.update(_collect_env_entries(d.get("env"), resolved_vars, default_domain))
        domains.append(
            {
                "serviceName": str(d.get("serviceName", "")).strip(),
                "port": int(d["port"]) if str(d.get("port", "")).isdigit() else None,
                "host": interpolate_string(str(d.get("host", default_domain)), resolved_vars, default_domain),
                "path": str(d.get("path", "/")) or "/",
            }
        )

    # Mounts
    mounts: list[dict[str, str]] = []
    for m in config.get("mounts") or []:
        if not isinstance(m, dict):
            continue
        fp = str(m.get("filePath", "")).strip()
        content = interpolate_string(str(m.get("content", "")), resolved_vars, default_domain)
        if fp:
            mounts.append({"filePath": fp, "content": content})

    return {
        "variables": resolved_vars,
        "domains": domains,
        "env": env_map,
        "mounts": mounts,
    }


def extract_port_from_service(svc: dict[str, Any]) -> int | None:
    """Extrai uma porta TCP publicada ou exposta de um serviço Compose."""
    for p in svc.get("ports") or []:
        if isinstance(p, dict):
            target = p.get("published") or p.get("target")
            if target and str(target).isdigit():
                return int(target)
        elif isinstance(p, (int, str)):
            s = str(p).split("/")[0]
            parts = s.split(":")
            cand = parts[-1] if parts else ""
            if cand.isdigit():
                return int(cand)

    for e in svc.get("expose") or []:
        s = str(e).split("/")[0].strip()
        if s.isdigit():
            return int(s)

    return None


def pick_main_service_and_port(
    services: dict[str, Any], domains: list[dict[str, Any]]
) -> tuple[str, int, str]:
    """Determina (main_service, port, index_path) para x-casaos."""
    for d in domains:
        svc_name = d.get("serviceName")
        if svc_name and svc_name in services:
            port = d.get("port") or extract_port_from_service(services[svc_name]) or 8080
            path = d.get("path") or "/"
            return svc_name, int(port), path

    service_names = list(services.keys())
    for name in service_names:
        low = name.lower()
        if not any(hint in low for hint in NON_MAIN_SERVICE_HINTS):
            port = extract_port_from_service(services[name]) or 8080
            return name, int(port), "/"

    first = service_names[0]
    port = extract_port_from_service(services[first]) or 8080
    return first, int(port), "/"


def ensure_service_port_published(svc: dict[str, Any], port: int) -> None:
    """Garante que o serviço principal publique a porta no host para o ZimaOS."""
    ports = svc.get("ports")
    if ports is None:
        ports = []
        svc["ports"] = ports

    for entry in ports:
        if isinstance(entry, dict):
            if str(entry.get("target")) == str(port):
                return
        elif isinstance(entry, (int, str)):
            raw = str(entry).split("/")[0]
            parts = raw.split(":")
            if parts and parts[-1] == str(port):
                return

    ports.append(
        {
            "target": int(port),
            "published": QuotedString(str(port)),
            "protocol": "tcp",
        }
    )


def rewrite_compose_volumes(svc: dict[str, Any]) -> None:
    """Converte bind mounts relativos do Dokploy (../files/...) para /DATA/AppData/$AppID/..."""
    volumes = svc.get("volumes")
    if not isinstance(volumes, list):
        return

    new_volumes: list[Any] = []
    for v in volumes:
        if isinstance(v, str):
            parts = v.split(":")
            if len(parts) >= 2 and (parts[0].startswith("../files/") or parts[0].startswith("./")):
                rel = parts[0].replace("../files/", "", 1).lstrip("./")
                parts[0] = f"/DATA/AppData/$AppID/{rel}"
                new_volumes.append(":".join(parts))
            else:
                new_volumes.append(v)
        elif isinstance(v, dict):
            src = str(v.get("source", ""))
            if src.startswith("../files/") or src.startswith("./"):
                rel = src.replace("../files/", "", 1).lstrip("./")
                v = dict(v)
                v["source"] = f"/DATA/AppData/$AppID/{rel}"
            new_volumes.append(v)
        else:
            new_volumes.append(v)
    svc["volumes"] = new_volumes


def _replace_env_refs(text: str, env_map: dict[str, str]) -> str:
    def _repl(match: re.Match[str]) -> str:
        var_name = match.group(1)
        if var_name in env_map:
            return env_map[var_name]
        return match.group(0)

    return ENV_REF_PATTERN.sub(_repl, text)


def inject_env_defaults(svc: dict[str, Any], env_map: dict[str, str]) -> None:
    """Substitui placeholders ${VAR} e ${VAR:-default} usando os valores resolvidos do template.toml."""
    if not env_map:
        return

    env = svc.get("environment")
    if isinstance(env, dict):
        updated: dict[str, Any] = {}
        for k, v in env.items():
            if v is None:
                updated[k] = env_map.get(k, "")
            else:
                updated[k] = _replace_env_refs(str(v), env_map)
        svc["environment"] = updated
    elif isinstance(env, list):
        updated_list: list[str] = []
        for item in env:
            s = str(item)
            if "=" in s:
                k, v = s.split("=", 1)
                updated_list.append(f"{k}={_replace_env_refs(v, env_map)}")
            else:
                if s in env_map:
                    updated_list.append(f"{s}={env_map[s]}")
                else:
                    updated_list.append(s)
        svc["environment"] = updated_list


def strip_dokploy_external_networks(compose: dict[str, Any]) -> None:
    """Remove referências à rede externa 'dokploy-network' que não existe no ZimaOS."""
    networks = compose.get("networks")
    if isinstance(networks, dict) and "dokploy-network" in networks:
        networks.pop("dokploy-network", None)
        if not networks:
            compose.pop("networks", None)

    for svc in (compose.get("services") or {}).values():
        if not isinstance(svc, dict):
            continue
        svc_nets = svc.get("networks")
        if isinstance(svc_nets, list) and "dokploy-network" in svc_nets:
            svc_nets = [n for n in svc_nets if n != "dokploy-network"]
            if svc_nets:
                svc["networks"] = svc_nets
            else:
                svc.pop("networks", None)
        elif isinstance(svc_nets, dict) and "dokploy-network" in svc_nets:
            svc_nets.pop("dokploy-network", None)
            if not svc_nets:
                svc.pop("networks", None)


def infer_version(meta: dict[str, Any], services: dict[str, Any], main_svc: str) -> str:
    raw_ver = str(meta.get("version") or "").strip()
    if raw_ver and raw_ver.lower() not in {"latest", "main", "master", "edge"}:
        return raw_ver.lstrip("v")
    image = str((services.get(main_svc) or {}).get("image") or "")
    if ":" in image:
        tag = image.rsplit(":", 1)[1].strip()
        if tag and tag.lower() not in {"latest", "alpine", "stable"}:
            return tag.lstrip("v")
    return "1.0.0"


def sanitize_compose_for_zimaos(compose: dict[str, Any], app_slug: str) -> None:
    """Ajusta o compose para compatibilidade estrita com o ZimaOS / CasaOS compose loader."""
    services = compose.get("services") or {}
    for svc_name, svc in services.items():
        if not isinstance(svc, dict):
            continue

        # 1. Remove env_file para evitar falhas de arquivos inexistentes no ZimaOS
        svc.pop("env_file", None)

        # 2. Corrigir deploy.replicas para inteiro
        if isinstance(svc.get("deploy"), dict):
            deploy = svc["deploy"]
            if "replicas" in deploy:
                try:
                    rep_str = str(deploy["replicas"]).split(":")[-1].strip("'\"}")
                    deploy["replicas"] = int(rep_str) if rep_str.isdigit() else 1
                except Exception:
                    deploy["replicas"] = 1

        # 3. Sanitizar mem_limit e cpus
        if "mem_limit" in svc and isinstance(svc["mem_limit"], str):
            if "${" in svc["mem_limit"]:
                svc["mem_limit"] = "2g"
        if "cpus" in svc and isinstance(svc["cpus"], str):
            try:
                cpu_clean = re.sub(r"[^\d.]", "", svc["cpus"])
                svc["cpus"] = float(cpu_clean) if cpu_clean else 1.0
            except Exception:
                svc.pop("cpus", None)

        # 4. Sanitizar ports
        ports = svc.get("ports")
        if isinstance(ports, list):
            cleaned_ports = []
            for p in ports:
                if isinstance(p, str):
                    if "${" in p:
                        m = re.search(r":-(\d+)", p)
                        if m:
                            p = m.group(1)
                        else:
                            p = re.sub(r"\$\{[^}]*\}?", "8080", p)
                cleaned_ports.append(p)
            svc["ports"] = cleaned_ports

        # 5. Sanitizar volumes (deduplicar e tratar subpath ou variáveis não resolvidas)
        volumes = svc.get("volumes")
        if isinstance(volumes, list):
            seen: set[str] = set()
            cleaned_vols: list[Any] = []
            for v in volumes:
                if isinstance(v, str):
                    if "${" in v:
                        v = re.sub(r"\$\{[A-Za-z0-9_:-]+", f"/DATA/AppData/{app_slug}/data", v).replace("}", "")
                    if v not in seen:
                        seen.add(v)
                        cleaned_vols.append(v)
                elif isinstance(v, dict):
                    v = dict(v)
                    v.pop("subpath", None)
                    v_key = json.dumps(v, sort_keys=True)
                    if v_key not in seen:
                        seen.add(v_key)
                        cleaned_vols.append(v)
                else:
                    cleaned_vols.append(v)
            svc["volumes"] = cleaned_vols


def convert_blueprint(
    bp_dir: Path,
    apps_out_dir: Path,
    base_url: str,
    default_domain: str,
    today_iso: str,
) -> dict[str, Any] | None:
    """Converte um único blueprint do Dokploy em Apps/<AppFolder>/docker-compose.yml."""
    compose_path = bp_dir / "docker-compose.yml"
    if not compose_path.exists():
        compose_path = bp_dir / "docker-compose.yaml"
    if not compose_path.exists():
        return None

    meta_path = bp_dir / "meta.json"
    meta: dict[str, Any] = {}
    if meta_path.exists():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))

    raw_id = str(meta.get("id") or bp_dir.name).strip()
    app_slug = slugify_app_id(raw_id)
    app_folder_name = folder_name_from_id(raw_id, meta.get("name"))
    display_name = str(meta.get("name") or raw_id.replace("-", " ").title()).strip()
    description = str(meta.get("description") or f"{display_name} self-hosted template imported from Dokploy.").strip()
    tagline = description.split(".")[0].strip()
    if len(tagline) > 90:
        tagline = tagline[:87].rstrip() + "..."

    toml_data = parse_template_toml(bp_dir / "template.toml", default_domain)

    compose_text = compose_path.read_text(encoding="utf-8")
    compose = yaml.safe_load(compose_text)
    if not isinstance(compose, dict) or not isinstance(compose.get("services"), dict) or not compose["services"]:
        return None

    services: dict[str, Any] = compose["services"]

    compose.pop("version", None)
    compose["name"] = app_slug

    strip_dokploy_external_networks(compose)

    main_svc, main_port, index_path = pick_main_service_and_port(services, toml_data["domains"])

    for svc_name, svc in services.items():
        if not isinstance(svc, dict):
            continue
        svc.setdefault("restart", "unless-stopped")
        inject_env_defaults(svc, toml_data["env"])
        rewrite_compose_volumes(svc)
        if svc_name == main_svc:
            ensure_service_port_published(svc, main_port)

    sanitize_compose_for_zimaos(compose, app_slug)

    app_dir = apps_out_dir / app_folder_name
    app_dir.mkdir(parents=True, exist_ok=True)

    # Copia logo (se existir)
    logo_name = str(meta.get("logo") or "").strip()
    icon_filename = "icon.svg"
    logo_src = bp_dir / logo_name if logo_name else None
    if logo_src and logo_src.is_file():
        ext = logo_src.suffix.lower() or ".png"
        icon_filename = f"icon{ext}"
        shutil.copy2(logo_src, app_dir / icon_filename)
    else:
        for cand in sorted(bp_dir.iterdir()):
            if cand.suffix.lower() in {".svg", ".png", ".webp", ".jpg", ".jpeg"}:
                icon_filename = f"icon{cand.suffix.lower()}"
                shutil.copy2(cand, app_dir / icon_filename)
                break

    icon_url = f"{base_url.rstrip('/')}/Apps/{app_folder_name}/{icon_filename}"

    mount_notes: list[str] = []
    if toml_data["mounts"]:
        files_dir = app_dir / "files"
        files_dir.mkdir(exist_ok=True)
        for m in toml_data["mounts"]:
            rel_fp = m["filePath"].lstrip("/")
            dest = files_dir / rel_fp
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(m["content"], encoding="utf-8")
            mount_notes.append(rel_fp)

    category = map_category(meta.get("tags"))
    version_str = infer_version(meta, services, main_svc)
    links = meta.get("links") or {}

    x_casaos: dict[str, Any] = {
        "id": f"com.dokploy.{app_slug}",
        "main": main_svc,
        "index": index_path,
        "port_map": QuotedString(str(main_port)),
        "scheme": "http",
        "icon": icon_url,
        "title": {"en_US": display_name},
        "tagline": {"en_US": tagline},
        "description": {"en_US": description},
        "author": "Dokploy Community",
        "developer": display_name,
        "category": category,
        "architectures": ["amd64", "arm64"],
        "version": QuotedString(version_str),
        "update_at": QuotedString(today_iso),
    }

    if links.get("website"):
        x_casaos["website"] = str(links["website"])
    if links.get("github"):
        x_casaos["repo"] = str(links["github"])
    if links.get("docs"):
        x_casaos["docs"] = str(links["docs"])

    if mount_notes:
        x_casaos["tips"] = {
            "before_install": {
                "en_US": (
                    "Imported from Dokploy. Default config files were extracted to the app's "
                    f"files/ folder ({', '.join(mount_notes)}). Review environment variables before starting."
                )
            }
        }

    ordered_compose: dict[str, Any] = {"name": compose["name"], "services": compose["services"]}
    for key, val in compose.items():
        if key not in {"name", "services", "x-casaos"}:
            ordered_compose[key] = val
    ordered_compose["x-casaos"] = x_casaos

    out_compose_path = app_dir / "docker-compose.yml"
    out_compose_path.write_text(
        yaml.dump(ordered_compose, Dumper=ZimaOSDumper, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )

    return {
        "id": x_casaos["id"],
        "folder": app_folder_name,
        "name": display_name,
        "tagline": tagline,
        "description": description,
        "category": category,
        "main": main_svc,
        "port": main_port,
        "version": version_str,
        "icon": icon_url,
    }


def write_store_root_files(
    out_dir: Path,
    store_id: str,
    maintainer: str,
    repo_url: str,
    converted_apps: list[dict[str, Any]],
) -> None:
    """Cria arquivos raiz exigidos pelo ZimaOS (protocolo v2 + compatibilidade v1)."""
    store_config = {
        "version": 2,
        "store_id": store_id,
        "name": {
            "en_US": "Dokploy Templates for ZimaOS",
            "pt_BR": "Templates Dokploy para ZimaOS",
        },
        "description": {
            "en_US": "Open-source self-hosted templates automatically converted from Dokploy/templates.",
            "pt_BR": "Templates open-source convertidos automaticamente de Dokploy/templates.",
        },
        "maintainer": maintainer,
        "url": repo_url,
    }

    config_json_str = json.dumps(store_config, indent=2, ensure_ascii=False) + "\n"
    (out_dir / "store-config.json").write_text(config_json_str, encoding="utf-8")
    (out_dir / "store.json").write_text(config_json_str, encoding="utf-8")

    supported_langs = ["en_US", "pt_BR"]
    supported_langs_str = json.dumps(supported_langs, indent=2) + "\n"
    (out_dir / "supported-languages.json").write_text(supported_langs_str, encoding="utf-8")

    category_list = [{"name": cat, "font": "apps"} for cat in ZIMAOS_V2_CATEGORIES]
    category_list_str = json.dumps(category_list, indent=2, ensure_ascii=False) + "\n"
    (out_dir / "category-list.json").write_text(category_list_str, encoding="utf-8")

    recommended = [app["folder"] for app in converted_apps[:12]]
    recommended_str = json.dumps(recommended, indent=2, ensure_ascii=False) + "\n"
    (out_dir / "recommend-list.json").write_text(recommended_str, encoding="utf-8")

    index_data = {
        "version": 2,
        "store_id": store_id,
        "name": store_config["name"],
        "description": store_config["description"],
        "maintainer": maintainer,
        "url": repo_url,
        "total_apps": len(converted_apps),
        "apps": converted_apps,
    }
    index_json_str = json.dumps(index_data, indent=2, ensure_ascii=False) + "\n"
    (out_dir / "index.json").write_text(index_json_str, encoding="utf-8")

    # Copia manifests para dist e dist/store para garantir suporte tanto v1 quanto v2
    for target_dir in [out_dir / "dist", out_dir / "dist" / "store"]:
        target_dir.mkdir(parents=True, exist_ok=True)
        (target_dir / "store-config.json").write_text(config_json_str, encoding="utf-8")
        (target_dir / "store.json").write_text(config_json_str, encoding="utf-8")
        (target_dir / "supported-languages.json").write_text(supported_langs_str, encoding="utf-8")
        (target_dir / "category-list.json").write_text(category_list_str, encoding="utf-8")
        (target_dir / "recommend-list.json").write_text(recommended_str, encoding="utf-8")
        (target_dir / "index.json").write_text(index_json_str, encoding="utf-8")


def write_store_readme(
    out_dir: Path,
    converted_apps: list[dict[str, Any]],
    categories: Counter,
    maintainer: str,
    repo_url: str,
    base_url: str,
) -> None:
    """Gera um README.md completo e elegante para a loja do ZimaOS."""
    total = len(converted_apps)
    cat_badges = " ".join(f"`{cat}: {count}`" for cat, count in categories.most_common())
    zip_url = f"{repo_url.rstrip('/')}/archive/refs/heads/main.zip"
    store_v2_url = f"{base_url.rstrip('/')}/store.json"

    # Tabela com as categorias e links
    by_category: dict[str, list[dict[str, Any]]] = {}
    for app in converted_apps:
        by_category.setdefault(app["category"], []).append(app)

    cat_sections = []
    for cat in ZIMAOS_V2_CATEGORIES:
        apps = by_category.get(cat, [])
        if not apps:
            continue
        apps_sorted = sorted(apps, key=lambda a: a["name"].lower())
        rows = [
            f"| **{app['name']}** | `{app['folder']}` | {app.get('tagline', '')} | [Compose](Apps/{app['folder']}/docker-compose.yml) |"
            for app in apps_sorted
        ]
        cat_sections.append(
            f"### 📁 {cat} ({len(apps)} apps)\n\n"
            f"| App | Pasta | Descrição | Compose |\n"
            f"| :--- | :--- | :--- | :--- |\n"
            + "\n".join(rows)
            + "\n"
        )

    readme_content = f"""# 🏪 Dokploy Templates para ZimaOS & CasaOS

Catálogo com **{total} aplicações auto-hospedadas (self-hosted)** convertidas automaticamente do [Dokploy/templates](https://github.com/Dokploy/templates) para o formato nativo da Loja de Aplicativos do **ZimaOS** e **CasaOS** (suporte aos protocolos v2 e v1 ZIP).

---

## 📊 Estatísticas
- **Total de Apps:** `{total}`
- **Categorias:** {cat_badges}
- **Sincronização:** Atualizado diariamente via GitHub Actions direto do Dokploy Canary.

---

## 🚀 Como Adicionar ao ZimaOS / CasaOS

### Método 1: URL de Repositório (Recomendado - Protocolo v1 / v2)
1. No seu **ZimaOS** ou **CasaOS**, abra a **App Store** (Loja de Apps).
2. Clique no ícone de engrenagem ⚙️ ou no botão **+ Adicionar Fonte** (**+ Add Source**).
3. Cole a seguinte URL:
   ```text
   {zip_url}
   ```
   *Ou a URL direta do manifesto:*
   ```text
   {store_v2_url}
   ```
4. Clique em **Adicionar** / **Confirmar**.
5. Aguarde alguns segundos até o ZimaOS sincronizar todos os {total} aplicativos no seu catálogo!

---

## 🛠️ Manutenção e Sincronização Automática
Este repositório possui uma GitHub Action (`.github/workflows/sync-dokploy.yml`) que roda todos os dias às 06:00 UTC, buscando novos templates e atualizações do repositório oficial do Dokploy e gerando os novos Compose files.

---

## 📦 Lista Completa de Aplicativos ({total})

{"".join(cat_sections)}

---

Feito com ❤️ pela comunidade para o ecossistema ZimaOS / CasaOS.
"""
    (out_dir / "README.md").write_text(readme_content, encoding="utf-8")


def build_v1_zip(out_dir: Path, zip_path: Path) -> None:
    """Empacota o repositório no formato ZIP compatível com '+ Add Source' do ZimaOS."""
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    root_prefix = out_dir.name
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for file_path in sorted(out_dir.rglob("*")):
            if file_path.is_dir() or file_path == zip_path:
                continue
            rel = file_path.relative_to(out_dir)
            if rel.parts and rel.parts[0] in {"dist", ".git", ".cache"}:
                continue
            zf.write(file_path, arcname=f"{root_prefix}/{rel.as_posix()}")


def write_github_action(out_dir: Path) -> None:
    """Gera workflow GitHub Actions para sincronização diária automática com Dokploy/templates."""
    wf_dir = out_dir / ".github" / "workflows"
    wf_dir.mkdir(parents=True, exist_ok=True)
    workflow = """name: Sync Dokploy Templates to ZimaOS App Store

on:
  schedule:
    - cron: "0 6 * * *"
  workflow_dispatch:

permissions:
  contents: write

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout store repo
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install PyYAML
        run: pip install pyyaml

      - name: Convert Dokploy templates
        run: |
          python3 dokploy_to_zimaos.py \\
            --clone \\
            --output . \\
            --base-url "https://raw.githubusercontent.com/${{ github.repository }}/main" \\
            --repo-url "https://github.com/${{ github.repository }}" \\
            --maintainer "${{ github.repository_owner }}" \\
            --zip

      - name: Commit updated store
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add Apps store-config.json store.json supported-languages.json category-list.json recommend-list.json index.json dist README.md dokploy_to_zimaos.py
          git diff --cached --quiet || git commit -m "chore: sync Dokploy templates"
          git push
"""
    (wf_dir / "sync-dokploy.yml").write_text(workflow, encoding="utf-8")


def clone_dokploy_repo(dest: Path, branch: str = "canary") -> Path:
    if dest.exists():
        print(f"Atualizando clone existente em {dest}...")
        subprocess.run(["git", "-C", str(dest), "pull", "--ff-only"], check=True)
    else:
        print(f"Clonando {DOKPLOY_REPO_URL} (branch {branch})...")
        subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", branch, DOKPLOY_REPO_URL, str(dest)],
            check=True,
        )
    return dest


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Converte a lista de templates do Dokploy para o formato da Loja do ZimaOS (v2 + ZIP v1)."
    )
    parser.add_argument("--source", type=Path, help="Caminho para clone local de Dokploy/templates.")
    parser.add_argument("--clone", action="store_true", help="Clona/atualiza Dokploy/templates automaticamente.")
    parser.add_argument("--branch", default="canary", help="Branch do Dokploy/templates (padrão: canary).")
    parser.add_argument("--output", type=Path, default=Path("./zimaos-dokploy-store"), help="Diretório de saída da loja.")
    parser.add_argument("--store-id", default="dokploy-templates", help="Identificador único da loja (store_id).")
    parser.add_argument("--maintainer", default="jvribeiro98", help="Nome do mantenedor em store-config.json.")
    parser.add_argument(
        "--repo-url",
        default="https://github.com/jvribeiro98/zimaos-dokploy-store",
        help="URL pública do repositório da loja.",
    )
    parser.add_argument(
        "--base-url",
        default="https://raw.githubusercontent.com/jvribeiro98/zimaos-dokploy-store/main",
        help="URL base usada para montar o link de x-casaos.icon.",
    )
    parser.add_argument("--domain", default="localhost", help="Domínio padrão para substituir ${domain}.")
    parser.add_argument("--limit", type=int, default=0, help="Limita quantidade de templates (0 = todos).")
    parser.add_argument("--zip", action="store_true", help="Gera dist/store/main.zip pronto para importar no ZimaOS.")
    parser.add_argument("--init-ci", action="store_true", help="Gera .github/workflows/sync-dokploy.yml para sync automático.")
    args = parser.parse_args()

    if args.clone:
        source_dir = clone_dokploy_repo(Path(".cache/dokploy-templates"), branch=args.branch)
    elif args.source:
        source_dir = args.source
    else:
        parser.error("Informe --clone ou --source <caminho-do-repo-dokploy-templates>.")

    blueprints_dir = source_dir / "blueprints"
    if not blueprints_dir.is_dir():
        sys.exit(f"Erro: diretório 'blueprints/' não encontrado em {source_dir}")

    out_dir = args.output.resolve()
    apps_out_dir = out_dir / "Apps"
    apps_out_dir.mkdir(parents=True, exist_ok=True)

    today_iso = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    bp_dirs = sorted([p for p in blueprints_dir.iterdir() if p.is_dir()])
    if args.limit > 0:
        bp_dirs = bp_dirs[: args.limit]

    converted: list[dict[str, Any]] = []
    skipped: list[tuple[str, str]] = []
    categories = Counter()

    for bp in bp_dirs:
        try:
            info = convert_blueprint(
                bp_dir=bp,
                apps_out_dir=apps_out_dir,
                base_url=args.base_url,
                default_domain=args.domain,
                today_iso=today_iso,
            )
            if info:
                converted.append(info)
                categories[info["category"]] += 1
            else:
                skipped.append((bp.name, "docker-compose.yml ausente ou sem services"))
        except Exception as exc:  # noqa: BLE001
            skipped.append((bp.name, str(exc)))

    write_store_root_files(
        out_dir=out_dir,
        store_id=args.store_id,
        maintainer=args.maintainer,
        repo_url=args.repo_url,
        converted_apps=converted,
    )

    write_store_readme(
        out_dir=out_dir,
        converted_apps=converted,
        categories=categories,
        maintainer=args.maintainer,
        repo_url=args.repo_url,
        base_url=args.base_url,
    )

    # Copia o script para a raiz da loja para que o GitHub Actions funcione independentemente
    script_file = Path(__file__).resolve()
    target_script = out_dir / "dokploy_to_zimaos.py"
    if script_file != target_script.resolve():
        shutil.copy2(script_file, target_script)

    if args.init_ci:
        write_github_action(out_dir)

    if args.zip:
        zip_path = out_dir / "dist" / "store" / "main.zip"
        build_v1_zip(out_dir, zip_path)
        print(f"Pacote ZIP v1 gerado em: {zip_path}")

    print(f"\nConversão concluída: {len(converted)} apps convertidos, {len(skipped)} ignorados.")
    print("Distribuição por categoria ZimaOS:")
    for cat, count in categories.most_common():
        print(f"  - {cat}: {count}")
    if skipped:
        print("\nIgnorados (primeiros 10):")
        for name, reason in skipped[:10]:
            print(f"  - {name}: {reason}")


if __name__ == "__main__":
    main()