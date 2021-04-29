from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

from .forms import *


#@app.route("/", methods=['GET', 'POST'])
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
    if request.method == 'POST'and form.validate_on_submit():
# admin1, 12345
# admin2, 24680
# admin3, 98765
        if form.username.data == 'admin1' and form.password.data == '12345' or form.username.data == 'admin2' and form.password.data == '24680' or form.username == 'admin3' and form.password.data == '98765':
            message = 'Printing Seating Chart...'
            #load reservation chart
            #load total sales
        else:
            message = 'Bad username/password combination. Try again.'
   

    return render_template("admin.html", form=form, template="form-template", message=message)

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():

    form = ReservationForm()

    return render_template("reservations.html", form=form, template="form-template")

