def gen_prime(x=2):
    '''素数'''
    while True:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            yield x
        x += 1
