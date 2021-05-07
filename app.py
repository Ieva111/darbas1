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

@app.route('/irankis')
def irankis():
    return render_template('irankis.html')

if __name__ == '__main__':
    app.run(debug=True)
