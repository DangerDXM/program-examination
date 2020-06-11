import sys


def int_to_bin(num):
    s = ''
    while num:
        s += str(num % 2)
        num = num // 2
    if num:
        s += num % 2
    return s[::-1]


def querry_1(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1] and s[i] == '1':
            return True
    return False


if __name__ == '__main__':
    print('please enter a number:')
    n = int(sys.stdin.readline().strip())
    if n < 0:
        raise ValueError('输入必须大于0...')
    elif n <= 2:
        print(0)
    else:
        total = 0
        for i in range(3, n+1):
            s = int_to_bin(i)

            if querry_1(s):
                total += 1
                print('i = %-2d, s = %-4s, total = %d' % (i, s, total))
                print('i = {}\t, s = {}\t, total = {}\t'.format(i, s, total))
        print('total successive 1:', total)
