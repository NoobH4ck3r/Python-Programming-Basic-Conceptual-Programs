limit=int(input("Enter the limit:\t"))

choicess = int(input("Enter the choice\n1.List\n2.Dictionary\n3.Set"))
if choicess == 1:
    lists=[input("Enter the name of item:\t") for i in range(limit)]
    print(lists)
elif choicess == 2:
    Dict1 = {d:input(f"Enter the {d} item in the dictionary:\t") for d in range(limit)}
    print(Dict1)
elif choicess ==3:
    sets={input(f"Enter the name of item {i}:\t") for i in range(limit)}
    print(sets)
else:
    print("Invalid option")


