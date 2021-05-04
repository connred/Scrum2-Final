from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

from .forms import *


# @app.route("/", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def user_options():
    form = UserOptionForm()
    if request.method == 'POST' and form.validate_on_submit():
        option = request.form['option']

        if option == "1":
            return redirect('/admin')
        else:
            return redirect("/reservations")

    return render_template("options.html", form=form, template="form-template")


@app.route("/admin", methods=['GET', 'POST'])
def admin():
    form = AdminLoginForm()

    message = None
    reservation = None
    sales = None

    username = form.username.data
    password = form.password.data

    if request.method == 'POST' and form.validate_on_submit():
        with open('passcodes.txt') as file:
            passcodes = file.read()
            login_info = username + ", " + password
            if login_info in passcodes:
                message = 'Printing Seating Chart...'
                reservation = get_bus_map()
                sales = "Total Sales:"
            else:
                message = 'Bad username/password combination. Try again.'

    return render_template("admin.html", form=form, template="form-template", message=message, reservation=reservation,
                           sales=sales)


def get_bus_map():  # Method to return bus seating chart from reservations.txt
    bus_map = [['O'] * 4 for row in range(12)]
    with open("reservations.txt", "r") as file:
        for line in file:
            string = line.split(",")
            row = int(string[1])
            seat = int(string[2])
            bus_map[row][seat] = 'X'
    file.close()
    return bus_map


@app.route("/reservations", methods=['GET', 'POST'])
def reservations():
    form = ReservationForm()

    return render_template("reservations.html", form=form, template="form-template")
