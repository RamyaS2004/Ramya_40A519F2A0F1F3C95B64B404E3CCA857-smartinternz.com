def fact_rec(n):
  if n==0:
    return 1
  else:
    return n*fact_rec(n-1)
num=int(input('Enter a number'))
res=fact_rec(num)
print("The factorial of {}is{}".format(num,res))