

def count_pairs (massive):
    result = []
    for i in range(0, (len(massive)+1)//2):
        result.append(massive[i] * massive[len(massive)-1-i])
    return result
        

array = [2, 3, 4, 5, 6]

print(count_pairs(array))
