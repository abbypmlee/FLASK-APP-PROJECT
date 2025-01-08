from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) #crear el objeto de la aplicación

#página de introducción
@app.route('/')
def index():
    return render_template('index.html')

#dirigiendo la página a la ruta correcta 
@app.route('/bienvenidos', methods=['GET', 'POST'])
def bienvenidos():
    bienvenidos = request.form.get('bienvenidos')
    return redirect(url_for('saludo', person_id=bienvenidos))

#definiendo una función para dirigir a cada plantilla
@app.route('/saludo/<person_id>', methods=['GET', 'POST'])
def saludo(person_id):
    if person_id == "1":
        return render_template('rodaja.html', name="Tomás Rodaja")
    elif person_id == "2":
        return render_template('erauso.html', name="Antonio Erauso")
    elif person_id == "3":
        return render_template('marina.html', name="Marina de Sant Miguel")

#las respuestas de Rodaja
@app.route('/rodaja', methods=['GET', 'POST'])
def rodaja():
    choice = request.form.get('choice')
    if choice == "1":
        response = "Dile que dé gracias a Dios por haber permitido le llevasen de casa a su enemigo."
    elif choice == "2":
        response = "De salud estoy neutral, porque están encontrados mis pulsos con mi celebro."
    elif choice == "3":
        response = "A la ciencia, en mucha; pero que a los poetas, en ninguna."
    elif choice == "4":
        response = "¡Nemo, por supuesto! Nemo novit Patrem, Nemo sine crimine vivit, Nemo sua sorte contentus."
    elif choice == "5":
        response = "La temprana y agradecida, seguro. De Madrid, cielo y suelo; de Valladolid, los entresuelos."
    else:
        response = "No tiene usted sentido... debes ser murmuradora." #nunca aparece; solo lo usé cuando estaba escribiendolo al principio 
    return render_template('response.html', response=response)

#las respuestas de Erauso
@app.route('/erauso', methods=['GET', 'POST'])
def erauso():
    choice = request.form.get('choice')
    if choice == "1":
        response = "Si quieres oír del Capítan Miguel de Erauso... ¡Cómo me arrepiento de lo que hice!"
    elif choice == "2":
        response = "No recuerdo mucho antes del convento—que lugar tan horrible!"
    elif choice == "3":
        response = "He servido como asistente para un comerciante, he trabajado en una tienda, he cuidado por ovejas."
    elif choice == "4":
        response = "Los Indies siempre me han fascinado. Sin embargo, la costa mía de San Sebastián me llama."
    elif choice == "5":
        response = "Justo antes de mi muerto serví como arriero—encontré las mulas más agradables que las personas."
    else:
        response = "Seguro que está aquí para atacarme!" #la misma que lo de Rodaja
    return render_template('response.html', response=response)

#Las respuestas de Marina
@app.route('/marina', methods=['GET', 'POST'])
def marina():
    choice = request.form.get('choice')
    if choice == "1":
        response = "¡Por supuesto! Fui confirmado por un obispo, frey del orden del Santo Domingo."
    elif choice == "2":
        response = "Nací en Córdoba, pero viajé para esta ciudad cuando tenía tres años."
    elif choice == "3":
        response = "Soy una mujer honesta y religiosa! ¿Por qué me miras así?"
    elif choice == "4":
        response = "SOY UNA PECADORA Y ABOMINACION DEL NOMBRE BUENO DE LA RELIGION."
    elif choice == "5":
        response = "Ay que tremor siento en mis piernas... espera.. mi dulce Jésus."
    else:
        response = "Por favor, ¡pregúntáme cualquier cosa y te responderé para mostrar mi inocencia!" #la misma que lo de Rodaja
    return render_template('response.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)