"""Genera la firma final con las URLs reales de las imágenes.
Uso:  python3 generar.py https://tudominio.com/firma-gaby/  [URL_DEL_BOTON]
"""
import sys
base = sys.argv[1] if len(sys.argv) > 1 else 'imagenes/'
if not base.endswith('/'): base += '/'
boton = sys.argv[2] if len(sys.argv) > 2 else 'https://wa.me/18018849511?text=Hola%20Gaby%2C%20me%20gustar%C3%ADa%20agendar%20una%20consulta.%20/%20Hi%20Gaby%2C%20I%27d%20like%20to%20book%20a%20consultation.'
t = open('plantilla-firma.html', encoding='utf-8').read().replace('{{BASE}}', base).replace('{{BOTON}}', boton)
open('firma.html', 'w', encoding='utf-8').write(t)
pagina = """<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Firma Gaby Orona</title>
<style>
body{margin:0;padding:10px;background:#f6f3f0;font-family:Arial,Helvetica,sans-serif;color:#222}
.caja{background:#fff;border-radius:12px;padding:16px;max-width:460px;margin:0 auto 14px;box-shadow:0 1px 4px rgba(0,0,0,.08)}
button{display:block;width:100%;max-width:460px;margin:0 auto 14px;padding:16px;border:0;border-radius:10px;background:#C95A1F;color:#fff;font-size:17px;font-weight:bold}
button.ok{background:#2e7d32}
h2{font-size:16px;margin:0 0 8px;color:#C95A1F}
ol{margin:0;padding-left:20px;font-size:14px;line-height:1.5}
#firma{padding:12px 6px}</style></head><body>
<div class="caja" id="firma">__FIRMA__</div>
<button id="copiar">Copiar firma</button>
<div class="caja"><h2>App de Gmail (iPhone o Samsung)</h2><ol>
<li>Toca <b>Copiar firma</b>.</li>
<li>Abre <b>mail.google.com</b> en Chrome o Safari y activa <b>Sitio de escritorio / Versión para computadora</b>.</li>
<li>&#9881; Configuración &rarr; Ver toda la configuración &rarr; <b>Firma</b> &rarr; Crear nueva &rarr; pega &rarr; elígela en <i>"Para correos nuevos"</i> y <i>"Para respuestas"</i> &rarr; <b>Guardar cambios</b> (al final).</li>
<li>En la app de Gmail: Configuración &rarr; tu cuenta &rarr; <b>Firma móvil</b> &rarr; apagada o vacía.</li>
<li>Envíate un correo de prueba.</li></ol></div>
<div class="caja"><h2>App Mail del iPhone</h2><ol>
<li>Toca <b>Copiar firma</b>.</li>
<li>Ajustes &rarr; Apps &rarr; Mail &rarr; <b>Firma</b> &rarr; borra lo que haya y pega.</li>
<li>Si se pega sin diseño: agita el iPhone &rarr; <b>Deshacer</b>.</li></ol></div>
<script>
document.getElementById('copiar').onclick=async function(){
  var b=this, el=document.getElementById('firma'), html=el.innerHTML, txt=el.innerText;
  try{
    await navigator.clipboard.write([new ClipboardItem({'text/html':new Blob([html],{type:'text/html'}),'text/plain':new Blob([txt],{type:'text/plain'})})]);
  }catch(e){
    var r=document.createRange(); r.selectNodeContents(el); var s=getSelection(); s.removeAllRanges(); s.addRange(r);
    try{document.execCommand('copy');}catch(_){}
    s.removeAllRanges();
  }
  b.textContent='¡Copiada! Ahora pégala'; b.className='ok';
  setTimeout(function(){b.textContent='Copiar firma';b.className='';},3000);
};
</script></body></html>""".replace('__FIRMA__', t)
open('index.html', 'w', encoding='utf-8').write(pagina)
print('Listo: firma.html e index.html con base =', base)
