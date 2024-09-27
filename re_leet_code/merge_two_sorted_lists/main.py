def mergeTwoLists(list1, list2):
    list3 = list1 + list2
    return sorted(list3)


list1 = [1, 2, 4]
list2 = [1, 3, 4]

print(mergeTwoLists(list1, list2))
