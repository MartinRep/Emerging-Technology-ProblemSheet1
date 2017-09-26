def SquareRoot(x):
    z = 1
    lastZ = None
    while z != lastZ:
        lastZ = z
        z = z - ((z*z - x) / (2 * z))
        print(z)
    
SquareRoot(25)