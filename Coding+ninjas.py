#!/usr/bin/env python
# coding: utf-8

# In[7]:


n=int(input("plz enter the range to check prime no.:"))
flag=False
for d in range(2,n,1):
    if n%d==0:
        flag=True
if flag:
    print("not prime")
    
else:
    print("prime")


# In[11]:


n=int(input("plz enter the range to check prime no.:"))
flag=False
for d in range(1,n+1):
    if d>1:
        for i in range(2,d):
            if d%i==0:
                break
               # print(d)
        else:
             print(d)


# In[1]:


def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

# decimal number
dec = int(input())

convertToBinary(dec)
print()


# In[11]:


n=int(input("enter;"))
while n>0:
    n=n//2
    print(n%2,end='')


# In[9]:


n = int(input())

dec = 0
i = 1
while n!=0:
    rem = n%10
    dec = dec + (rem*i)
    i = i*2
    n = int(n/10)

print(dec)


# In[15]:


n=12
while n>0:
    rem=n%2
    print(rem)
    n=n//2


# In[ ]:


= int(input())

binary = 0
power = 1

while n >0:
   lastbit = n%2
   binary += (lastbit*power)
   power *=10
   n = n//2
print(binary)


# In[49]:


n = int(input())
a = 0
b = 1
sum = 0
i = 1
if n==1:
    print(b)
#esle:
else:
    while i <= n:
        print(sum)
        a=b
        b=a+sum
        sum=a+b
        i+=1


# In[20]:


def evenFib(n) :
	if (n < 1) :
		return n
	if (n == 1) :
		return 2

	return ((4 * evenFib(n-1)) + evenFib(n-2))



n = int(input())
print(evenFib(n))


# In[24]:


n=int(input())
if n<1:
    print(n)
elif n==1:
    print(2)
else:
    b=n-1
    c=n-2
    print(4*b+c)


# In[34]:


nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   
   while count < nterms:
       
            print(n1)
            nth = n1 + n2
       # update values
            n1 = n2
            n2 = nth
            count += 1


# In[36]:


n=int(input("enter;"))
a=0
b=1
i=0
sum=0
if n<1:
    print("invalid input")
elif n==1:
    print("none")
else:
    while i<n:
        print(a)
        nth=a+b
        a=b
        b=nth
        i+=1
        


# In[43]:


Number = int(input("Please Enter the Fibonacci Number Range = "))

First = 0
Second = 1
Sum = 0

for Num in range(0, Number):
    print(First, end = '  ')
    Sum = Sum + First
    Next = First + Second
    First = Second
    Second = Next

print( Sum)


# In[60]:


n=int(input("enter;"))
a=0
b=1
i=0
sum=0
if n<1:
    print("invalid input")
elif n==1:
    print("none")
else:
    while i<n:
        print(a)
        #sum=sum+a
       # print(sum)
        nth=a+b
        a=b
        b=nth
        
        i+=1
   


# In[ ]:




