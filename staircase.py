# staircase

def staircase(n):
   # _,_,_,_,#

   spaces = 0
   symblos = n
   for i in range(n):
    n -= 1
    print((' ' * n) + ('#' * (i+1)))
    
    

staircase(4)