import random
import array
a=['@','#','$','%','=',':','?','.','/','|','~','>','*','(',')','<']
b=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
c=['A','B','C','D','E','F','G','H','I','J','K','l','M','N','O','P','Q','R','S','T','U','V','W','x','Y','Z']
d=['0','1','2','3','4','5','6','7','8','9']
len1=int(input("Enter password length :"));
z=a+b+c+d
rd=random.choice(d)
ru=random.choice(c)
rl=random.choice(b)
rs=random.choice(a)
rp=rd+ru+rl+rs
for i in range(len1-4):
    rp+=random.choice(z)
tpass=array.array('u',rp)
random.shuffle(tpass)
password=""
for c in tpass:
    password+=c
print("Generated Password:",password)