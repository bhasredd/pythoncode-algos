def gcd(a,b):
    if a < b:
        a,b = b,a
    if b==0:
        return a
    else:
        return gcd(b, a%b)

if __name__ == '__main__':
    import time
    t0 = time.time()
    print gcd(6768764543787*2,6768764543787)
    t1 = time.time()
    print t1-t0
