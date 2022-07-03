
divisor = int(input())
boundary = int(input())

num = 0
for n in range(0, boundary+1):

    if n % divisor == 0:
        if n <= boundary:
            if n > 0:
                num = n
        #print('hi')
    else:
        pass
print(num)



