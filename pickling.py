import json
d = dict(name='Bob', age=20, score=90)
try:
    import cPickle as pickle
except ImportError:
    import pickle
print pickle.dumps(d)

f1 = open('D:\MyTestFile\\dum.txt', 'wb')
pickle.dump(d, f1)
print d
f1.close()

f2 = open('D:\MyTestFile\\json.txt', 'wb')
json.dump(d, f2)
f2.close()
f2 = open('D:\MyTestFile\\json.txt', 'rb')
print f2.read()
f2.close()

f3 = open('D:\MyTestFile\\json.txt', 'rb')
d = json.load(f3)
print d

