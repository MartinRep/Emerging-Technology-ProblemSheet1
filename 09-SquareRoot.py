def SquareRoot(x):
    z = 1
    for i in range(0,10):
        z = z - ((z*z - x) / (2 * z))
        print(z)
    
SquareRoot(25)