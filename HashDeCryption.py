def Decryption():
    file = open("HashDictionary.txt", 'r')
    lines = file.readlines()
    value = input("Hash : ")

    for line in lines:
        item = line.split("\t")
        if any(value in s for s in item):
            if (not item):
                print("Hash is not in Dictionary\nRecommand to use web Hash Decrypter.")
            else:
                print(item)

Decryption()