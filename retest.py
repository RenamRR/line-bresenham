import matplotlib.pyplot as plt
import time

def plot_points(x, y):
    plt.scatter(x, y, color='black')

def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    xincrement = dx / float(steps)
    yincrement = dy / float(steps)
    x = x1
    y = y1
    plot_points([round(x)], [round(y)])
    start_time = time.monotonic()
    for i in range(steps):
        x += xincrement
        y += yincrement
        plot_points([round(x)], [round(y)])
    end_time = time.monotonic()
    return end_time - start_time

def bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    x = x1
    y = y1
    plot_points([x], [y])
    start_time = time.monotonic()
    while x != x2 or y != y2:
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
        plot_points([x], [y])
    end_time = time.monotonic()
    return end_time - start_time

# coordenadas dos pontos inicial e final da reta
x1, y1 = 10, 20
x2, y2 = 80, 120

# desenha a reta usando o algoritmo DDA
dda_time = dda(x1, y1, x2, y2)
print(f"DDA: tempo de execução = {dda_time:.6f} segundos")

# desenha a reta usando o algoritmo de Bresenham
bresenham_time = bresenham(x1, y1, x2, y2)
print(f"Bresenham: tempo de execução = {bresenham_time:.6f} segundos")

plt.show()
