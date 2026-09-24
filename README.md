# Encuesta de alta · T1

Prototipo navegable de la encuesta de perfilamiento que aparece como modal sobre el
administrador de T1envíos, T1tienda y T1pagos.

**En línea**

| | |
|---|---|
| Versión A — la encuesta termina en el cierre | https://vercel-encuesta-roan.vercel.app |
| Versión B — el cierre de pagos continúa en el mismo modal | https://vercel-encuesta-roan.vercel.app/v-b |
| Encuesta para la landing nueva — cinco casos de entrada | https://vercel-encuesta-roan.vercel.app/landing |
| Cierres de envíos — cuatro propuestas comparadas | https://vercel-encuesta-roan.vercel.app/opciones |
| Matriz de casos — qué se pregunta y dónde termina cada uno | https://vercel-encuesta-roan.vercel.app/matriz |

El selector de arriba cambia el caso: en las dos primeras, el producto del panel
de fondo y del cierre; en `/landing`, además de dónde llega el usuario.

## Los dos casos de `/landing`

El cuestionario es el mismo de siempre: llegar desde la landing nueva no lo
cambia. Lo único distinto es la pantalla final, que entrega la tarea con la
que el usuario venía en vez de una oferta genérica.

| Caso | Preguntas | Termina en |
|---|---|---|
| Envíos · a cotizar | las mismas que envíos | cuenta lista, el cupón de cashback y «Ver resultados de cotización» |
| Pagos · link · acuse | las mismas que pagos | activar métodos y «¡Listo! Ya puedes cobrar» con «Ver mi link» |
| Pagos · link · resumen | las mismas que pagos | activar métodos y el resumen: monto, URL y compartir por WhatsApp |

Tienda desde la landing no pasa por encuesta: entra directo al flujo de crear
tienda. Aparece en la matriz, no en el prototipo.

La matriz recoge un solo cierre de pagos, el del resumen: los dos cierres son
una comparación de diseño, no dos casos distintos de encuesta.

## Cómo editar

Los archivos que se editan a mano son los de **`src/`**. Todo lo demás
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
src/encuesta.src.html   fuente de la encuesta actual
src/landing.src.html    fuente de la encuesta para la landing nueva
src/opciones.src.html   fuente de la comparativa de cierres
src/matriz.src.html     fuente de la matriz de casos
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
