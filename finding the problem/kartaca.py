
import base64

dizim = []


def toString(binaryString):
    
    return "".join([chr(int(binaryString[i:i+8],2)) for i in range(0,len(binaryString),8)])

import os
your_path = '../karataca2/kartaca'
files = os.listdir(your_path)
print(files)
file = open("yazi.txt","w",encoding="utf-8")
#print("yapi : ",files," uzunluk : ",len(files))



def basee(codee):
	coded_string = codee
	deger = base64.b64decode(coded_string)
	message = deger.decode('ascii')
	return message

eslesme = {}

for i in files:
	ince = basee(i)
	eslesme[i]=int(ince)

sorted_items = dict(sorted(eslesme.items(), key=lambda item: item[1]))

print(sorted_items)

sirali = []

for i in sorted_items.keys():
	sirali.append(i)

for i in sirali:
	f = open(f"../karataca2/kartaca/{i}","r")
	print(f)
	yazi = f.read()
	dizim.append(yazi)
	lastt = yazi.replace(' ','')
	yaz = toString(lastt)
	#yaz = toString(lastt)
	metin = yaz
	file.write(metin)
	print(metin)


file.close()

for i in dizim:
	print(i)
