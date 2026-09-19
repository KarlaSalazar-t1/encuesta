#!/usr/bin/env python3
"""
Construye los prototipos de encuesta de alta.

Cada fuente de src/ se convierte en un solo HTML con los logos, el confeti y
las imágenes incrustados, sin más dependencias externas que la tipografía y
lottie-web.

Uso:   python3 src/build.py
Salida: vercel-encuesta/index.html          encuesta actual, versión A
        vercel-encuesta/v-b/index.html      la misma, versión B
        vercel-encuesta/landing/index.html  encuesta para la landing nueva
        vercel-encuesta/opciones/index.html comparativa de cierres de envíos
        opcion-b-registro.html              registro de la maqueta de 2 columnas
"""
import re, os, json, base64, subprocess, zipfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICONOS = os.path.join(RAIZ, "iconos")
SITIO = os.path.join(RAIZ, "vercel-encuesta")

LOGOS = {
    "ENVIOS": ("t1envios.svg", "T1envíos", "brand"),
    "TIENDA": ("t1tienda.svg", "T1tienda", "brand"),
    "PAGOS":  ("t1pagos.svg",  "T1pagos",  "brand"),
    "T1":     ("t1-logotipo.svg", "T1", "iso"),
}
PAGOS = {
    "VISA": "Property 1=visa.svg", "MC": "Property 1=mc.svg",
    "AMEX": "Property 1=emex.svg", "SPEI": "Property 1=spei.svg",
    "KUESKI": "Property 1=kueski.svg",
    "VCARNET": "Property 1=vcarnet.svg",
}
REDES = {"WA": "Whatsapp.png", "FB": "Facebook 2.png", "IG": "Insta.png"}


def inline_svg(archivo, clase, alt):
    svg = open(os.path.join(ICONOS, archivo), encoding="utf-8").read().strip()
    svg = re.sub(r"<!--.*?-->", "", svg, flags=re.S)
    svg = re.sub(r"\s*\n\s*", "", svg)
    attrs = ('class="%s" role="img" aria-label="%s"' % (clase, alt)) if clase \
            else ('role="img" aria-label="%s"' % alt)
    svg = re.sub(r'<svg\s+width="[^"]*"\s+height="[^"]*"', "<svg " + attrs, svg, count=1)
    return svg.replace("\\", "\\\\").replace("'", "\\'")


def b64(ruta, tipo="png"):
    return "data:image/%s;base64,%s" % (
        tipo, base64.b64encode(open(ruta, "rb").read()).decode())


def mockup_tienda():
    """El mockup viene a 635px; se reduce a 2x del tamaño de uso."""
    tmp = os.path.join(RAIZ, "src", "_tienda@2x.png")
    subprocess.run(["sips", "-Z", "448", os.path.join(ICONOS, "img tienda.png"),
                    "--out", tmp], capture_output=True)
    fuente = tmp if os.path.exists(tmp) else os.path.join(ICONOS, "img tienda.png")
    dato = b64(fuente)
    if os.path.exists(tmp):
        os.remove(tmp)
    return dato


def confeti():
    """El .lottie es un zip; se saca el JSON de la animación y se minifica."""
    with zipfile.ZipFile(os.path.join(RAIZ, "celebrate.lottie")) as z:
        nombre = [n for n in z.namelist() if n.startswith("animations/")][0]
        return json.dumps(json.loads(z.read(nombre).decode("utf-8")),
                          separators=(",", ":"), ensure_ascii=False)


TIENDA_B64 = mockup_tienda()
LOTTIE = confeti()


def procesar(nombre_fuente):
    src = open(os.path.join(RAIZ, "src", nombre_fuente), encoding="utf-8").read()

    def pon(marcador, contenido, requerido=True):
        nonlocal src
        assert not requerido or marcador in src, "falta el marcador " + marcador
        src = src.replace(marcador, contenido)

    for clave, (archivo, alt, clase) in LOGOS.items():
        pon("<!--LOGO_%s-->" % clave, inline_svg(archivo, clase, alt))
    for clave, archivo in PAGOS.items():
        pon("<!--PAY_%s-->" % clave, inline_svg(archivo, None, clave.title()))
    for clave, archivo in REDES.items():
        # Solo la encuesta de la landing comparte el link por redes
        pon("<!--RED_%s-->" % clave, b64(os.path.join(ICONOS, archivo)), requerido=False)
    pon("<!--IMG_PRODUCTOS-->", TIENDA_B64)
    src = re.sub(r"/\*LOTTIE\*/.*?/\*LOTTIE\*/", lambda m: LOTTIE, src, count=1, flags=re.S)
    return src


def pagina(cuerpo):
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '</head>\n<body>\n' + cuerpo + '\n</body>\n</html>\n')


def escribe(ruta_rel, contenido):
    destino = os.path.join(SITIO, ruta_rel)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    open(destino, "w", encoding="utf-8").write(contenido)


encuesta = procesar("encuesta.src.html")
escribe("index.html", pagina(encuesta))
escribe("v-b/index.html", pagina(encuesta))

landing = procesar("landing.src.html")
escribe("landing/index.html", pagina(landing))

# /opciones no lleva assets: se copia tal cual dentro del mismo esqueleto
opciones = open(os.path.join(RAIZ, "src", "opciones.src.html"), encoding="utf-8").read()
escribe("opciones/index.html", pagina(opciones))

json.dump({"cleanUrls": True}, open(os.path.join(SITIO, "vercel.json"), "w"), indent=2)

registro = encuesta.replace('var VARIANTE_FIJA = "A";', 'var VARIANTE_FIJA = "B";', 1)
open(os.path.join(RAIZ, "opcion-b-registro.html"), "w", encoding="utf-8").write(pagina(registro))

print("listo · encuesta %d · landing %d · opciones %d bytes"
      % (len(encuesta), len(landing), len(opciones)))
