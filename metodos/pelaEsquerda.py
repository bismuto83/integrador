def f(x):
    return x**2

particao = [i/100 for i in range(100)]
resultado = 0
for x_i in particao:
    resultado += f(x_i) * 1/100

print(resultado)
