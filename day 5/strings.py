#string methods are alpha,is digit,is alam,is upper,is lower,converting in lower case,converting in upper case,swap case
#inp="hello world"
#print(inp.upper())
#print(inp.lower())
#print(inp.capitalize())
#print(inp.title())
#print(inp.swapcase())
#print(inp.strip())
#print(inp.replace('l','z'))
#print(inp.split())
#print(inp.split('o'))

#inp='123'
#print(inp.isalpha)
#print(inp.isalnum())
#print(inp.isascii())
#print(inp.islower())
#print(inp.isupper)
#print(inp.istitle)
#print(inp.isnumeric())
#print(inp.isdigit())
 
#print(ord('a'))
#print(ord('a')+3)

#print(ord('<'))
#print(chr(60))

#check how many vowels are there in string
#check=['a','e','i','o','u']
#count=0
#inp="hello world"
#for i in inp:
#    if(i in check):
#        count+=1
#print(count) 

#write a program to print all the consonants
#check=['a','e','i','o','u']
#abc="bcdfghjklmnpqrstvwxyz"
#count=0
#c=0
#i="vaishnavi"
#inp=i.lower()
#for i in inp:
#    if (i in abc):
#        count+=1
#print(count)                

#print all the vowels followed by consonants
#check=['a','e','i','o','u']
#abc="bcdfghjklmnpqrstvwxyz"
#ans=""
#i="vaishnavi"
#inp=i.lower()
#for i in inp:
#    if(i in check):
#        ans+=i
#for i in inp:
#    if(i in abc):
#        ans+=i
#print(ans)

#print the non repeating characters in a string or print the unique characters in string
#check=['a','e','i','o','u']
#abc="bcdfghjklmnpqrstvwxyz"
#ans=""
#i="vaishnavi"
#inp=i.lower()
#for i in inp:
#    if(i not in ans):
#        ans+=i
#print(ans)

#check="0123456789"
#abc="bcdfghjklmnpqrstvwxyz"
#vow="aeiou"
#sum=0
#i="vaishnavi123"
#inp=i.lower()
#for i in inp:
#    if (i in check):
#        sum+=int(i)
#print(sum)

#check="0123456789"
#abc="bcdfghjklmnpqrstvwxyz"
#vow="aeiou"
#rev=0
#i="vaishnavi123"
#inp=i.lower()
#for i in inp:
#    if(i in check):
#        rev%


#for i in range(32,128):
#    print(chr(i),end=" ") 

          
#inp=input()
#sum=0
#for i in inp:
#    if(ord(i)>=48 and ord(i)<=57):
#        sum+=int(i)
#print(sum)

#write a code to print all the capital letters in a string
#inp=input()
#sum=0
#for i in inp:
#    if(ord(i)>=65 and ord(i)<=90):
#      print(i)

#remove all the bracklets from the given algebraic expression
#inp=input()
#for i in inp:
#   if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
#       pass
#   else:
#       print(i,end=" ")
#print()

#o/p: ABC 4
#     EFG
#inp=input()
#for i in inp:
#    print(chr(ord(i)+4,end=" "))
#    count+=i
# print(count) 

#hello-----wor----ld
#---------helloworld
#inp=input()
#count=0
#ans=""
#for i in inp:
#    if(i=="-"):
#        count+=1
#    else:
#        ans=ans+i    
#print("-"*count+ans)

#patterns
#for i in range(3):
#    for j in range(3):
#        print("*",end=" ")
#    print() 

for i in range(10):
    for j in range(10):
        if(i==j):
           print(" ",end=" ")
        else:
           print("*",end=" ")
    print()         
