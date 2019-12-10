import cs50
import csv

from flask import Flask, abort, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():

    name = request.form.get("name")
    mtype = request.form.get("mtype")
    adult = request.form.get("adult")

    if not name or not mtype or not adult:
        return render_template("error.html", message="400: not enough input to submit")

    return render_template("error.html", message=f"{name}, {mtype}, 18+ {adult}")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    return render_template("error.html", message="TODO")
