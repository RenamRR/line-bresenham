import matplotlib.pyplot as plt
import time

# Função para plotar os pontos
def plotPoints(x, y):
    plt.scatter(x, y, color="black")

# Implementação do algoritmo DDA
def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    xincrement = dx / float(steps)
    yincrement = dy / float(steps)
    x = x1
    y = y1
    plotPoints([round(x)], [round(y)])
    start_time = time.time()
    for i in range(steps):
        x += xincrement
        y += yincrement
        plotPoints([round(x)], [round(y)])
    print("DDA: %.2f segundos" % (time.time() - start_time))

# Implementação do algoritmo Bresenham
def bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    x = x1
    y = y1
    plotPoints([x], [y])
    start_time = time.time()
    while x != x2 or y != y2:
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
        plotPoints([x], [y])
    print("Bresenham: %.2f segundos" % (time.time() - start_time))

# Chamando as funções para desenhar as retas
dda(1, 1, 20, 15)
bresenham(1, 1, 20, 15)

plt.show()