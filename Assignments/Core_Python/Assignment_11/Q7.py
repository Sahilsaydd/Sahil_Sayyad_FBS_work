def intersection_of_lists(list1, list2):
    result = []
    for i in range(len(list1)):
        if list1[i] in list2:
            result.append(list1[i])
    return result

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print("Intersection:", intersection_of_lists(list1, list2))
