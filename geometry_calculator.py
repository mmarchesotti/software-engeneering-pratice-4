import math

def area_circle(radius):
    if radius < 0:
        raise ValueError("O raio não pode ser negativo.")
    return math.pi * radius ** 2

def area_rectangle(length, width):
    if length < 0 or width < 0:
        raise ValueError("O comprimento e a largura não podem ser negativos.")
    return length * width

def area_triangle(base, height):
    if base < 0 or height < 0:
        raise ValueError("A base e a altura não podem ser negativas.")
    return 0.5 * base * height
