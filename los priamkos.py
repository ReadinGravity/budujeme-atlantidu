from PIL import Image

img = Image.new('RGB', (550, 550), 'white')
pixels = img.load()

a = input('Daj suradnice bodu A ako Ax,Ay:').split(',')
b = input('Daj suradnice bodum B ako Bx,By:').split(',')
a = list(map(int,a))
b = list(map(int,b))

#a[0] <= b[0]
if a[0] > b[0]:
    a, b = b, a

if a[0] == b[0]:  #ci ten had neni vertikalny
    if a[1] > b[1]:
        a[1], b[1] = b[1], a[1]
    for y in range(a[1], b[1] + 1):
        if 0 <= a[0] < 550 and 0 <= y < 550:
            pixels[a[0], y] = (255, 0, 0)
else:
    k = (b[1] - a[1]) / (b[0] - a[0])
    q = a[1] - k * a[0]
    temp = int(k * a[0] + q)
    for x in range(a[0], b[0] + 1):
        y = int(k * x + q)
        if 0 <= x < 550 and 0 <= y < 550:
            pixels[x, y] = (255, 0, 0)
        print(x, y)

        vector = (b[0] - a[0], b[1] - a[1])
        vector = (vector[1], vector[0] * (-1))
        if vector[0] < 0 and vector[1] < 0:
            vector = (vector[0] * (-1), vector[1] * (-1))
        c = float((-1) * (vector[0] * a[0] + vector[1] * a[1]))
        if abs(y - temp) > 1:
            for i in range(1, abs(y - temp)):
                if y < temp:
                    i = -i
                new_x = round((vector[1] * (temp + i) * (-1) + c * (-1)) / vector[0])
                print(new_x, temp + i)
                if 0 <= new_x < 550 and 0 <= temp + i < 550:
                    pixels[new_x, temp + i] = (255, 0, 0)
        temp = y

img.show()
