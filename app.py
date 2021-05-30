
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def darbas():
    return render_template('darbas.html')

@app.route('/klausimynas')
def klausimynas():
    return render_template('klaus.html')

@app.route('/duk')
def duk():
    return render_template('duk.html')

@app.route('/rezultatas')
def rez():
    return render_template('rezultatas.html')

@app.route('/rezultatas1')
def rez1():
    return render_template('rezultatas1.html')

@app.route('/rezultatas2')
def rez2():
    return render_template('rezultatas2.html')

@app.route('/irankis')
def irankis():
    return render_template('irankis.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
