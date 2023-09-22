from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def flask_first():
    return "este é meu primeiro programa flask"

@app.route("/vitor")
def flask_second():
    return"sou programador"

@app.route("/index")
def flask_third_webpage():
    return render_template('index.html')

app.run(debug=True)