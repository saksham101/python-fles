def fib(num) :
  if num == 1 :
    return 0
  elif num == 1 :
    return 1
  elif num == 2 :
    return 1
  else :
    return fib(num-1) + fib(num-2)
num = input("enter the number of terms")
num = int(num)
j=1
while j<=num :
  series = fib(j)
  print(series)
  j+=1
