def qsort(array, left, right):
    middle = (left + right) // 2
    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)
    return array

element = int(input('ввести любое целое число_'))
array = list(map(int, input('ввести список чисел через пробел_').split()))
print(qsort(array,0,len(array) - 1))

if element<=array[0] or element>=array[len(array) - 1]:
    print ('невозможно соблюдать условия поиска индекса')
else:
    def binary_search(array, element, left, right):
        middle = (right + left) // 2
        if left > right:
            return 'числа нет в списке, индекс ближайшего меньшего', middle
        if array[middle] == element:
            return 'индекс ближайшего меньшего', middle - 1
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    print(binary_search(array, element, 0, len(array) - 1))

