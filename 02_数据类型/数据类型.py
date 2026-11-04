#type(要查看类型的数据)
print("Hello")
print(type("Hello"))

print(type(10))#int
print(type(3.14))#float
print(type(True))# bool
print(type(False))
print(type(None))
num = -100
print(type(num))#int

#isinstance(数据，类型)--->bool值--->判断数据是否为指定类型，如果是：True 否则：False
print(isinstance(num,int))#True
print(isinstance(num,float))#False
