@app.route("/terminos")
def terminos():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Términos y Condiciones</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                padding: 2rem;
                background-color: #f5f5f5;
                color: #222;
                line-height: 1.6;
            }
            h1 {
                color: #111;
            }
        </style>
    </head>
    <body>
        <h1>Términos y Condiciones de CÉSAR IA</h1>
        <p>Versión completa disponible en PDF.<br>
        Última actualización: 26 de marzo de 2025</p>
        <p>Puedes descargar los términos completos desde el siguiente enlace:</p>
        <a href="https://cesar.net.ar/static/Terminos_y_Condiciones_CESAR_IA_Final_Total.pdf" target="_blank">📄 Descargar PDF</a>
    </body>
    </html>
    """
