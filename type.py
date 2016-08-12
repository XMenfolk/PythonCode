#coding=utf-8
def fn(self, name='World'):#先定义函数
    print ('Hello,%s.'%name)

Hello = type('Hello', (object,),dict(hello=fn))#创建Hello class

h = Hello()
h.hello()

print (type(Hello))
print (type(h))
