# menentukan bilangan genap
genap = lambda x: x%2 == 0
list(filter(genap, range(11)))
print(list(filter(genap, range(11))))