from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
@app.route('/Home')
def Inicio():
    return render_template('Inicio.html')

@app.route('/<name>')
def render(name):
    return render_template('InfoFilmes.html', name=name)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80) #Necessário para o replit
