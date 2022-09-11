class transport():
    global ticketcost
    #global age
    global discount
    ticketcost = 100
    #age =60
    discount = 0.1
    def female(self,gender,modeoftransport,nooftickets):
        if gender == "F" and modeoftransport == "bus":
            print("Transportation is free for female. Congrats! You are free to travel")
            #return gender
    def male(self,gender,modeoftransport,nooftickets):
        age=input("enter age : ")
        a=int(age)
        if gender == "M" and modeoftransport == "bus" and a >= 60:
            amount = (ticketcost * nooftickets)-(ticketcost * nooftickets * discount)
            print("Hey Man your ticket amount with discount is " + str(amount))
        else:
            amount = ticketcost * nooftickets
            print("Hey Man your not eligible for discount and ur ticket amount without discount is " + str(amount))
            #return gender

    def transgender(self, gender, modeoftransport, nooftickets):
        if gender == "T" and modeoftransport == "bus":
            amount = ticketcost * nooftickets
            print("Hey Man your not eligible for discount and ur ticket amount with discount is " + str(amount))
            #return gender

travel1=transport()
travel1.female("F","bus",2)
travel1.transgender("T","bus",2)
travel1.male("M", "bus", 2)





