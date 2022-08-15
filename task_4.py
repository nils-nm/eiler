first = 999
second = 999
answer = 0
while True:
    x = first * second

    y = str(x)
    if y == y[::-1]:
        print(x, y, y[::-1])
        if x > answer:
            answer = x
    if first == 100 and second == 100:
        break
    if second == 100:
        second = 999
        first -= 1
    else:
        second -= 1
print(answer)
