#no of vowels in a given string
'''
s="mock is important"
c=0
for i in s:
    if i in 'aeiouAEIOU':
        c+=1
print(c)
'''
#remove the vowels in a given string
'''
s="mock is important"
stir=""
for i in s:
    if i in "AEIOUaeiou":
        stir+=i
print(stir)
'''   
#longest common  prefix
'''
def longestcommonPrefix(arr):
    arr.sort()
    first=arr[0]
    last=arr[-1]
    minLength=min(len(first),len(last))
    i=0
    while i<minLength and first[i]==last[i]:
        i+=1
    return first[:i]
arr=["geeksforgeeks","geeks","geek","geezer"]
print(longestcommonPrefix(arr))
'''
# Python program to check Adam Number 
# To reverse Digits of numbers
'''
def reverseDigits(num) : 
	rev = 0
	while (num > 0) : 
		rev = rev * 10 + num % 10
		num //= 10
		
	return rev 

# To square number 
def square(num) : 
	return (num * num) 
	
# To check Adam Number 
def checkAdamNumber(num) : 
	
	# Square first number and square 
	# reverse digits of second number 
	a = square(num) 
	b = square(reverseDigits(num)) 
		
	# If reverse of b equals a then given 
	# number is Adam number 
	if (a == reverseDigits(b)) : 
		return True
	else : 
		return False

# Driver program to test above functions 
num = 14
if (checkAdamNumber(num)) : 
	print ("Adam Number") 
else : 
	print ("Not a Adam Number") 

'''
'''
s="esha is beautiful"
rev=""
for i in s.split():
    rev=i+' '+rev
print(rev)

'''
#half in uppercase
s="esha is not stupid but beautiful"
res=""
a=len(s)//2
for i in range(len(s)):
    if i>a:
        res+=s[i].upper()
    else:
        res+=s[i].lower()
print(res)

#

















































































































    
    



