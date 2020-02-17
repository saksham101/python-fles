stri=(input("enter string "))
l=len(stri)
for i in range(0,l):
 c=stri[i]
 print("The ASCII value of '" + c + "' is", ord(c))

str1=stri
all_f = {} 
for i in str1: 
  if i in all_f: 
        all_f[i] += 1
  else: 
        all_f[i] = 1
print ("Count of all characters in given string is : ",str(all_f))         
