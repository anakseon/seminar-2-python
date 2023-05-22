N = int(input('введите количество монет'))
for i in range(N):
    x = int(input('Орел(1) или решка(0)? '))
    if x == 1:
        k+=1
    else:
        j+=1
print(f' орел [k]')
print(f' решка [j]')
