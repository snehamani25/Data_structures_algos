
def insertion_sort(a):
    key = 0
    i = 0
    # print(a)
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while (i >= 0 and a[i] > key):
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    print(a)

def main():

    str_arr = list(input("Enter an array of numbers that you wish to sort:").split(','))
    arr=[int(x) for x in str_arr]
    insertion_sort(arr)

if __name__=="__main__":
    main()