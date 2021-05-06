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
                cost_matrix = get_cost_matrix()
                totalsales = 0
                for i in range(12):
                    for j in range(4):
                        current = reservation[i][j]
                        if current is 'X':
                            totalsales += cost_matrix[i][j]

                sales = "Total Sales:" + str(totalsales)
            else:
                message = 'Bad username/password combination. Try again.'

    return render_template("admin.html", form=form, template="form-template", message=message, reservation=reservation,
                           sales=sales)


def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix


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
    if request.method == 'GET':
        reservation = get_bus_map()
    if request.method == 'POST' and form.validate_on_submit():
        reservation = get_bus_map()
        course = 'INFOTC4320'
        first_name = form.first_name.data
        row = int(form.row.data) - 1
        seat = int(form.seat.data) - 1
        row = str(row)
        seat = str(seat)
        check = False
        requested_seat = str(row + ", " + seat)
        if requested_seat in open('reservations.txt').read():
            row = int(row) + 1
            seat = int(seat) + 1
            message = 'ERROR! Row: {} Seat: {} is already assigned. Choose Again.'.format(
                row, seat)
            return render_template("reservations.html", form=form, template="form-template",
                                   reservation=reservation, message=message)
        with open('reservations.txt', 'a') as writefile:
            if check is False:
                # Seat not reserved
                ticket = "".join([first_name[i] + course[i] for i in range(len(first_name))]) + course[len(first_name):]
                writefile.write("\n{}, {}, {}, {}".format(first_name, row, seat, ticket))
                row = int(row) + 1
                seat = int(seat) + 1
                message = 'Congratulations {}! Row: {} Seat: {} is now reserved for you! Enjoy the Trip\nYour e-ticket ' \
                          'number is: {}'.format(first_name, row, seat, ticket)
                reservation = get_bus_map()
                return render_template("reservations.html", form=form, template="form-template",
                                       reservation=reservation,
                                       message=message)

    return render_template("reservations.html", form=form, template="form-template", reservation=reservation)
