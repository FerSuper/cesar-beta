@app.route("/")
def home():
    return """
return """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CÉSAR IA Beta</title>
  <style>
    body {
      background-color: #121212;
      color: #00ffc8;
      font-family: Arial, sans-serif;
      text-align: center;
      padding-top: 20vh;
    }
    .modal {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0, 0, 0, 0.85);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 9999;
    }
    .modal-content {
      background: #ffffff;
      color: #000;
      padding: 2rem;
      border-radius: 10px;
      max-width: 600px;
      text-align: center;
      box-shadow: 0 0 30px #00ffc8;
    }
    button {
      padding: 10px 20px;
      background-color: #00ffc8;
      border: none;
      color: #000;
      font-weight: bold;
      cursor: pointer;
      margin-top: 1rem;
    }
    footer {
      background-color: #111;
      color: #ccc;
      text-align: center;
      padding: 1rem;
      font-size: 0.9rem;
      position: fixed;
      bottom: 0;
      width: 100%;
    }
    .hidden { display: none; }
  </style>
</head>
<body>

<div class="modal" id="modal">
  <div class="modal-content">
    <h2>Términos y Condiciones</h2>
    <p>Al usar este servicio aceptás que:</p>
    <ul style="text-align: left;">
      <li>No damos consejos médicos, legales ni financieros.</li>
      <li>Las respuestas pueden contener errores.</li>
      <li>No usarás el sistema con fines ilegales, violentos o discriminatorios.</li>
      <li>No copiás, modificás ni revendés el sistema.</li

    """
