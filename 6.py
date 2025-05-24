L= ['a', 'b', 'c','d','e']
D = {'a': 11, 'b': 22, 'm': 33, 'd': 66}
key = input("Enter key: ")

if key in L and key in D:
    print("Value of key:", D[key])
else:
    print("Key not present.")