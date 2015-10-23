# -*- coding: utf-8 -*-

from flask import Flask, render_template

from trafiklab.sl import sites, trains, buses

app = Flask(__name__)


@app.route('/')
def busstop():
    return render_template('index.html', departurest=trains(9521), departuresb=buses(7571))


#Site-ID
@app.route('/sites')
def sitessearch():

    sitelist = sites(("Balticvagen"))

    return    str(sitelist)


if __name__ == '__main__':
   # app.debug=True
    app.run()
