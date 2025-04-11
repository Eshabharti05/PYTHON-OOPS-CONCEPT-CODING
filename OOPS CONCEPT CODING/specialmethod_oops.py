'''
comp name='abc'
com loc='banglore'
empcount=0
ename,eage,erole,esalary==sp
'''
class Employee():
    cn='abc'
    cloc='Banglore'
    empcount=0

    def __init__(self,en,ea,er,esal):
        self.ename=en
        self.eage=ea
        self.erole=er
        self.esalary=esal
        Employee.empcount+=1

    def __del__(self):
        Employee.empcount-=1
        print("emp is deleted")

esha=Employee('esha',22,'developer',50000000)
print(Employee.empcount)
        
    


















































































































































