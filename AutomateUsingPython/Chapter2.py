#learn if then else controls
#use break to end a loop
#continue means iterate to the next loop
#range function learned already
#learn importing
#like import matlibplot.pyplot etc.
#import and from are the same
#finished chapter 2

def collatz(InputNumber):
    if InputNumber%2 == 0:
        print("InputNumber is even and output is: ",InputNumber//2)
    elif InputNumber%2 == 1:
        print("InputNumber is odd and output is: ",3*InputNumber+1)
            
collatz(4)        
            