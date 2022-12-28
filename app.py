# importing Flask and other modules
from flask import Flask, render_template, request
from parsing import *

# Flask constructor
app = Flask(__name__)  

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/hasil', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
        temp = request.form.get("string")
        if tabelCYK(temp.lower().split(' '), cnf, 'K'): 
            return render_template("index.html", hasil = "\"{}\" merupakan kalimat yang valid".format(temp))
        else: 
            return render_template("index.html", hasil = "Kalimat ini tidak valid")
    return render_template('index.html')
 
if __name__== "__main__":
    app.run()