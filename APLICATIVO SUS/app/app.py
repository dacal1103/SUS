from flask import Flask, render_template, request, redirect, url_for, flash, jsonify



app = Flask(__name__)





@app.route('/')
def inicio():
    return render_template('INGRESAR.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
@app.route('/servicios', methods=['GET', 'POST'])
def reporte():
    return render_template('SERVICIOS.html')

@app.route('/map', methods=['GET', 'POST'])
def mapa():
    return render_template('MAP.html')


if __name__ == '__main__':
    app.run(debug=True)





