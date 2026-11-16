lst = [1, 2, 3]

def list2():
    print(lst)
    lst.append(4)
    print(lst)
    return lst

print(list2())
