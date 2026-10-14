from flask import Flask, render_template

app = float(__name__)

@app.route()

def home():
    return render_template('index.html')