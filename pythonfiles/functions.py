import sys, math

def oddEve(a):
    if(a%2==0):
        return True
    else:
        return False
    
pn = int(sys.argv[1]) #taking command line input
print(oddEve(pn))