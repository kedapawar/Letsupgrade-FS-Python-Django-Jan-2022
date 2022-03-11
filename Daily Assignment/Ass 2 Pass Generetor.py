import random
sam1="kedar"
i1=random.sample(sam1,3)
sam2="PAWAR"
i2=random.sample(sam2,3)
sam3="14031984"
i3=random.sample(sam3,6)
sam4="!@#$&"
i4=random.sample(sam4,3)
i5=i1+i2+i3+i4
x="".join(i5)
random.shuffle(i5)
print("".join(i5)) 