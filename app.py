import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = "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"


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            engine="text-davinci-001",
            prompt=generate_prompt(animal),
            temperature=0.6,
            max_tokens=90
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Artikel Die Der oder Das.


hint: Haus
pickupline:  Das Haus.

hint: Mutter 
pickupline: Die Mutter.
hint: {}
pickupline:""".format(
        animal.capitalize()
    )
