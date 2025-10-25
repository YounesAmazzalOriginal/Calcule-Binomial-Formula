# Binomial Formula

n = int(input("n = "))
k = int(input("k = "))

while k > n :
    print("k > n Erreur")
    n = int(input("n = "))
    k = int(input("k = "))


v = n-k
i,j,p = 0,0,0
f_n,f_k,f_v = 1,1,1

while i < n :
    i += 1
    f_n = f_n * i
    print(i)

while j < k :
    j += 1
    f_k = f_k * j
    print(j)

while p < v :
    p += 1
    f_v = f_v * p
    print(p)


formule = f_n/(f_k * f_v)
print(f" = {formule}")
