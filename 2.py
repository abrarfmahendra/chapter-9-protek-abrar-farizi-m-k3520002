print('\n', 'Piramida Bintang', '\n')


def bintang(n):
    a = 0
    b = -1
    for i in range(n):
        print(('*' * (1+2*i)).center(1+2*5))


bintang(4)

print('\n')
