from sys import stdin, stdout


def readInput(n):

    new = ''
    sa = []
    while n > 0:
        new = stdin.readline()
        new = new[:-1] + '$'
        for i in range(len(new)):
            print(new[-i:])
            sa += [new[-i:]]
        n-=1
        print("unsorted", sa)
    return sorted(range(len(sa)), key=lambda k: sa[k])

print(readInput(3))
