

def float_difference(massive):
    minimal = massive[0]
    maximal = massive[0]
    for i in range(len(massive)):
        if massive[i] % 1 != 0:
            if massive[i] % 1 < minimal % 1:
                minimal = massive[i]
            if massive[i] % 1 > maximal % 1:
                maximal = massive[i]
    print(maximal)
    print(minimal)
    return maximal%1 - minimal%1


array = [1.1, 1.2, 3.1, 5, 10.01]
print(float_difference(array))
