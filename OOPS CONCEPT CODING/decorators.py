'''
def outer(arg):
    print("outer started")
    def inner():
        print("inner started")
        arg()
        print("inner ended")
    print("outer ended")
    return inner

@outer
def hello():
    print("hello started")
    print("hello ended")

@outer
def fun():
    print("hiiii everyone")
fun()






#time taken for fibbonacci series problem.
'''
'''
def decoratortime(arg):
    def inner():
        import time
        it=time.time()
        arg()
        ft=time.time()
        print("time taken for completing task",it-ft)
    return inner
@decoratortime
def fibbo():
    fv=int(input())
    sv=int(input())
    n=int(input())
    for i in range(n):
        print(fv)
        fv,sv=sv,fv+sv
fibbo()
'''













































































    






















    
    
