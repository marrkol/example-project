# 1. suma_listy
def suma_listy(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + suma_listy(l[1:])

l = [1, 2, 6, 4, 6]
print(suma_listy(l))

#   czy l jest puste?
#       y -> zwróć 0
#       n -> zwróć l[0] + suma_listy(lista_bez_0_elementu)

# 2. znajdz_najwiekszy_element_listy
def najwiekszy_element(l):
    if len(l) == 1:
        return l[0]
    else:
        max = najwiekszy_element(l[1:])
        return l[0] if l[0] > max else max

l = [5, 2, 9, 1, 7, 15, 20]
print(najwiekszy_element(l))

#   czy l ma 1 element?
#       y -> zwróć l[0]
#       n ->
#           czy najwiekszy_element(l[1:]) większe od l[0]?
#           y -> zwróć najwiekszy_element(l[1:])
#           n -> zwróć l[0]

# 3. silnia
def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)
print(silnia(5))

#   czy n jest zerem?
#       y -> zwróć 1
#       n -> zwróć n * silnia(n-1)

# 4. ciag_fibonaciego
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(8))

#   czy n jest zerem?
#       y -> zwróć 0
#       n ->
#           czy n jest jedynką?
#           y -> zwróć 1
#           n -> zwróć fib(n-1) + fib(n-2)

