

def unique(st):
    arr = []
    counter = 0
    for j, i in enumerate(st):
        if j == 0:
            arr.append(i)
        elif i != arr[counter]:
            arr.append(i)
            counter += 1

    return arr
