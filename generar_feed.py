#!/usr/bin/env python3
"""Genera feed.csv (formato de catálogo de Facebook/WhatsApp Business)
a partir de products.json. Ejecutar cada vez que cambie el catálogo.

Uso: python3 generar_feed.py [URL_BASE]
  URL_BASE = URL pública del sitio, ej. https://usuario.github.io/catalogo-laser
"""
import csv, json, sys

BASE = (sys.argv[1] if len(sys.argv) > 1 else "https://USUARIO.github.io/catalogo-laser").rstrip("/")

with open("products.json", encoding="utf-8") as f:
    data = json.load(f)

cfg = data["config"]
rows = []
for p in data["productos"]:
    if p.get("activo") is False:
        continue
    rows.append({
        "id": p["sku"],
        "title": p["nombre"],
        "description": p["descripcion"],
        "availability": "in stock",
        "condition": "new",
        "price": f'{p["precio"]:.2f} {cfg.get("moneda", "MXN")}',
        "link": f'{BASE}/#{p["sku"]}',
        "image_link": f'{BASE}/{p["imagen"]}',
        "brand": cfg["nombre"],
    })

with open("feed.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys())
    w.writeheader()
    w.writerows(rows)

print(f"feed.csv generado con {len(rows)} productos.")
