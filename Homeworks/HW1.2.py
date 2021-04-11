n = int(input("Bir sayı giriniz: "))
a = range(0,(n+1)) #so that including n
for i in a:
    if i % 2 == 0:
        print(i, end=" ")

