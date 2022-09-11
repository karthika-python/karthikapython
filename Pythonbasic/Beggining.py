class class1():
    global command
    global started
    global stop
    started = False
    stop = False
    def carfunction(self,command):
        if command == "start":
            if started:
                print("Car already started")
            else:
                self.started = True
                print("Car started")
        elif command == "stop":
            if stop:
                print("Car already stopped")
            else:
                self.stop= True
                print("Car stopped")
        elif command == "help":
            print('''Start means car started.Stop means car stops and quit means quit''')
        elif command == "quit":
            print("You Quit")
        else:
            print("Sorry Dont understand")
obj1=class1()
obj1.carfunction("start")
obj1.carfunction("stop")
obj1.carfunction("quit")
obj1.carfunction("help")
obj1.carfunction("start")



'''creditscore=input("Enter the creditscore : ")
    Propertycost=input("Enter the property value")

    def downpay(self):
        if int(self.creditscore)>=850:
            downpayment=0.1*int(self.Propertycost)
            print("downpayment for your property is : " +str(downpayment))
        else:
            downpayment=0.2*int(self.Propertycost)
            print("downpayment for your property is : " +str(downpayment))
   propertycost=1000000
   creditscore=False
   def downpay(self):
       if self.creditscore:
           downpayment=0.1*self.propertycost
       else:
           downpayment=0.2*self.propertycost
       print(f"your downpayment is: $ {downpayment}")'''













