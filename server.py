from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)

# Clave para manejar sesiones en Flask
app.secret_key = "clave_secreta_cambiar_en_produccion"

# Lista que generará los mensajes del destino
DESTINY_MESSAGES = [
    # Mensajes positivos
    "Tu **futuro** es brillante como una supernova. Una gran oportunidad laboral se presenta pronto. ¡Prepárate!",
    "El **universo** te sonríe. Recibirás un regalo inesperado o una noticia que cambiará tu día para bien.",
    "La **suerte** está de tu lado. Encontrarás algo que creías perdido y te traerá gran felicidad y paz.",
    "Tu **sabiduría** te guiará. Una decisión difícil resultará ser la correcta, trayendo prosperidad a tu vida.",
    
    # Mensajes de mala suerte/advertencia
    "Ten cuidado con tu **color** favorito, podría traerte un pequeño contratiempo. Mantente alerta hoy.",
    "Un **número** clave te alertará de un desafío, pero lo superarás con paciencia y esfuerzo constante.",
    "Tu **destino** te depara una pequeña confusión o retraso inesperado. La paciencia es tu mejor aliada.",
    "No confíes ciegamente. Una persona cercana podría no ser sincera. Mantén tus ojos abiertos."
]

# Ruta principal que muestra el formulario para ingresar datos
@app.route("/")
def mostrar_formulario():
    return render_template("index.html")

# Ruta para procesar los datos del formulario y almacenarlos en sesión
@app.route("/enviar", methods=["POST"])
def enviar_datos():
    """Recibe los datos del formulario, los almacena en 'session' y redirige a la ruta /futuro"""
    if request.method == "POST":
        session['nombre'] = request.form.get('nombre', 'Viajero Astral')
        session['color'] = request.form.get('color')
        session['numero'] = request.form.get('numero', '0')
        session['year'] = request.form.get('year')
        session['animal'] = request.form.get('animal')

        return redirect(url_for('mostrar_futuro'))
    return redirect(url_for('mostrar_formulario'))

# Ruta para mostrar la predicción del futuro basada en los datos ingresados
@app.route("/futuro")
def mostrar_futuro():
    # Verificar si el usuario ha pasado por el formulario
    if 'nombre' not in session:
        return redirect(url_for('mostrar_formulario'))
    
    nombre = session.get('nombre')
    color = session.get('color')
    numero = session.get('numero')
    year = session.get('year')
    animal = session.get('animal')

    # Generar predicción aleatoria
    prediccion_template = random.choice(DESTINY_MESSAGES)
    
    return render_template("futuro.html", 
                         prediccion=prediccion_template, 
                         nombre=nombre,
                         color=color,
                         numero=numero,
                         year=year,
                         animal=animal)

if __name__ == "__main__":
    app.run(debug=True)