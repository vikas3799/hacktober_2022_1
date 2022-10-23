p=open("Sample.txt","r")
x=p.read()
print(x)

p.close()





'''
p=open("Sample.txt","w")
list1=[]
for i in range(2):
    s=input("enter your paragraph : ")
    list1.append(s+"\n")
    
x=p.writelines(list1)
print(x)
p.close()
'''
