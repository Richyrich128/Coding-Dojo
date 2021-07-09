def countdown(input):
    count = []
    for i in range(input, 0, -1):
        count.append(i)
    return count
print(countdown(10))

print()
def print_and_return(a, b):
    print(a)
    return b
print(print_and_return(5, 8))

print()
def first_plus_length(arr):
    return(arr[0] + arr[len(arr)-1])

print(first_plus_length([1,2,3,4]))
print()

def values_greater_than_second(li):
    if len(li) >= 2:
        other_list = []
        num = li[1]
        count = 0
        for i in li:
            if num < i:
                count += 1
                other_list.append(i)
        print(count)
        return other_list
    return False

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

def length_and_value(c, d):
    arr = []
    for _ in range(c):
        arr.append(d)
    return arr

print(length_and_value(6,2))