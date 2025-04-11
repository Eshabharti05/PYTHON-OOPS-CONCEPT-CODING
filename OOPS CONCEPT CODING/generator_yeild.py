def fibbo(fv,sv,n):
    i=1
    while i<=n:
        yield fv
        fv,sv=sv,fv+sv
        i+=1
fbo=fibbo(0,1,5)
for i in fbo:
    print(i)
        
