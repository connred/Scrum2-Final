#https://stackoverflow.com/questions/45261003/return-true-if-the-input-file-contains-in-every-line-otherwise-return-false

firstName = "Brian" 
lastName = "Jiang"
row = 0 
seat = 4

def seat_availability(row, seat):
    with open("reservations.txt", "r") as inputFile:
        for line in inputFile:
            test = "{}, {}".format(row, seat)
            if test not in line:
                flag = True
            else:
                return True
    if flag:
        return False


def reservations(firstName, row, seat):
    with open('reservations.txt', 'r') as readfile:
        course = "INFOTC4320"
        ticket = "".join([firstName[i] + course[i] for i in range(len(firstName))]) + course[len(firstName):]
        multiplelines = readfile.readlines()
        test = "{}, {}".format(row, seat)

    with open('reservations.txt', 'a+') as writefile:
        
        if seat_availability(row, seat):
            return "<p>This seat has already been taken.</p>"
        
        else:
            print("Seat Reserved!")
            writefile.write("\n{}, {}, {}, {}".format(firstName, row, seat, ticket))
               
print(reservations(firstName, row, seat))

