a = [34, 56, 22, 1, 10]
m = 0
cpy = 0
i = 0
for i in range(len(a)-1):
    m = i
    #print(i)
    for j in range(i+1, len(a)):
        print(a[m])
        if a[j] < a[m]:
            m = j

    a[i], a[m] = a[m], a[i]
print(a)
