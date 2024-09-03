import time


def binarySearch(shop, price):
    l = 0
    r = len(shop) - 1
    while r - l > -1:
        mid = int((r + l) / 2)
        if shop[mid] == price:
            return True
        if shop[mid] < price:
            l = mid + 1
        else:
            r = mid - 1
    return False

_ = int(input())
shop = list(map(int, input().split()))
print(str(binarySearch(shop, int(input()))).lower())
