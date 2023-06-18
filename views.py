from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    flash("Hi there, what is your name?")
    return render_template("index.html")

@views.route("/greet", methods=["POST","GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", nice to meet you!")
    return render_template("index.html")