cases = int(input("Enter the number of cases:\t"))
for i in range(cases):
    l = input("Enter input:\t")
    n = l
    while(n != n[::-1]):
        n = int(n)+1
        n = str(n)
    print(f"The plendrom of {l} is {n}")
