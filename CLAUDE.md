# Catálogo de corte láser — instrucciones para Claude Code

Este repositorio es un catálogo estático publicado en GitHub Pages. Los pedidos
se hacen por WhatsApp (no hay carrito). Toda la información de productos vive en
`products.json`; `index.html` lo lee y pinta el catálogo automáticamente.

## Estructura

```
/index.html        → sitio completo (no requiere build)
/products.json     → config del negocio + lista de productos
/img/              → fotos de producto, nombradas por SKU (ej. LSR-007.jpg)
/generar_feed.py   → genera feed.csv para catálogo de Facebook/WhatsApp Business
/archivos/         → (opcional) fuentes de corte por SKU: SVG, CDR, DXF, AI
```

## Flujo: agregar un producto nuevo

Cuando el usuario te entregue un producto nuevo (archivos SVG/Corel/DXF, fotos,
nombre, precio), haz TODO lo siguiente:

1. **SKU**: asigna el siguiente consecutivo `LSR-XXX` (revisa el último en
   `products.json`).
2. **Carpeta de fuentes**: crea `archivos/LSR-XXX/` y guarda ahí los archivos de
   corte (SVG, CDR, DXF). Nunca publiques estos archivos en el sitio; están en
   el repo solo como respaldo de producción. Si el usuario prefiere repo
   privado para las fuentes, sepáralas.
3. **Foto**: optimiza la foto principal a JPG ~1200px de ancho y guárdala como
   `img/LSR-XXX.jpg`.
4. **products.json**: agrega el objeto con: sku, nombre, categoria, precio
   (MXN, número), descripcion (1–2 frases, orientadas a beneficio),
   material, personalizable (bool), imagen.
5. **Feed**: ejecuta `python3 generar_feed.py` para regenerar `feed.csv`.
6. **Publicar**: `git add -A && git commit -m "Nuevo producto LSR-XXX: <nombre>"
   && git push`. GitHub Pages se actualiza solo en ~1 minuto.
7. Confirma al usuario la URL de la pieza publicada.

## Flujo: primer despliegue (solo una vez)

1. `gh repo create catalogo-laser --public --source=. --push`
   (o crea el repo y haz push manual).
2. Activa Pages: `gh api repos/{owner}/catalogo-laser/pages -X POST
   -f build_type=legacy -f "source[branch]=main" -f "source[path]=/"`
   o desde Settings → Pages → branch `main`, carpeta `/ (root)`.
3. La URL queda en `https://<usuario>.github.io/catalogo-laser/`.

## Reglas

- Antes de hacer push, valida que `products.json` sea JSON válido
  (`python3 -m json.tool products.json`).
- No dupliques SKUs. No borres productos: si algo se descontinúa, agrégale
  `"activo": false` y filtra en index.html si el usuario lo pide.
- Los precios son en MXN, por pieza.
- El número de WhatsApp y el nombre del negocio están en `products.json →
  config`. Si el usuario los cambia, solo se editan ahí.
- Mensajes de commit en español, formato: `Nuevo producto LSR-XXX: <nombre>` /
  `Actualiza LSR-XXX: <qué cambió>`.
