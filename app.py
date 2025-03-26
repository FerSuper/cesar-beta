@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>César IA Beta</title>
        <style>
            body {
                background-color: #121212;
                color: #00ffc8;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 20vh;
            }
            h1 {
                font-size: 2.5em;
            }
            p {
                font-size: 1.2em;
                color: #ccc;
            }
        </style>
    </head>
    <body>
        <h1>César IA - Página de Prueba</h1>
        <p>Estamos configurando todo para que tengas la mejor experiencia en inteligencia artificial.</p>
    </body>
    </html>
    """
