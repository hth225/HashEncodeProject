def Decryption():
    file = open("HashDictionary.txt", 'r')
    lines = file.readlines()
    value = input("Hash : ")

    for line in lines:
        item = line.split(" ")
        if any(value in s for s in item):
            print(item)