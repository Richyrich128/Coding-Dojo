for i in range(151):
    print(i)
print()
for j in range(5,1001,5):
    print(j)
print()
for k in range(1, 101):
    five = k % 5 == 0
    ten = k % 10 == 0
    if(five or ten):
        if (five):
            print("Coding")
        if (ten):
            print("Coding Dojo")
    else:
        print(k)

print()
sum = 0
for y in range(1, 500001, 2):
    sum += y
print(sum)

print()
for f in range(2018, 0, -4):
    print(f)

print()
lowNum = 2
highNum = 9
mult = 3
for a in range(lowNum, highNum + 1):
    if (a % mult == 0):
        print(a)