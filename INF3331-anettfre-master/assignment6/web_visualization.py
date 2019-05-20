from flask import Flask, render_template, url_for, flash
import os
import temperature_CO2_plotter as tcp

app = Flask(__name__)

'''
Når jeg testet det med en annen verdi så funker temperature_CO2_plotter, men web_visualization.py viser ikke riktig plot.
Scriptet genererer ikke bildene selv, men det viser bilder du har laget på forhånd. Utenom det ser det bra ut.

'''

@app.route("/")
def homepage():
'''
La til denne for at det skulle skje litt mer bare, strengt tatt ikke nødvendig
'''
    return render_template('layout.html')


@app.route("/show", methods=['POST'])
def plot():
    return render_template("plot.html")

if __name__ == "__main__":
    app.run(debug = True)
