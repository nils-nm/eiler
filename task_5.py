a = 1
answer = 0
while True:
    for i in range(1, 21):
        if a % i == 0:
            if i == 20:
                answer = a
            continue
        else:
            a += 1
            break
    if answer != 0:
        break
print(answer)
