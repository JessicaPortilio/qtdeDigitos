def contarDigitos(n):
    if n < 10:
        return 1
    cont = 0
    while n > 0:
        cont += 1
        n //= 10
    return cont


numero = int(input())
print(contarDigitos(numero))