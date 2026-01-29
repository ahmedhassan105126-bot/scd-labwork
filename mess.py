# messy.py
def f(a,b,c):
 if c=='add':
  return a+b
 elif c=='sub':
  return a-b
 elif c=='mul':
  return a*b
 elif c=='div':
  return a/b
x=int(input())
y=int(input())
z=input()
print(f(x,y,z))