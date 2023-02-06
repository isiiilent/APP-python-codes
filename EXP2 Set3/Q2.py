def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print('Enter Number')
abc=input()
print(mydoubler(abc))