from Pythonbasic.Hotelname import hotelname
from Pythonbasic.Itemcost import costs

class orders(hotelname,costs):
    global discount
    discount= 0.1
    global no_of_item
    def orderfood(self,no_of_item):
        while int(no_of_item>=1):
            items= input("Enter the food Item : ")
            if items.lower() == "idly":
                quantity= input("enter no of " +str(items) + ":")
                if int(quantity)>=100:
                    cost = (int(quantity)*self.itemcost())-(discount * int(quantity) * self.itemcost())
                    print("cost of idly with discount is :" + str(cost))
                else:
                    cost=int(quantity)*self.itemcost()
                    print("cost of idly is :" +str(cost))
            else:
                print("Item not available!")
            no_of_item = int(no_of_item) - 1
            if int(no_of_item)<=0:
                break
        else:
            print("Invalid Entry!!")


order1=orders()
order1.hotelnames()
order1.orderfood(2)








