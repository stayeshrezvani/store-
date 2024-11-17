import time ,datetime
mylist=[]
for i in range (1,4):
    newlist=input("enter name of product for list:")
    mylist.append(newlist)
class Store:
    def __init__(self,myproduct):
        self.myproduct=myproduct
    def  buy(self):
        buy=input("what do you buy?")
        self.myproduct.append(buy)
        self.myproduct.append(mylist)
        print(self.myproduct)
    def sell(self):
        print(self.myproduct)
        sell=input("what do you want to sell from this list?") 
        if sell in self.myproduct:
            self.myproduct.remove(sell)
            print("ok")
            print(self.myproduct)
        else:
            print(" Sorry!we do not have this product!!")
    def change(self):
        newpro=input("what is you new product?")
        changer=input("do you want to exchange the new product with which old product?")
        if changer in self.myproduct:
            self.myproduct.append(newpro)
            self.myproduct.remove(changer)
            
        else:
            print(" Sorry!we do not have this product!!")
    def show(self):
        print("your new list of product:%s"%self.myproduct)
    def time(self):
        print("time is :%s"%time.asctime())
    def date(elf):
        print("date is :%s"%datetime.datetime.today())
              
seller=Store(mylist)
while(True):
    Q=int(input("   enter (0) for exit\nenter numer (1-6):"))
    if Q==0:
        print("closed!")
        break
    if Q==1:
        seller.buy()
    if Q==2:
        seller.sell()
    if Q==3:
        seller.change()
    if Q==4:
        seller.show()
    if Q==5:
        seller.time()
    if Q==6:
        seller.date()





