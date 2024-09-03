class Book:
    def __intit__(self, isbn, name, year):
        self.isbn = isbn
        self.name = name
        self.year = year


def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    left_arr = []
    right_arr = []
    for i in range(n1):
        left_arr.append(arr[left + i])
    for j in range(n2):
        right_arr.append(arr[mid + 1 + j])
    i = j = 0
    k = left
    while i < n1 and j < n2:
        if ((left_arr[i].year < right_arr[j].year) or
                (left_arr[i].year == right_arr[j].year and left_arr[i].name <= right_arr[j].name)):
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = left_arr[i]
        k += 1
        i += 1
    while j < n2:
        arr[k] = right_arr[j]
        k += 1
        j += 1


def MergeSort(arr, left, right):
    if left >= right:
        return

    mid = int(left + (right - left) / 2)

    MergeSort(arr, left, mid)
    MergeSort(arr, mid + 1, right)

    merge(arr, left, mid, right)


n = int(input())
library = []
for i in range(n):
    isbn, name, year = input().split('"')
    isbn = isbn[:10]
    name = '"' + name + '"'
    year = int(year[1:])
    book = Book()
    book.year = year
    book.isbn = isbn
    book.name = name
    library.append(book)

MergeSort(library, 0, n - 1)

for book in library:
    print(' '.join([book.isbn, book.name, str(book.year)]))


