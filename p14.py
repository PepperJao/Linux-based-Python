import string
import random
cats=open('svg.html','r')
str0 = cats.read()
print ("读取的字符串是 : ", str0)

#for line in cats:
#   print("读取的字符串是 : ",line)
#l=list(str0)

#n=str0.index('#0')
#print(n)
for i in range(10):
    r1=(random.randint(100,1000))
    r2=(random.randint(0,10))
# print(r)
    str1=str0.replace('#008B8B','#%sB%dB'%(r1,r2))
    print(str1)
    cats2=open('svg_out%s.html'%i,'w')
    cats2.write(str1)
cats.close()
