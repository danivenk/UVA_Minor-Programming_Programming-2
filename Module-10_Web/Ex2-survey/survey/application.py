#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
version: python 3+
application.py creates a survey application using flask
Dani van Enk, 11823526
"""

# import libraries
import cs50
import csv

from flask import Flask, abort, jsonify, redirect, render_template, request
from html import escape
from werkzeug.exceptions import default_exceptions, HTTPException


# Configure application
app = Flask(__name__)


# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """
    Disable caching

    parameter:
    response

    returns a response
    """
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    """
    redirects from / to /form

    returns a redirect
    """

    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    """
    render form.html

    returns the form template
    """

    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    """
    add form submission to csv-file and render sheet

    returns the sheet template
    """

    # get values from submitted form
    name = request.form.get("name")
    mtype = request.form.get("mtype")
    adult = request.form.get("adult")

    # make sure the required values are given else give 400 error
    if not name or not mtype:
        abort(400, "not enough input to submit")

    # change adult to no if checkbox was empty
    if not adult:
        adult = "no"

    # prepare data matrix
    csv_data = []

    # open survey data file
    with open("survey.csv", "r+", newline="") as file:

        # make reader object
        reader = csv.reader(file)

        # read all rows in the data file and add them to the data matrix
        for row in reader:
            csv_data.append(row)

        # check if the csv header is present
        if csv_data[0] != ["Name", "Media Type", "For adults"]:
            csv_data.insert(0, ["Name", "Media Type", "For adults"])

        # add submission to data matrix
        csv_data.append([name, mtype, adult])

        # go back to start of the data file
        file.seek(0)

        # make writer object
        writer = csv.writer(file)

        # write every row from the data matrix to the data file
        for csv_line in csv_data:
            writer.writerow(csv_line)

    return render_template("sheet.html", data=csv_data)


@app.route("/sheet", methods=["GET"])
def get_sheet():
    """
    render sheet form data file

    return the sheet template
    """

    # prepare data matrix
    csv_data = []

    # open survey data file
    with open("survey.csv", "r", newline="") as file:

        # make reader object
        reader = csv.reader(file)

        # read all rows in the data file and add them to the data matrix
        for row in reader:
            csv_data.append(row)

        # check if the csv header is present
        if csv_data[0] != ["Name", "Media Type", "For adults"]:
            csv_data.insert(0, ["Name", "Media Type", "For adults"])

    return render_template("sheet.html", data=csv_data)


@app.errorhandler(HTTPException)
def errorhandler(error):
    """
    Handle errors

    used same code as in the exercise similarities

    return error template
    """

    return render_template("error.html", message=error), error.code


# https://github.com/pallets/flask/pull/2314
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
