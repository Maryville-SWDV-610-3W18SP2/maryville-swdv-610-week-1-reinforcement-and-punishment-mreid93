def isMultiple(n, m):
    if n % m == 0:
        return True
    else:
        return False
    
def main():
    print('This tests if n is a multiple of m')
    n = input('Enter your n value as an integer : ')
    m = input('Enter your m value as an integer : ')
    if isMultiple(n,m) == True:
        print('n is a multiple of m!')
    else:
        print('n is NOT a multiple of m.')
