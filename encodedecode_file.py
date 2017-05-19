import hashlib
import base64
import os
md = hashlib.md5()
sha = hashlib.sha256()
sha2 = hashlib.sha224()


file = input("FILE ADDRESS : ")
f = open(file, 'w+')
re = f.read()

print('''1 : MD5
2 : SHA 256
3 : SHA 224
4 : BASE 64
''')
value = input("SELECT ENCODE ALGORITHM : ")

#while value == "4":

if value == "1":
    md.update(re.encode("utf-8"))
    f.write (md.hexdigest())
    f.close()
    

elif value == "2":
    sha.update(re.encode("utf-8"))
    f.write (sha.hexdigest())
    f.close()

elif value == "3":
    sha2.update(re.encode("utf-8"))
    f.write (sha2.hexdigest())
    f.close()

elif value == "4":
    g = input("1 : ENCODE 2: DECODE \n")
    if g == "1":
        bs = base64.b64encode(re.encode("utf-8"))
        f.write(bs)
        f.close()

    elif g == "2":
        bsd = base64.b64decode(re.encode("utf-8"))
        f.write (bsd)
        f.close()

    else :
        print("WRONG TYPE")

else :
    print("WRONG TYPE.")
os.system("pause")
