'''
class address:
    def __init__(self,c,s,co):
        self.city=c
        self.state=s
        self.country=co
    def display_address(self):
        print(f'city name is {self.city}')
        print(f'state is {self.state}')
        print(f'country is {self.country}')
Banglore=address("ranchi","Jharkhand","India")

class Student:
    def __init__(self,n,i,cl,ad):
        self.sname=n
        self.sid=i
        self.sclass=cl
        self.saddr=ad
    def student_info(self):
        print(f'student name is {self.sname}')
        print(f'student id is {self.sid}')
        print(f'student class is {self.sclass}')
        print('student address is: ')
        self.saddr.display_address()
        

esha=Student("eshuu",12,5,Banglore)
esha.student_info()
'''


'''
class Player:
    def __init__(self,pn,pa,pco,pm,pw,pr):
        self.pname=pn
        self.page=pa
        self.pcountry=pco
        self.pmatches=pm
        self.pwickets=pw
        self.pruns=pr

class Team:
    def  __init__(self,nop):
        self.nop=nop
        self.pl=[]
        for i in range(self.nop):
            pn=input("enter player name")
            pa=int(input("enter player age"))
            pco=input("enter player country")
            pm=int(input("enter player matches played"))
            pw=int(input("enter player wickets"))
            pr=int(input("enter player runs"))
            PlayerObj=Player(pn,pa,pco,pm,pw,pr)
            self.pl.append(PlayerObj)
            
    def max_runs(self):
        mruns=self.pl[0]
        for i in self.pl:
            if i.pruns>mruns.pruns:
                mruns=i
        return mruns.pname

    def max_wickets(self):
        mw=self.pl[0]
        for i in self.pl:
            if i.pwickets>mw.pwickets:
                mw=i
        return mw.pname
esha=Team(2)
print(esha.max_runs(),"has highest runs")
print(esha.max_wickets(),"has max wickets")
'''


class address:
    def __init__(self,c,s,co):
        self.city=c
        self.state=s
        self.country=co
    def display_address(self):
        print(f'city name is {self.city}')
        print(f'state is {self.state}')
        print(f'country is {self.country}')

class Student:
    def __init__(self,n,i,cl):
        self.sname=n
        self.sid=i
        self.sclass=cl
        c=input("enter city")
        s=input("enter state")
        co=input("enter country")
        ACO=address(c,s,co)
        self.adr=ACO

    def student_info(self):
        print(f'student name is {self.sname}')
        print(f'student id is {self.sid}')
        print(f'student class is {self.sclass}')
        print('student address is: ')
        self.adr.display_address()

esha=Student("esha",12,2)
esha.student_info()      
        








































