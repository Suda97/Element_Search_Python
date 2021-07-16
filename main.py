import random


def genlist():
    g = []
    i = 0
    while i < random.randint(10, 50):
        g.append(random.randint(0, 100))
        i += 1
    return g


def binary_search(lis, left, right, u):
    if right >= left:
        mid = (right + left) // 2

        if lis[mid] == u:
            return True
        elif lis[mid] > u:
            return binary_search(lis, left, mid - 1, u)
        else:
            return binary_search(lis, mid + 1, right, u)

    else:
        return False


if __name__ == '__main__':
    li = sorted(set(genlist()))
    print(li)
    usin = int(input("Give me number: "))
    print(binary_search(li, 0, len(li) - 1, usin))
