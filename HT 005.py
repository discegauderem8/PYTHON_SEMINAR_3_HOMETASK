from tkinter import N


def Negafibonacci (a):
    if a in {0, 1}: 
        return a
    else:
        return Negafibonacci (a+2) - Negafibonacci (a + 1)

def Fibonacci (b):
    if b in {0, 1}:
        return b
    else:
         return Fibonacci(b-1) + Fibonacci(b-2)


N = int(input("Введите число N: "))
result = []

for i in range (-N, 0):
    result.append(Negafibonacci (i))

for j in range (0, N+1):
    result.append(Fibonacci(j))

print(result)








































