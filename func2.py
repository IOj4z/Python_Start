def odds(arr):
    return arr.index('odd') in arr


def find_sum(n):
    res = 0
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res


print(find_sum(5))