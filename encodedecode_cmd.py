import hashlib
import base64
import os
md = hashlib.md5()
sha = hashlib.sha256()
sha2 = hashlib.sha224()


print('''1 : MD5
2 : SHA 256
3 : SHA 224
4 : BASE 64
''')
value = input("SELECT ENCODE ALGORITHM : ")

#while value == "4":

if value == "1":
    plaintext = input("PLZ TYPE PLAIN TEXT( MD5 ) : ")
    md.update(plaintext.encode("utf-8"))
    print (md.hexdigest())

elif value == "2":
    plaintext2 = input("PLZ TYPE PLAIN TEXT( SHA 256 ) : ")
    sha.update(plaintext2.encode("utf-8"))
    print (sha.hexdigest())

elif value == "3":
    plaintext3 = input("PLZ TYPE PLAIN TEXT( SHA224 ) : ")
    sha2.update(plaintext3.encode("utf-8"))
    print (sha2.hexdigest())

elif value == "4":
    g = input("1 : ENCODE 2: DECODE \n")
    if g == "1":
        plaintext4 = input("PLZ TYPE PLAIN TEXT( BASE 64 ) :")
        bs = base64.b64encode(plaintext4.encode("utf-8"))
        print (bs)
    elif g == "2":
        plaintext5 = input("PLZ TYPE ENCODED TEXT( BASE 64 ) :")
        bsd = base64.b64decode(plaintext5.encode("utf-8"))
        print (bsd)

    else :
        print ("WRONG TYPE")

else :
    print("WRONG TYPE.")
os.system("pause")

