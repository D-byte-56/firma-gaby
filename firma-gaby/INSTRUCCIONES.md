# Firma de correo — Gaby Orona

## Qué hay en la carpeta

| Archivo | Para qué sirve |
|---|---|
| `plantilla-firma.html` | La firma (tablas y estilos en línea, compatible con Gmail, Apple Mail y Outlook). Tiene dos marcadores: `{{BASE}}` (dónde están las imágenes) y `{{BOTON}}` (a dónde lleva el botón). |
| `imagenes/` | Foto, logo e íconos en PNG (Gmail y Outlook no muestran SVG). Están a doble resolución para que se vean nítidos en el teléfono. |
| `generar.py` | Llena los marcadores y crea `firma.html` + `index.html`. |
| `firma-texto.txt` | Versión en texto plano para la app de Gmail. |

## Enlaces que ya trae
- Teléfono → `tel:+18018849511` (en el teléfono abre la llamada)
- Correo → `mailto:oronarealestate@gmail.com`
- Instagram → `instagram.com/GabyOronaRealtor`
- Botón "Book a consultation" → abre WhatsApp con Gaby (`wa.me/18018849511`) con este mensaje ya escrito: "Hola Gaby, me gustaría agendar una consulta. / Hi Gaby, I'd like to book a consultation." Si su WhatsApp es otro número, se cambia en `generar.py`.

## Paso 1 — Subir todo a GitHub Pages (obligatorio, es gratis)
Una firma de correo **no puede llevar las imágenes dentro**: Gmail y la mayoría de apps bloquean las imágenes incrustadas. Tienen que estar en un enlace público, y GitHub Pages sirve perfecto.

1. Primero genera la firma con la dirección que va a tener tu GitHub Pages (cambia `TU-USUARIO`):
   ```bash
   python3 generar.py https://TU-USUARIO.github.io/firma-gaby/imagenes/
   ```
2. En GitHub crea un repositorio **público** llamado `firma-gaby` (Pages gratis solo funciona con repos públicos).
3. Sube `index.html`, `firma.html` y la carpeta `imagenes/` (con **Add file → Upload files** o con git).
4. En el repo: **Settings → Pages → Source: Deploy from a branch → Branch: `main` / `(root)` → Save**.
5. Espera 1–2 minutos y verifica que abran:
   - `https://TU-USUARIO.github.io/firma-gaby/` (la página con la firma)
   - `https://TU-USUARIO.github.io/firma-gaby/imagenes/foto-gaby.png`

> Usa la dirección de **github.io**, no la de `github.com/.../blob/...`: esa es una página de GitHub, no la imagen, y en el correo saldría rota. Tampoco renombres ni borres el repo después, porque las firmas ya enviadas dejarían de mostrar las imágenes.

## Paso 3 — Instalarla desde el teléfono (sin computadora)
Ella solo abre `https://TU-USUARIO.github.io/firma-gaby/` en el teléfono. La página tiene la firma, un botón **Copiar firma** y los pasos escritos.

### Opción A (recomendada) — App de Gmail, funciona en iPhone y Samsung
La app de Gmail no deja pegar firmas con imágenes, **pero** según Google: *"si no creas una firma en la app de Gmail, los mensajes nuevos usan la firma que configuraste en la computadora"*. Esa firma de "computadora" sí acepta imágenes, y se puede configurar desde el navegador del teléfono:
1. Tocar **Copiar firma** en la página.
2. Abrir **mail.google.com** en Chrome o Safari y activar **Sitio de escritorio** (Chrome: menú ⋮ → "Sitio de escritorio"; Safari: botón **aA** → "Solicitar sitio de escritorio").
3. ⚙️ → **Ver toda la configuración** → **Firma** → **Crear nueva** → pegar → elegirla en "Para correos nuevos" y "Para respuestas" → **Guardar cambios** (al final de la página).
4. En la app de Gmail: ☰ → Configuración → su cuenta → **Firma móvil** → apagada o vacía.
5. Mandarse un correo de prueba y revisar que lleguen la foto, los enlaces y el botón de WhatsApp.

> Puede que mientras escribe en la app no vea la firma; lo que importa es cómo llega el correo. Por eso es clave el correo de prueba.

### Opción B — App Mail del iPhone
1. Tocar **Copiar firma**.
2. Ajustes → Apps → Mail → **Firma** → borrar lo que haya y pegar.
3. Si se pega sin diseño: agitar el iPhone → **Deshacer**.

### App Samsung Email: no recomendada
No acepta bien firmas con imágenes. En Samsung es mejor usar la **app de Gmail** (Opción A).

### Plan B si algo falla
`firma-texto.txt` es una versión solo con texto que funciona en cualquier app (Firma móvil de Gmail o firma de Samsung). Con esa el teléfono y el correo igual se pueden tocar, pero no lleva la foto ni el logo.

## Para cambiar algo después
Se edita `plantilla-firma.html` y se vuelve a correr `generar.py`. Los colores son `#D2621F` (nombre, línea, íconos) y `#C95A1F` (botón y frase).
