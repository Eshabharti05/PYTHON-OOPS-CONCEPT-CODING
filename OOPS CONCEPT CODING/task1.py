class Employee:
    cname="abc"
    cloc="Banglore"
    empcount=0
    def __init__(self,en,ea,er,esal):
        self.ename=en
        self.eage=ea
        self.erole=er
        self.esal=esal
        Employee.empcount+=1
    def __del__(self):
        Employee.empcount-=1
        print("emp is deleted")
esha=Employee("esha",34,"developer",45000000)
print(Employee.empcount)
