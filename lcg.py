def linear_congruence_generator(seed=1,a=5,b=3,c=7):
    """ b and c should be relatively prime """
    while True:
        seed = (a*seed + b) % c
        yield seed

if __name__ == '__main__':
    lcg = linear_congruence_generator(4)
    for i in xrange(14):
        print lcg.next()

