#!/usr/bin/env python3
"""
Construye el prototipo de la encuesta de alta.

Toma src/encuesta.src.html y le incrusta los logos, la animación de confeti
y el mockup de tienda, de modo que el resultado sea un solo archivo HTML
sin dependencias externas más allá de la tipografía y lottie-web.

Uso:   python3 src/build.py
Salida: vercel-encuesta/index.html   (versión A)
        vercel-encuesta/v-b/index.html (versión B, misma página)
        opcion-b-registro.html       (registro de la maqueta de 2 columnas)
"""
import re, os, json, base64, subprocess, zipfile, io

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICONOS = os.path.join(RAIZ, "iconos")
SRC = os.path.join(RAIZ, "src", "encuesta.src.html")

src = open(SRC, encoding="utf-8").read()

def inline_svg(archivo, clase, alt):
    svg = open(os.path.join(ICONOS, archivo), encoding="utf-8").read().strip()
    svg = re.sub(r"<!--.*?-->", "", svg, flags=re.S)
    svg = re.sub(r"\s*\n\s*", "", svg)
    attrs = ('class="%s" role="img" aria-label="%s"' % (clase, alt)) if clase \
            else ('role="img" aria-label="%s"' % alt)
    svg = re.sub(r'<svg\s+width="[^"]*"\s+height="[^"]*"', "<svg " + attrs, svg, count=1)
    return svg.replace("\\", "\\\\").replace("'", "\\'")

def sustituir(marcador, contenido):
    global src
    assert marcador in src, "falta el marcador " + marcador
    src = src.replace(marcador, contenido)

# ── Imagotipos de producto e isotipo T1 ──
for clave, (archivo, alt, clase) in {
    "ENVIOS": ("t1envios.svg", "T1envíos", "brand"),
    "TIENDA": ("t1tienda.svg", "T1tienda", "brand"),
    "PAGOS":  ("t1pagos.svg",  "T1pagos",  "brand"),
    "T1":     ("t1-logotipo.svg", "T1", "iso"),
}.items():
    sustituir("<!--LOGO_%s-->" % clave, inline_svg(archivo, clase, alt))

# ── Métodos de pago ──
for clave, archivo in {
    "VISA": "Property 1=visa.svg", "MC": "Property 1=mc.svg",
    "AMEX": "Property 1=emex.svg", "SPEI": "Property 1=spei.svg",
    "PAYPAL": "Property 1=paypal.svg", "KUESKI": "Property 1=kueski.svg",
    "VCARNET": "Property 1=vcarnet.svg",
}.items():
    sustituir("<!--PAY_%s-->" % clave, inline_svg(archivo, None, clave.title()))

# ── Mockup de tienda: se reduce a 2x del tamaño de uso antes de incrustarlo ──
tmp = os.path.join(RAIZ, "src", "_tienda@2x.png")
subprocess.run(["sips", "-Z", "448", os.path.join(ICONOS, "img tienda.png"),
                "--out", tmp], capture_output=True)
fuente = tmp if os.path.exists(tmp) else os.path.join(ICONOS, "img tienda.png")
sustituir("<!--IMG_PRODUCTOS-->",
          "data:image/png;base64," + base64.b64encode(open(fuente, "rb").read()).decode())
if os.path.exists(tmp):
    os.remove(tmp)

# ── Confeti: el .lottie es un zip; se extrae el JSON y se minifica ──
with zipfile.ZipFile(os.path.join(RAIZ, "celebrate.lottie")) as z:
    nombre = [n for n in z.namelist() if n.startswith("animations/")][0]
    lottie = json.loads(z.read(nombre).decode("utf-8"))
src = re.sub(r"/\*LOTTIE\*/.*?/\*LOTTIE\*/",
             lambda m: json.dumps(lottie, separators=(",", ":"), ensure_ascii=False),
             src, count=1, flags=re.S)

def pagina(cuerpo):
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '</head>\n<body>\n' + cuerpo + '\n</body>\n</html>\n')

sitio = os.path.join(RAIZ, "vercel-encuesta")
os.makedirs(os.path.join(sitio, "v-b"), exist_ok=True)
open(os.path.join(sitio, "index.html"), "w", encoding="utf-8").write(pagina(src))
open(os.path.join(sitio, "v-b", "index.html"), "w", encoding="utf-8").write(pagina(src))
json.dump({"cleanUrls": True}, open(os.path.join(sitio, "vercel.json"), "w"), indent=2)

registro = src.replace('var VARIANTE_FIJA = "A";', 'var VARIANTE_FIJA = "B";', 1)
open(os.path.join(RAIZ, "opcion-b-registro.html"), "w", encoding="utf-8").write(pagina(registro))

# /opciones · comparativa de propuestas para la pantalla final de envios.
# No lleva assets incrustados: se copia tal cual dentro del mismo esqueleto.
opciones = open(os.path.join(RAIZ, "src", "opciones.src.html"), encoding="utf-8").read()
os.makedirs(os.path.join(sitio, "opciones"), exist_ok=True)
open(os.path.join(sitio, "opciones", "index.html"), "w", encoding="utf-8").write(pagina(opciones))

print("listo ·", len(src), "bytes ·", len(opciones), "bytes en /opciones")
