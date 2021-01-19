import jinja2
import click
from collections import namedtuple
import os


template = """server {
    listen 80;

    server_name {{ ws.url }}kamilaburzynska.com;

    return 301 https://{{ ws.url }}kamilaburzynska.com$request_uri;
}

server {
    listen 443 ssl;

    server_name {{ ws.url }}kamilaburzynska.com;

    ssl_certificate /etc/letsencrypt/live/kamilaburzynska.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/kamilaburzynska.com/privkey.pem;

    resolver 127.0.0.11 valid=30s;

{% if ws.has_service %}
    location /api/ {
        set $api_url kamila_{{ ws.service_name }}_service_1:{{ ws.service_port }};
        proxy_pass http://$api_url;
    }
{% endif %}
    location / {
        set $ui_url kamila_{{ ws.ui_name }}_1:{{ ws.ui_port }};
        proxy_pass http://$ui_url;
    }
}

"""

WebsiteInfo = namedtuple(
    "WebsiteInfo",
    ["url", "service_name", "service_port", "has_service", "ui_name", "ui_port"],
)


def create_website_info(spec):
    has_service = "service_port" in spec
    return WebsiteInfo(
        url="" if "is_root" in spec else spec["name"] + ".",
        service_name=spec["name"],
        service_port=spec.get("service_port", None),
        has_service=has_service,
        ui_name=spec.get("ui_name", spec["name"] + ("_ui" if has_service else "")),
        ui_port=5000,
    )


@click.command()
@click.argument("output_dir")
def main(output_dir):
    cfg = [
        {"name": "about_me", "is_root": True},
        {"name": "byte-size", "ui_name": "byte_size"},
        {"name": "drums"},
        {"name": "face", "service_port": 3003},
        {"name": "fit", "service_port": 3003},
        {"name": "movie", "service_port": 3005},
        {"name": "navbar"},
        {"name": "news", "service_port": 5000},
        {"name": "robots"},
    ]

    for c in cfg:
        print(f'procesing: {c["name"]}')
        info = create_website_info(c)
        with open(os.path.join(output_dir, c['name'] + '.conf'), 'w') as f:
            f.write(jinja2.Template(template).render(ws=info))

    print("===== DONE =====")


if __name__ == "__main__":
    main()
