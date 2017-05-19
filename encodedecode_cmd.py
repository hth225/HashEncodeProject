import hashlib
import base64
import os
import HashDeCryption

md = hashlib.md5()
sha = hashlib.sha256()
sha2 = hashlib.sha224()
file = open("HashDictionary.txt", "a")

while(True):

    print("C to Continue\nPress any key to exit")
    con = input()
    try:
        if (con == 'c' or con == 'C'):
            print('''1 : MD5\n2 : SHA 256\n3 : SHA 224\n4 : BASE 64\n5 : Decryption''')
            value = input("SELECT ENCODE ALGORITHM : ")

            #while value == "4":

            if value == "1":
                plaintext = input("PLZ TYPE PLAIN TEXT( MD5 ) : ")
                md.update(plaintext.encode("utf-8"))
                print (md.hexdigest()+"\n")
                file.write(md.hexdigest()+ "\t"+plaintext +"\n")
                file.close()

            elif value == "2":
                plaintext2 = input("PLZ TYPE PLAIN TEXT( SHA 256 ) : ")
                sha.update(plaintext2.encode("utf-8"))
                print (sha.hexdigest()+"\n")
                file.write(sha.hexdigest()+ "\t"+plaintext2 +"\n")
                file.close()

            elif value == "3":
                plaintext3 = input("PLZ TYPE PLAIN TEXT( SHA224 ) : ")
                sha2.update(plaintext3.encode("utf-8"))
                print (sha2.hexdigest()+"\n")
                file.write(sha2.hexdigest()+ "\t"+plaintext3 +"\n")
                file.close()

            elif value == "4":
                g = input("1 : ENCODE 2: DECODE \n")
                if g == "1":
                    plaintext4 = input("PLZ TYPE PLAIN TEXT( BASE 64 ) :")
                    bs = base64.b64encode(plaintext4.encode("utf-8"))
                    print (bs+"\n")
                    file.write(bs + "\t"+ plaintext4 +"\n")
                    file.close()

                elif g == "2":
                    plaintext5 = input("PLZ TYPE ENCODED TEXT( BASE 64 ) :")
                    bsd = base64.b64decode(plaintext5.encode("utf-8"))
                    print (bsd+"\n")
                    file.write(bsd+ "\t"+plaintext5+"\n")
                    file.close()
                else :
                    print ("WRONG TYPE")

            elif value == "5":
                HashDeCryption.Decryption()

            else:
                print("WRONG TYPE")

        else :
            print("Exit")
            break

    except:
        print("Invalid command")
        os.system("pause")
        break

