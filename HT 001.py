
def odd_sum(massive):
    result = 0
    for i in range(1, len(massive), 2):

        result += massive[i]

    return result


array = [2, 3, 5, 9, 3]

print(odd_sum(array))


# АЛЬТЕРНАТИВНЫЙ (сельский) ВАРИАНТ

# def odd_sum (massive):
#     result = 0
#     count = 0
#     for i in massive:
#         count += 1
#         if count ==2:
#             result += i
#             count = 0

#     return result


# array = [2, 3, 5, 9, 3]

# print (odd_sum (array))
