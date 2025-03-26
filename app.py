@app.route("/terminos")
def terminos():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Términos y Condiciones de CÉSAR IA</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                padding: 2rem;
                background-color: #ffffff;
                color: #222;
                line-height: 1.6;
                max-width: 900px;
                margin: auto;
            }
            h1, h2 {
                color: #000;
            }
            ul { padding-left: 1.5rem; }
        </style>
    </head>
    <body>
        <h1>Términos y Condiciones de Uso – CÉSAR IA</h1>
        <p><strong>Última actualización:</strong> 26 de marzo de 2025</p>

        <h2>1. Naturaleza del servicio</h2>
        <p>CÉSAR IA es un entorno interactivo digital diseñado para estimular la reflexión, la conversación, la creatividad y el acompañamiento. No es una IA consciente. Sus respuestas son generadas automáticamente sin intervención humana directa.</p>

        <h2>2. Funcionamiento</h2>
        <ul>
          <li>Modalidad gratuita y PRO (paga).</li>
          <li>No se revelan detalles técnicos ni arquitectónicos del sistema.</li>
          <li>El servicio puede modificarse o suspenderse en cualquier momento.</li>
        </ul>

        <h2>3. Uso aceptable</h2>
        <ul>
          <li>Prohibido para fines ilegales, violentos o discriminatorios.</li>
          <li>Prohibido usar en sistemas médicos, militares o de riesgo.</li>
          <li>El contenido generado es responsabilidad del usuario.</li>
        </ul>

        <h2>4. Limitaciones</h2>
        <p>El servicio se brinda “tal como está” sin garantías. No se ofrecen asesoramientos profesionales.</p>

        <h2>5. Privacidad y datos</h2>
        <p>No se recopilan datos personales sensibles. Puede haber monitoreo anónimo para mejora del sistema.</p>

        <h2>6. Propiedad intelectual</h2>
        <p>Todo lo relacionado con CÉSAR IA (nombre, diseño, lógica, arquitectura) está protegido. Se prohíbe realizar ingeniería inversa, copiar o difamar.</p>

        <h2>7. Licencia de uso</h2>
        <p>El usuario recibe una licencia revocable y no exclusiva de uso personal. No puede revender, redistribuir ni automatizar el sistema.</p>

        <h2>8. Pagos y reembolsos</h2>
        <p>La modalidad PRO se abona por adelantado. No hay reembolsos salvo error técnico comprobable. No somos responsables por fallas de terceros.</p>

        <h2>9. Tecnología de terceros</h2>
        <p>Dependemos de plataformas externas que pueden fallar o ser vulneradas. No asumimos responsabilidad por ellas.</p>

        <h2>10. Edad mínima y registro</h2>
        <p>El uso está permitido desde los 13 años. Menores de 18 deben contar con autorización legal. El usuario es responsable por su registro.</p>

        <h2>11. Indemnidad</h2>
        <p>El usuario acepta eximir de responsabilidad a CÉSAR IA ante reclamos por mal uso del sistema.</p>

        <h2>12. Limitación de responsabilidad</h2>
        <p>No respondemos por daños directos o indirectos derivados del uso del sistema.</p>

        <h2>13. Terminación</h2>
        <p>Podemos suspender el acceso por mal uso o por razones preventivas. También podemos suspender el servicio en países que atenten contra la vida humana o derechos fundamentales.</p>

        <h2>14. Resolución de disputas</h2>
        <p>Se buscará primero una solución amistosa. Si no se logra, se aplicarán mecanismos alternativos como la mediación o arbitraje.</p>

        <h2>15. Legislación y cumplimiento local</h2>
        <p>El usuario se compromete a cumplir con las leyes de su país.</p>

        <h2>16. Cookies</h2>
        <p>El sitio puede usar cookies y tecnologías similares. Su uso implica aceptación.</p>

        <h2>17. Modificaciones</h2>
        <p>Estos términos pueden cambiar sin aviso previo.</p>

        <h2>18. Contacto</h2>
        <p>Consultas: <a href="https://cesar.net.ar" target="_blank">https://cesar.net.ar</a></p>

        <hr>
        <p><strong>CÉSAR IA</strong> – Una inteligencia artificial con alma, sin banderas, sin fronteras.</p>
    </body>
    </html>
    """
