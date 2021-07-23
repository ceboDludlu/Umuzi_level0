#task6.0
def maximum( a, b, c):

    a = int(input("input first digit: "))
    b = int(input("input second digit: "))
    c = int(input("input third digit: "))

    if (a >= b) and (a >= c):
        return a
  
    elif (b >= a) and (b >= c):
        return b
    else:
        return c
          
    #print(maximum(a, b,c))
     
    