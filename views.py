from flask import Blueprint, render_template, request
from forms import ContactForm
import pandas as pd

views = Blueprint(__name__, "views")


@views.route("/", methods=["POST", "GET"])
def home():
    form = ContactForm()
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        res = pd.DataFrame(
            {"name": name, "email": email, "subject": subject, "message": message},
            index=[0],
        )
        res.to_csv("./contactusMessage.csv")
        print("The data are saved !")
    else:
        return render_template("index.html", form=form)

    return render_template("index.html", form=form)
