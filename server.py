#!flask/bin/python
# coding=utf-8
from flask import Flask, request, redirect, url_for, render_template
from pytechlag.pytechlag import TechLag

app = Flask(__name__)

@app.route('/', strict_slashes=False, methods=['GET', 'POST'])
def basic_info(err=None):
    if request.method == 'POST':
        print("POST")
        tl = TechLag(package=request.form['package'], version=request.form['version'], kind=request.form["kind"])
        tl.analyze()
    return render_template('form.html', err=err)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug="True", port=5050)