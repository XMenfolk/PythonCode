f = open('D:\MyTestFile\\daibaoyang_case01.py', 'r')
for line in f.readlines():

    print (line.strip())
f.close()