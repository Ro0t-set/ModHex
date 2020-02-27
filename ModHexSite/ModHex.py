
#!/usr/bin/python

import sys
import random
#ok ora lo impacchetto...

nome_file =  sys.argv[1]


with open("media"+nome_file, 'rb') as f:
    data = f.read()

data = list(data)
larghezza_fascia=7
for i in range(100):
    posizione = random.randint(0,len(data))
    for x in range(larghezza_fascia):
        if(posizione+x < len(data)):
            data[posizione+x] = random.randint(0,255)


data = bytearray(data)

#file modificato nella cartella mod_media
with open("media/mod_media"+nome_file, 'wb') as f:
    f.write(data)

print("tutto ok")
