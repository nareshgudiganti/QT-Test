for i in range(2, 100):
    for j in range(2, int(i/2)+1):
        if i%j == 0:
            break
    else:
        print(i)