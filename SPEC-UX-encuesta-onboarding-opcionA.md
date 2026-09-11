# Encuesta de alta · Opción A · especificación para diseño

**Para:** Karla — UX
**De:** Daniel Soto — Growth
**Fecha:** 9 de septiembre de 2026
**Prototipo vivo:** https://claude.ai/code/artifact/84c385a6-cf78-401e-a02f-2f500c6f021e
**Estado:** Opción A aprobada por Arturo y el equipo. Este documento es la fuente de verdad para el diseño.

> Todas las medidas y todos los textos de este documento están **extraídos del prototipo**, no
> escritos a mano. Si algo aquí no coincide con el prototipo, el prototipo está mal y hay que
> avisarme.

---

## 0 · Lo que hay que saber antes de abrir Figma

**Cinco reglas duras.** Ninguna es negociable en esta primera versión, y todas vienen de decisiones
ya tomadas por Arturo o de datos medidos.

| # | Regla | De dónde viene |
|---|---|---|
| 1 | **La cuenta ya existe** cuando aparece el modal. Detrás se ve el panel de T1envíos. | Decisión de junta: quien abandona deja una cuenta usable, no se pierde. |
| 2 | **Obligatorio de punta a punta.** No hay «X», no se cierra al hacer clic afuera, no hay «Ahora no», no hay «Omitir». | Arturo pidió así el primer borrador. |
| 3 | **Una pregunta por pantalla.** Nunca todo junto. | Decidido en junta. Stripe y Tiendanube hacen lo mismo. |
| 4 | **Cero tecleo salvo un caso.** El nombre llega prellenado excepto para quien ya vende. | 19.1% de los nombres capturados hoy no son nombres de negocio («no», «nose», «hola», «ok»). |
| 5 | **No se pregunta industria ni giro fino.** La tercera pregunta es la corta. | El playbook de Data Science: «el giro, moda o alimentos, cambia el mensaje, no el negocio». |

**Por qué existe cada pregunta.** Esto importa para diseñar: si una pregunta se simplifica o se
fusiona, se pierde un perfil. El árbol de perfilamiento del playbook consolidado cierra **5 de 10
perfiles el día cero**, y cada uno depende de una pregunta concreta.

| Pregunta | Qué perfil cierra |
|---|---|
| ¿Cuál te describe mejor? → *Uso personal* | **#11** La persona, uso personal |
| ¿Cuál te describe mejor? → *Voy empezando* | **#1** El que empieza |
| ¿Dónde vendes hoy? → *A otros negocios / mayoreo* | **#8** El mayorista B2B |
| ¿Qué vendes? → *Servicios* | **#4** El prestador de servicios |
| *Local* + *Productos* juntos | **#3** El negocio local |

Los otros cinco perfiles (#2, #5, #6, #9, #10) **no se preguntan a propósito**: se separan por
volumen o por recurrencia, y eso lo medimos solo en días. Los perfiles #7 y #12 entran por API y
nunca ven esta encuesta.

---

## 1 · El mapa completo: tres caminos, siete pantallas distintas

La primera respuesta define todo el recorrido. **No hay ningún otro punto donde el flujo se
bifurque.**

```
                        ┌─────────────────────────────┐
                        │  P1 · ¿Cuál te describe     │
                        │       mejor?                │   ← siempre
                        └──────────────┬──────────────┘
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        │                              │                              │
   «Voy empezando»            «Ya estoy vendiendo»              «Uso personal»
        │                              │                              │
        ▼                              ▼                              │
┌───────────────────┐        ┌───────────────────┐                    │
│ P2 · ¿Cómo se va  │        │ P2 · ¿Cómo se     │                    │
│ a llamar tu       │        │ llama tu negocio? │                    │
│ negocio?          │        │ (campo VACÍO)     │                    │
│ (PRELLENADO)      │        └─────────┬─────────┘                    │
└─────────┬─────────┘                  │                              │
          │                            ▼                              │
          │                  ┌───────────────────┐                    │
          │                  │ P3 · ¿Dónde       │                    │
          │                  │ vendes hoy?       │                    │
          │                  └─────────┬─────────┘                    │
          │                            │                              │
          ▼                            ▼                              │
┌───────────────────┐        ┌───────────────────┐                    │
│ P3 · ¿Qué vas a   │        │ P4 · ¿Qué vendes? │                    │
│ vender?           │        │                   │                    │
└─────────┬─────────┘        └─────────┬─────────┘                    │
          │                            │                              │
          └────────────────┬───────────┴──────────────────────────────┘
                           ▼
                 ┌───────────────────┐
                 │  CIERRE           │
                 │  Tu cuenta está   │
                 │  lista            │
                 └───────────────────┘
```

**Los tres recorridos, con su largo real:**

| Respuesta en P1 | Pantallas | Secuencia | Toques mínimos | Tecleo |
|---|---|---|---|---|
| **Voy empezando** | **3** | tipo → nombre → qué vas a vender | **4** | ninguno |
| **Ya estoy vendiendo** | **4** | tipo → nombre → dónde vendes → qué vendes | **7** | el nombre |
| **Uso personal** | **1** | tipo | **2** | ninguno |

*Cómo se cuentan los toques:* «Voy empezando» viene preseleccionada, así que ese camino no gasta un
toque en elegirla — sólo avanzar tres veces y marcar el giro. Los otros dos sí gastan un toque en
cambiar la selección de la primera pantalla.

> **Uso personal es el caso más importante de entender.** Es **una sola pantalla**. No ve pantalla
> de nombre —se le pone el suyo automáticamente— ni de canales ni de giro. De la pantalla 1 salta
> directo al cierre.

**Siete pantallas distintas para diseñar** (× 2 dispositivos = **14 artboards**):

1. P1 · ¿Cuál te describe mejor?
2. P2 · Nombre — variante *Voy empezando* (prellenado)
3. P2 · Nombre — variante *Ya estoy vendiendo* (vacío)
4. P3 · ¿Dónde vendes hoy? *(solo «Ya estoy vendiendo»)*
5. P · ¿Qué vas a vender? — variante *Voy empezando*
6. P · ¿Qué vendes? — variante *Ya estoy vendiendo*
7. Cierre

---

## 2 · Pantalla por pantalla

Los textos están en su forma final. **Cópialos literal.**

### P1 · ¿Cuál te describe mejor?

La ven los tres caminos. Es la única pantalla con línea de bienvenida.

| Elemento | Contenido |
|---|---|
| Línea de bienvenida | `Te damos la bienvenida a T1envíos` |
| Pregunta | `¿Cuál te describe mejor?` |
| Ayuda | `Con esto acomodamos lo que sigue.` |
| Opciones (una sola, tarjetas apiladas) | `Voy empezando` · `Ya estoy vendiendo` · `Uso personal` |
| Preseleccionada | **`Voy empezando`** |
| Botón izquierdo | *nada* (es la primera pantalla) |
| Botón derecho | `Continuar` — **salvo si está elegido `Uso personal`, donde dice `Guardar y empezar`** |
| Progreso | `1 de 3` · `1 de 4` · `1 de 1`, según la opción marcada |

**Dos condicionales que viven dentro de esta pantalla y hay que diseñar:**

- **El contador de progreso cambia al tocar una opción.** Con `Voy empezando` dice *1 de 3*; con
  `Ya estoy vendiendo` dice *1 de 4*; con `Uso personal` dice *1 de 1*. La barra se redibuja.
- **El botón cambia de texto.** Con `Uso personal` esta pantalla es la última, así que el botón
  dice `Guardar y empezar` en vez de `Continuar`.

> **Por qué «Voy empezando» viene preseleccionada.** Es la mayoría medida: 2,817 contra 1,457 en la
> encuesta actual, o sea **66% de las altas**. Preseleccionar ancla —lo medimos en el popup de
> recarga, donde los chips jalaron al 23.2% hacia $200— así que la preselección tiene que ser la
> opción más común, no la más rentable.

---

### P2 · Nombre — variante «Voy empezando»

| Elemento | Contenido |
|---|---|
| Pregunta | `¿Cómo se va a llamar tu negocio?` |
| Ayuda | `Puedes cambiarlo cuando quieras.` |
| Campo | **prellenado** con `Tienda de José Daniel` |
| Marca de agua | `Nombre de tu negocio` *(sólo se ve si el usuario borra todo)* |
| Botón izquierdo | `← Atrás` |
| Botón derecho | `Continuar` — **activo desde el inicio**, porque ya hay valor |
| Progreso | `2 de 3` |

> El prellenado es `Tienda de ` + **nombre de pila**, sin apellidos. Si el nombre de pila fuera
> `José Daniel`, el campo dice `Tienda de José Daniel`.

---

### P2 · Nombre — variante «Ya estoy vendiendo»

Misma pantalla, **estado distinto**: el campo llega vacío porque este negocio ya tiene nombre.

| Elemento | Contenido |
|---|---|
| Pregunta | `¿Cómo se llama tu negocio?` |
| Ayuda | `Así aparecerá en tus guías.` |
| Campo | **vacío** |
| Marca de agua | `Dulcería La Esquina` |
| Botón izquierdo | `← Atrás` |
| Botón derecho | `Continuar` — **bloqueado** hasta que se escriba algo |
| Progreso | `2 de 4` |

> **Este es el único tecleo obligatorio de toda la encuesta.** Es a propósito: quien ya vende tiene
> un nombre y ponerle uno inventado ensucia el dato. Los otros dos caminos no teclean nada.

---

### P3 · ¿Dónde vendes hoy? *(solo «Ya estoy vendiendo»)*

| Elemento | Contenido |
|---|---|
| Pregunta | `¿Dónde vendes hoy?` |
| Ayuda | `Puedes elegir más de una.` |
| Opciones (**selección múltiple**) | `En un local o punto de venta` · `Redes sociales` · `Marketplaces` · `Tienda en línea propia` · `A otros negocios / mayoreo` |
| Preseleccionada | *ninguna* |
| Botón izquierdo | `← Atrás` |
| Botón derecho | `Continuar` — **bloqueado** hasta marcar al menos una |
| Progreso | `3 de 4` |

- Las casillas son **cuadradas** (multi-selección), no redondas.
- En escritorio van en **dos columnas**. Como son cinco, **la última ocupa la fila completa** para
  no dejar un hueco.
- En celular van en **una columna**.
- Ninguna opción excluye a otra: se pueden marcar las cinco.

---

### P · ¿Qué vendes? — dos variantes de texto

Es la última pregunta de los dos caminos de negocio. **Sólo cambia el enunciado**; las opciones son
las mismas.

| | «Voy empezando» | «Ya estoy vendiendo» |
|---|---|---|
| Pregunta | `¿Qué vas a vender?` | `¿Qué vendes?` |
| Ayuda | `Con esto ajustamos tus tarifas.` | `Con esto ajustamos tus tarifas.` |
| Progreso | `3 de 3` | `4 de 4` |

| Elemento | Contenido |
|---|---|
| Opciones (**una sola**) | `Productos` · `Servicios` · `Ambos` |
| Preseleccionada | *ninguna* |
| Botón izquierdo | `← Atrás` |
| Botón derecho | `Guardar y empezar` — **bloqueado** hasta elegir una |

- Casillas **redondas** (selección única).
- En escritorio van en **tres columnas**; en celular en **una**.

---

### Cierre

Sin resumen de respuestas. Sólo la confirmación, el gancho de cashback y dos salidas.

| Elemento | Contenido |
|---|---|
| Ícono | Palomita verde en círculo verde claro |
| Título | `Tu cuenta está lista` |
| Texto | `Tu **primera recarga tiene cashback**. Úsalo en tu primer envío.` (las negritas van en «primera recarga tiene cashback») |
| Botón blanco | `Explorar` |
| Botón rojo | `Cotizar envío` |

- El contenido va **centrado vertical y horizontalmente** en el modal.
- No hay progreso, ni «Atrás», ni pie separado: los botones viven dentro del bloque centrado.

---

## 2.1 · Volver atrás y cambiar de respuesta

`← Atrás` aparece en todas las pantallas menos la primera. Regresa una pantalla y **conserva lo ya
contestado**. El caso interesante es volver hasta la primera pantalla y cambiar de tipo, porque eso
reescribe el recorrido completo. Está resuelto así:

| Situación | Qué pasa |
|---|---|
| El usuario **escribió** un nombre y luego cambia de tipo | **Se respeta lo que escribió.** No se sobrescribe nunca. |
| El nombre venía **prellenado** y no lo tocó, y cambia de tipo | Se reemplaza por el prellenado del tipo nuevo. De `Tienda de José Daniel` a vacío si elige «Ya estoy vendiendo». |
| Cambia de «Ya estoy vendiendo» a otro tipo | **Se borran los canales marcados**, porque esa pregunta deja de existir en el recorrido. |
| Cambia a «Uso personal» desde cualquier punto | El recorrido colapsa a **1 de 1** y el botón pasa a `Guardar y empezar`. |

**Al cambiar de tipo, el contador y la barra de progreso se recalculan de inmediato**, todavía en la
primera pantalla. Un usuario puede ver *1 de 4* y al tocar otra opción ver *1 de 1* sin cambiar de
pantalla.

---

## 3 · Estructura del modal

La misma en todas las pantallas salvo el cierre.

```
┌────────────────────────────────────────────┐
│  T1envíos          ▬▬▬▬▬▬▭▭▭▭▭   2 de 4    │  ← cabecera fija
├────────────────────────────────────────────┤
│                                            │
│  Te damos la bienvenida a T1envíos         │  ← sólo en P1
│  ¿Cómo se llama tu negocio?                │  ← pregunta
│  Así aparecerá en tus guías.               │  ← ayuda
│                                            │
│  ┌──────────────────────────────────────┐  │
│  │ Dulcería La Esquina                  │  │  ← control
│  └──────────────────────────────────────┘  │
│                                            │
│              (espacio en blanco)           │
│                                            │
├────────────────────────────────────────────┤
│  ← Atrás                     [ Continuar ] │  ← pie fijo
└────────────────────────────────────────────┘
```

**Tres zonas.** Cabecera y pie son **fijos**; sólo el centro cambia. El botón principal **nunca se
pierde de vista**, aunque el contenido creciera.

**La cabecera** lleva el logotipo `T1envíos` a la izquierda y, a la derecha, la barra de progreso
con el contador. No lleva título ni botón de cerrar. Es la misma en las cuatro pantallas.

**El pie** lleva `← Atrás` a la izquierda —ausente en la pantalla 1— y el botón principal a la
derecha.

---

## 4 · Medidas

Extraídas del prototipo. Todo en píxeles.

### Escritorio

| | |
|---|---|
| Marco de referencia | 1240 × 820 |
| **Modal** | **880 × 660**, alto **fijo** |
| Radio del modal | 16 |
| Sombra | `0 24px 60px rgba(31,41,55,.28)` |
| Velo | `rgba(31,41,55,.45)` + desenfoque de 3 px |
| Margen del velo | 22 |
| Posición | centrado vertical y horizontal |
| Cabecera | alto 72 · padding `26 56 22` · línea inferior 1 px `#E7E7E7` |
| Cuerpo | padding `44 56 36` |
| Pie | alto 99 · padding `22 56 30` · línea superior 1 px `#E7E7E7` |
| Ancho útil del contenido | 766 |

> **El alto es fijo a propósito.** Las cuatro pantallas comparten el mismo marco, así el aire
> sobrante se lee como espacio deliberado y el modal no salta de tamaño entre pasos.

### Celular

| | |
|---|---|
| Marco de referencia | 376 × 756 |
| **Modal** | ancho completo (360), **alto variable** hasta 93% de la pantalla |
| Radio | 18 arriba, 0 abajo — es una hoja anclada al borde inferior |
| Tirador | barra gris de 36 × 4, centrada, arriba de todo |
| Velo | igual que escritorio |
| Cabecera | alto 65 · padding `16 22 14` |
| Cuerpo | padding `20 22 24` |
| Pie | alto 85 · padding `16 22 22` |
| Ancho útil | 314 |
| Alto de la hoja, medido | 457 en P1 · 541 en canales — **varía con el contenido** |

**Altos reales del contenido, medidos:**

| Pantalla | Escritorio | Celular |
|---|---|---|
| P1 · tipo | 487 | 305 |
| P2 · nombre | 487 | 169–195 |
| P3 · canales | 487 | 389 |
| P · qué vendes | 487 | 275 |

> **Ninguna pantalla requiere desplazamiento**, ni en escritorio ni en celular, en ninguno de los
> tres caminos. Es un requisito, no una casualidad: si al diseñar crece el contenido, hay que
> volver a medirlo.

---

## 5 · Componentes

### Tipografía

Manrope en todo. Interlínea base 1.366.

| Rol | Escritorio | Celular | Peso | Color |
|---|---|---|---|---|
| Logotipo cabecera | 17 | 17 | 700 | `#1F2937`, el «1» en `#DB3B2B` |
| Contador de progreso | 11.5 mono | 11.5 mono | 500 | `#A3A3A3` |
| Línea de bienvenida | 13 | 13 | 500 | `#737373` |
| **Pregunta** | **27** | **22** | 700 | `#1F2937` |
| Ayuda | 14 | 13.5 | 400 | `#737373` |
| Texto de opción | 15 | 14.5 | 400 (600 al elegirse) | `#4C4C4C` (`#1F2937` al elegirse) |
| Texto del campo | 15 | 15 | 600 | `#1F2937` |
| Botón | 14 | 14 | 600 | blanco |

Interletraje de la pregunta: **−0.022em**. Es lo que la hace ver compacta y no estirada.

### Opción (tarjeta seleccionable)

| | Escritorio | Celular |
|---|---|---|
| Alto mínimo | 52 | 48 |
| Padding | `15 18` | `13 16` |
| Radio | 10 | 10 |
| Separación entre opciones | 10 | 9 |
| Separación marca–texto | 13 | 13 |

| Estado | Borde | Fondo | Texto |
|---|---|---|---|
| Normal | 1 px `#D9D9D9` | blanco | `#4C4C4C` peso 400 |
| Hover | 1 px `#4C4C4C` | blanco | igual |
| **Elegida** | 1 px `#DB3B2B` | `rgba(219,59,43,.06)` | `#1F2937` peso 600 |

**La marca** va a la izquierda, **19 × 19**, borde de 1.5 px `#D9D9D9`. Cambia de forma según el
tipo de selección:

| | Contorno | Al elegirse, relleno interior |
|---|---|---|
| **Selección única** (P1, ¿qué vendes?) | círculo | punto de **9 × 9**, redondo |
| **Selección múltiple** (¿dónde vendes hoy?) | cuadrado de **radio 4** | cuadro de **10 × 10**, radio 2 |

En los dos casos el borde pasa a `#DB3B2B` y el relleno es `#DB3B2B`.

### Campo de texto

| | |
|---|---|
| Alto | 56 |
| Padding | `0 18` |
| Radio | 10 |
| Con texto | fondo `#F8F8F8`, borde `#D9D9D9` |
| **Vacío** | fondo **blanco**, borde `#4C4C4C` — se lee como campo por llenar |
| Con foco | fondo blanco, borde `#4C4C4C` |
| Marca de agua | `#A3A3A3` |

### Botón principal

| | |
|---|---|
| Alto | 46 |
| Padding | `0 26` |
| Radio | 10 |
| Activo | fondo `#DB3B2B`, texto blanco, flecha `→` a la derecha |
| **Bloqueado** | fondo `#A3A3A3`, cursor de no permitido |

**«Atrás»** es texto plano con una flecha `←` a la izquierda, sin fondo ni borde, en `#4C4C4C`.

### Barra de progreso

Riel de 4 px de alto, radio 2, fondo `#E7E7E7`, ancho 169. Relleno `#DB3B2B` que crece con
transición de 260 ms. A la derecha, el contador en tipografía mono.

### Paleta

| Token | Valor | Uso |
|---|---|---|
| Rojo T1 | `#DB3B2B` | acento, selección, botón principal |
| Tinta | `#1F2937` | preguntas y texto elegido |
| Oxford | `#4C4C4C` | texto de opción, «Atrás» |
| Secundario | `#737373` | ayudas y bienvenida |
| Deshabilitado | `#A3A3A3` | marcas de agua, botón bloqueado |
| Borde | `#D9D9D9` | bordes de control |
| Línea | `#E7E7E7` | divisiones de cabecera y pie |
| Fondo suave | `#F8F8F8` | campo con texto |
| Verde | `#4FC153` sobre `#F0FDF4` | palomita del cierre |

---

## 6 · Movimiento

| Momento | Qué pasa |
|---|---|
| Aparece el modal | Velo con fundido de 180 ms. Escritorio: la tarjeta sube 10 px y escala de .985 a 1 en 220 ms. Celular: la hoja sube desde abajo en 260 ms. |
| Cambio de pantalla | El contenido entra desde la derecha, 12 px, 200 ms. La barra de progreso crece en 260 ms. |
| **Elegir una opción** | **Nada.** Sólo cambia el estado del control. |
| Escribir en el campo | Nada. |
| Cierre | La palomita entra con un rebote corto de 260 ms. |

> **La tercera línea es importante.** En una versión anterior cada clic reconstruía el modal y se
> veía un parpadeo. Elegir no debe animar nada.

Todo el movimiento se apaga con `prefers-reduced-motion`.

---

## 7 · Lo que NO lleva

Para que no haya dudas al diseñar:

- ❌ Botón «X» de cerrar
- ❌ Cerrar al hacer clic fuera del modal
- ❌ «Ahora no», «Omitir», «Lo hago después» ni ninguna otra salida
- ❌ Resumen de respuestas en el cierre
- ❌ Pregunta de industria o giro fino
- ❌ Pregunta de volumen o de ventas anuales
- ❌ Opción «Solo cobro» *(vive en T1 Pagos, no aquí)*
- ❌ Ilustraciones o imágenes dentro del modal

---

## 8 · Estados que hay que entregar

Para cada una de las 7 pantallas × 2 dispositivos:

1. **Al entrar** — como se ve la primera vez.
2. **Contestada** — con la opción elegida o el campo lleno.
3. **Botón bloqueado** — todas las pantallas menos P1 y la variante prellenada de P2 llegan con el
   botón en gris.

Y aparte:

4. **Hover** de una opción en escritorio.
5. **Foco de teclado** en opción, campo y botones — hoy es un contorno de 2 px en el rojo de acento
   `#DB3B2B`, con 2 px de separación y radio 3. Si prefieres un color distinto para que no se
   confunda con el estado elegido, dímelo y lo cambio.
6. **Campo vacío contra campo lleno** — cambian fondo y borde.

---

## 9 · Lo que falta decidir, y quién

Ninguno de estos bloquea el diseño visual, pero conviene que los sepas.

| Tema | Estado |
|---|---|
| **% de altas por Google/Apple sin nombre** | Sin medir. El dato vive en el identity hub y no he podido alcanzarlo. Si resultara alto, hay que definir un valor de respaldo (`Mi tienda`) para el prellenado. |
| **Cuentas creadas por un comercial** | Son pocas pero valiosas. La propuesta es no mostrarles el modal hasta el primer ingreso del dueño, para que el nombre no quede con el del empleado. Falta la bandera que marque esas cuentas. |
| **Reaparición del modal** | Se acordó que vuelva a salir si falta información, con disparador por número de envíos o por actividad continua. **Umbral sin definir**, y esa pantalla no está diseñada. |
| **Actualización de perfil** | Sin dueño ni definición. Alonso pidió que salga a más tardar un par de semanas después de la encuesta. |
| **Flujo de tienda con prompt** | Alonso lo señaló: quien crea su tienda con IA llega con datos ya inferidos, y el modal debería llegar prellenado mostrando sólo lo que falta. **No está contemplado en esta versión.** |
| **Instrumentación** | Requisito duro antes de construir: hoy medimos el abandono pantalla por pantalla porque cada paso tiene su propia URL. Un modal sin cambio de URL sólo se mide si emite eventos, con el momento como propiedad. |
| **A dónde llevan los dos botones del cierre** | Sin definir. `Cotizar envío` presumiblemente al cotizador y `Explorar` al panel, pero no está acordado. En el prototipo los dos simplemente cierran el modal. |

---

## 10 · Referencias

- **Prototipo navegable:** https://claude.ai/code/artifact/84c385a6-cf78-401e-a02f-2f500c6f021e
  Mueve el interruptor a **Opción A** y cambia entre escritorio y celular. Los tres caminos se
  recorren eligiendo distinto en la primera pantalla.
- **Benchmark:** capturas del onboarding real de Stripe, Tiendanube y Trigger.dev, dentro del
  prototipo.
- **Árbol de perfilamiento:** al final del prototipo, con las tres reglas de desempate del playbook.
- **Tokens del producto:** NEXUS V2.0.

Cualquier duda, o si al diseñar encuentras que algo no cierra, dime y lo resolvemos antes de que
llegue a desarrollo.
