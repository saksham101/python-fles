import re
inp = input("enter the file name")
fhand = open(inp)
numlist = list()
for line in fhand :
  num = re.findall('[0-9]+',line)
  numlist+=num
sum1=0
for num in numlist :
    num=int(num)
    sum1+=num
print(sum1)
