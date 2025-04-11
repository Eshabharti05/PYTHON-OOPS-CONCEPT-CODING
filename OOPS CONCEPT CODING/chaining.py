    class bank_v1():
    bank_name='SBI'
    bank_roi=7
    bank_branch="Mysore"
    def __init__(self,cn,ca,cac,cb):
        self.cname=cn
        self.cage=ca
        self.account=cac
        self.cbalance=cb
    def customer_details(self):
        print(f'customer name is {self.cname}')
        print(f'customer age is {self.cage}')
        print(f'customer account number is {self.account}')
        print(f'customer balance is {self.cbalance}')
        
    @classmethod
    def bank_details(cls):
        print(f'bank name is {cls.bank_name}')
        print(f'bank rate of interest is {cls.bank_roi}')
        print(f'bank branch is {cls.bank_branch}')

    @staticmethod
    def get_int_value():
        it=int(input("enter the amount"))
        return it

    def withdraw(self):
        amount=self.get_int_value()
        if amount<=self.cbalance:
            self.cbalance-=amount
            print(f'withdraw is successful and current balance is {self.cbalance}')
        else:
            print("insufficient amount")
            
    def deposite(self):
        amount=self.get_int_value()
        if amount>0:
            self.cbalance+=amount
            print("deposite successful")
        else:
            print("Enter sufficient amount")

#esha=bank_v1("esha",23,982973,10000)
#esha.customer_details()
#esha.withdraw()
#esha.deposite()


class bank_v2(bank_v1):
    bank_branch="Banglore"
    bank_mobile=8833445577

    def __init__(self,cn,ca,cac,cb,pin,ad):
        super().__init__(cn,ca,cac,cb)
        self.cpin=pin
        self.cadhar=ad

    def customer_details(self):
        super().customer_details()
        print(f'customer adhaar number is {self.cadhar}')

    @classmethod
    def bank_details(cls):
        super().bank_details()
        print(f'bank mobile number is {cls.bank_mobile}')
    
    def change_pin(self):
        pin=input("enter your pin")
        if self.cpin==pin:
            newpin=input("enter new pin")
            repin=input("Re-enter new pin")
            if newpin==repin:
                self.cpin=newpin
                print("Your pin has changed successfully")
            else:
                print("You have entered different pins")
        else:
            print("Incorrect Pin")


    def withdraw(self):
        pin=input("enter your pin")
        if self.cpin==pin:
            #super().withdraw()
            bank_v1.withdraw(self)
        else:
            print("Enter correct pin")

    @classmethod
    def change_roi(cls):
        roi=int(input("enter rate of interest"))
        cls.bank_roi=roi
        print("Your bank rate of interest is changed ")


    
esha=bank_v2("eshhhu",22,34450,55987000,"eshu@123",83993507)

esha.bank_details()
esha.customer_details()
esha.change_pin()
esha.withdraw()
esha.deposite()
esha.change_roi()
            

        
        
        

    
    
    
        
        
        
    
        
        
    
    
        

        
        
        
