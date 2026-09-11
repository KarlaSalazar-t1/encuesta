# Encuesta de alta · T1

Prototipo navegable de la encuesta de perfilamiento que aparece como modal sobre el
administrador de T1envíos, T1tienda y T1pagos.

**En línea**

| | |
|---|---|
| Versión A — la encuesta termina en el cierre | https://vercel-encuesta-roan.vercel.app |
| Versión B — el cierre continúa en el primer paso real | https://vercel-encuesta-roan.vercel.app/v-b |

El selector de arriba cambia el producto del panel de fondo y del cierre.

## Cómo editar

El único archivo que se edita a mano es **`src/encuesta.src.html`**. Todo lo demás
—`vercel-encuesta/` y `opcion-b-registro.html`— es generado: no editarlo.

```bash
python3 src/build.py
```

El build incrusta los logos de `iconos/`, el confeti de `celebrate.lottie` y el mockup
de tienda, y escribe el sitio completo. El resultado es un solo HTML sin dependencias
externas salvo la tipografía de Google Fonts y lottie-web desde CDN.

Requiere `sips`, que viene con macOS, para redimensionar el mockup.

## Cómo publicar

```bash
python3 src/build.py
cd vercel-encuesta && npx vercel deploy --prod
```

Verificar contra el **contenido**, no contra el código de respuesta: el dominio
responde 200 aunque el despliegue haya fallado y esté sirviendo el build anterior.

```bash
curl -s https://vercel-encuesta-roan.vercel.app/ | grep -o "Solo por tiempo limitado"
```

## Estructura

```
src/encuesta.src.html   fuente editable
src/build.py            genera el sitio
iconos/                 imagotipos T1, métodos de pago, mockup de tienda
celebrate.lottie        animación de confeti del cierre
vercel-encuesta/        generado · lo que se despliega
opcion-b-registro.html  generado · registro de la maqueta de dos columnas
SPEC-UX-…md             especificación original de Growth
referencias visuales/   capturas de referencia usadas en el diseño
```

## Decisiones abiertas

- Destino real de los botones del cierre en cada producto.
- Vigencia del "Solo por tiempo limitado": si la oferta no vence, es urgencia falsa.
- Si el 10% y los $5,000 del cupón coinciden con la oferta vigente.
- Tienda: el prompt de la versión B debería traspasar al flujo de creación existente
  en vez de reimplementarlo.
