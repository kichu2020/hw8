import math
def factorial (n):
  fact=1
  for i in range (1,n+1):
    fact=fact*i
  return fact


def isprime(n):
  prime = False
  sqrt1=int(math.sqrt(n))+1
  for i in range (2,sqrt1):
    if n % i ==0:
      return False
  else:
      return True

def isleap(year):
  leap=False
  if year%4 ==0:
    
    if year%100==0 and year%400==0:
      return True
    else:
      return False
  else:
    return False

def cel2far(degrees):
  return((degrees*9/5)+32)

def far2cel(degrees):
  return((degrees-32)*5/9)

def km2miles(dist):
  return(dist/1.609)

def miles2km(dist):
  return (dist*1.609)

def medmodrng (list1):

  list1sort=sorted(list1)
  len1=len(list1sort)
  listrang=list1sort[-1]-list1sort[0]
  lenmed=int(len1/2)
  listmed=list1sort[lenmed]
  return(listrang,listmed)

