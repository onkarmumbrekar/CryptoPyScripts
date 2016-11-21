n = int(input().strip())
s = input().strip()
k = int(input().strip())
encrypt =''
alphasmall ='abcdefghijklmnopqrstuvwxyz'
alphacap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for c in s:
        small = alphasmall.find(c)
        if small>=0:
            encrypt += alphasmall[(small+k)%26]
        elif alphacap.find(c)>=0:
            encrypt += alphacap[(alphacap.find(c)+k)%26]
        else:
            encrypt +=c

print(encrypt)