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
    
    seating_chart = get_bus_map() # Gets seating chart and puts it into variable that is then
                                    # used to fill data in template below. Joseph Collins
        
    # Haven't implemented any code to keep table from displaying if login hasn't been 
      # achieved. Joseph Collins
        
    return render_template("admin.html", form=form, data=seating_chart, template="form-template") # Table display data was added to corresponding html pages. Joseph Collins

def get_bus_map(): # Method to return bus seating chart from reservations.txt
    bus_map = [['O']*4 for row in range(12)]
    with open("reservations.txt","r") as file:
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
    
    seating_chart = get_bus_map() # Gets seating chart and puts it into variable that is then
                                    # used to fill data in template below. Joseph Collins
    
    return render_template("reservations.html", form=form, data=seating_chart, template="form-template") # Table display data was added to corresponding html pages. Joseph Collins

