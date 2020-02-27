
#!/usr/bin/python

import sys
import random
#ok ora lo impacchetto...

nome_file =  sys.argv[1]


with open(nome_file, 'rb') as f:
    data = f.read()

data = list(data)
print("lettura ex ok")

larghezza_fascia=7000

for i in range(10):
    posizione = random.randint(0,len(data))
    for x in range(larghezza_fascia):
        if(posizione+x < len(data)):
            data[posizione+x] = random.randint(0,255)

print("mod ok")
data = bytearray(data)

print("conversione ok")
with open("mod_"+nome_file, 'wb') as f:
    f.write(data)

print("fine")