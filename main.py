import numpy as np

def f(x): return x**2

def integral(f, a = 0, b = 1, n = 50_000):
    dx = (b - a) / n 
    x_esquerda = a + np.arange(n) * dx
    x_direita = a + (np.arange(n) + 1) * dx
    x_media = (x_esquerda + x_direita) / 2
    return np.sum(f(x_media)) * dx

print (integral(f,0,1))