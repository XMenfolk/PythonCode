class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print ('My name is %s' % self.name)


s = Student('Bob')
s()

print callable([1, 2, 3])
