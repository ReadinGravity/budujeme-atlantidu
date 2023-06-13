from PIL import Image

img = Image.new('RGB', (250, 250), 'white')
pixels = img.load()

a = input('Give point A as x,y:').split(',')
b = input('Give point B as x,y:').split(',')
a = list(map(int, a))
b = list(map(int, b))

if (a[0] > b[0] and a[1] > b[1]) or (a[0] > b[0] and a[1] < b[1]):
    a, b = b, a

if b[0] - a[0] != 0:
    k = (b[1] - a[1]) / (b[0] - a[0])
    q = a[1] - k * a[0]
    temp = int(k * a[0] + q)
    for x in range(a[0], b[0] + 1):
        y = int(k * x + q)
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
                pixels[new_x, temp + i] = (255, 0, 0)
        temp = y
else:
    if a[1] > b[1]:
        a[1], b[1] = b[1], a[1]
    for y in range(a[1], b[1] + 1):
        pixels[a[0], y] = (255, 0, 0)

img.show()
