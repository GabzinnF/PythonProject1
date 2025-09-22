from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/animal')
def animal():
    return render_template('animal.html')
@app.route('/pessoa')
def pessoa():
    return render_template('pessoa.html')

if __name__ == '__main__':
    app.run(debug=True)