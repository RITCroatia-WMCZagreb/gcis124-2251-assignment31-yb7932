'''
@ASSESSME.USERID: yb7932
@ASSESSME.AUTHOR: author, list of authors
@ASSESSME.DESCRIPTION: Assignment 3.1
@ASSESSME.ANALYZE: YES
'''

import math 

def fact(b):
    if b > 0:
        return math.factorial(int(b))
    return 0


def root(c):
    if c > 0:
      return math.sqrt(float(c))
      return 0
    

    def trunk(z):
        
        return math.trunc(z)
    
    
def main():
   x1 = int(input)("Enter a numeric value:")
   print(x1, "factorial","=",fact(x1))


x2 = float(input)("Enter a numeric value:")
print("The square root of", x2,"=",root(x2))



x3 = float(input("Enter a numeric value:"))


print(x3,"truncated","=",trunk(x3))


if __name__ == "main":
    main()